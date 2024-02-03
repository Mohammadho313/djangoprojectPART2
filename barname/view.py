def check_login_or_main(request):
    if 'username' in request.session:
        return redirect('/panel/')
    else:
        return redirect('/login/')

def login_page(request):
    msg = request.GET.get('msg', "no_msg")
    msg2 = msg.replace(" ","")
    if(msg2 is None):
        msg="no_msg"
    if(msg == "no_msg"):
        html = ""
    else:
        html = "<p>پیام سیستم: "+str(msg)+"</p>"
    html += """
    <html>   
<body>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css"/>
<style>
*{
font-family: "Vazirmatn";
direction: rtl;
}
</style>
<h3>ورود</h3>
<form action="/make_login/" method="post"/>
<input placeholder="نام کاربری" name="username"/><br>
<input type="password" placeholder="رمز عبور" name="password"/><br>
<input type="submit" value="ورود"/>
</form><br><br><br>
<a href="/create_clinic/"><button>ساخت کلینیک جدید</button></a><br>
<a href="/signup/"><button>ثبت نام</button></a>
</body>
</html>"""
    return HttpResponse(html)

def signup_page(request):
    msg = request.GET.get('msg', "no_msg")
    msg2 = msg.replace(" ","")
    if(msg2 is None):
        msg="no_msg"
    if(msg == "no_msg"):
        html = ""
    else:
        html = "<p>پیام سیستم: "+str(msg)+"</p>"
    html += """<html>   
<body>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css"/>
<style>
*{
font-family: "Vazirmatn";
direction: rtl;
}
</style>
<h3>ثبت نام</h3>
<form action="/make_signup/" method="post"/>
<input placeholder="نام کاربری" name="username"/><br>
<input type="password" placeholder="رمز عبور" name="password"/><br>
<input type="email" placeholder="ایمیل" name="email"/><br>
<input placeholder="نام" name="name"/><br>
<input placeholder="نقش(منشی/بیمار)" name="role"/><br>
<input placeholder="آیدی کلینیک(اگر منشی هستید)" name="clinic_id"/><br>
<input type="submit" value="ارسال"/>
</form><br><br><br>
<a href="/create_clinic/"><button>ساخت کلینیک</button></a><br>
<a href="/login/"><button>ورود</button></a>
</body>
</html>"""
    return HttpResponse(html)

def create_clinic_page(request):
    msg = request.GET.get('msg', "no_msg")
    msg2 = msg.replace(" ","")
    if(msg2 is None):
        msg="no_msg"
    if(msg == "no_msg"):
        html = ""
    else:
        html = "<p>پیام سیستم: "+str(msg)+"</p>"
    html += """<html>   
<body>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css"/>
<style>
*{
font-family: "Vazirmatn";
direction: rtl;
}
</style>
<h3>اضافه کردن درمانگاه</h3>
<form action="/make_add_clinic/" method="post"/>
<input placeholder="آیدی  کلینیک" name="clinic_id"/><br>
<input type="email" placeholder="ایمیل کلینیک" name="email"/><br>
<input placeholder="نام کلینیک" name="name"/><br>
<input placeholder="آدرس کلینیک" name="address"/><br>
<input placeholder="شماره موبایل کلینیک" name="phone_number"/><br>
<input placeholder="خدمات ارائه شده در کلینیک" name="services"/><br>
<input type="submit" value="ارسال"/>
</form><br><br>
<a href="/login/"><button>ورود</button></a><br>
<a href="/signup/"><button>ثبت نام</button></a>
</body>
</html>"""
    return HttpResponse(html)
def make_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = TheUser.objects.get(username=username, password=password)
        except:
            return redirect('/login?msg=نام کاربری یا رمز عبور اشتباه است')
        if user is not None:
            request.session['username'] = username
            return redirect('/panel/?msg=خوش آمدید')
        else:
            return redirect('/login?msg=نام کاربری یا رمز عبور اشتباه است')
    else:
        return redirect('/login')

def make_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        name = request.POST['name']
        role = request.POST['role']
        clinic_id = request.POST['clinic_id']
        if(role != "منشی" and role != "بیمار"):
            return redirect('/login?msg=لطفا نقش را به درستی وارد کنید')
        try:
            user = TheUser.objects.get(username=username)
            return redirect('/login?msg=نام کاربری تکراری است')
        except:
            pass
        try:
            user = TheUser.objects.get(email=email)
            return redirect('/login?msg=ایمیل تکراری است')
        except:
            pass
        if(role == "منشی"):
            if(len(clinic_id) < 1):
                return redirect('/login?msg=آیدی کلینیک نادرست است')
            try:
                user = TheUser.objects.get(clinic_id=clinic_id)
                return redirect('/login?msg=منشی دیگری برای این کلینیک وجود دارد')
            except:
                pass
        if(len(clinic_id) < 1):
            clinic_id = "not_منشی"
        user = TheUser(username=username, password=password,clinic_id=clinic_id,email=email,name=name,role=role)
        user.save()
        request.session['username'] = username
        return redirect('/panel/?msg=خوش آمدید')
    else:
        return redirect('/login')


def add_clinic(request):
    if request.method == 'POST':
        clinic_id = request.POST['clinic_id']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        services = request.POST['services']
        try:
            user = TheClinic.objects.get(email=email)
            return redirect('/login?msg=ایمیل تکراری است')
        except:
            pass
        try:
            user = TheClinic.objects.get(clinic_id=clinic_id)
            return redirect('/login?msg=آیدی کلینیک تکراری است')
        except:
            pass
        clinic = TheClinic(clinic_id=clinic_id, email=email,name=name,address=address,phone_number=phone_number, services=services)
        clinic.save()
        return redirect('/panel/')
    else:
        return redirect('/login')

def panel(request):
    if 'username' not in request.session:
        return redirect('../login/')
    user = TheUser.objects.get(username=request.session['username'])
    msg = request.GET.get('msg', "no_msg")
    msg2 = msg.replace(" ","")
    if(msg2 is None):
        msg="no_msg"
    if(msg == "no_msg"):
        html = ""
    else:
        html = "<p>پیام سیستم: "+str(msg)+"</p>"
    if(user.role == "بیمار"):
        
        html += """<html>   
    <body>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css"/>
<style>
*{
font-family: "Vazirmatn";
direction: rtl;
}
</style>
    <h1>پنل کاربری بیمار</h1><br>
    <a href="/panel/new_appointment"><button>نوبت ویزیت جدید</button></a><br><br>
    <a href="/panel/my_appointments"><button>نوبت های ویزیت من</button></a><br><br><br>
    <a href="/panel/list_clinics"><button>مشاهده لیست کلینیک ها</button></a><br><br>
    <a href="/panel/logout"><button>خروج از حساب کاربری</button></a>
    </body>
    </html>"""
    if(user.role == "منشی"):
        html = """<html>   
    <body>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css"/>
<style>
*{
font-family: "Vazirmatn";
direction: rtl;
}
</style>
    <h1>پنل کاربری منشی</h1><br>

    <a href="/panel/pending_appointments"><button>نوبت های در انتظار تایید</button></a><br><br>
    <a href="/panel/confirmed_appointments"><button>نوبت های تایید شده</button></a><br><br>
        <a href="/panel/rejected_appointments"><button>نوبت های رد شده</button></a><br><br>
    <a href="/panel/expired_appointments"><button>نوبت های گذشته</button></a><br><br>
    
    <a href="/panel/logout"><button>خروج از حساب کاربری</button></a>
    </body>
    </html>"""
    return HttpResponse(html)
