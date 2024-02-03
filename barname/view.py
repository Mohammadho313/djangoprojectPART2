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