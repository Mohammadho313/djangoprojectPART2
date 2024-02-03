from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_login_or_main),
    path('login/', views.login_page),
    path('signup/', views.signup_page),
    path('create_clinic/', views.create_clinic_page),
    path('make_login/', views.make_login),
    path('make_signup/', views.make_signup),
    path('make_add_clinic/', views.add_clinic),
    path('panel/', views.panel),
    path('panel/new_appointment/', views.new_appointment),
    path('panel/make_new_appointment/', views.make_new_appointment),
    path('panel/my_ap  pointments/', views.my_appointments),
    path('panel/cancel_appointment/', views.cancel_appointment),
    path('panel/list_clinics/', views.list_clinics),
    path('panel/logout/', views.make_logout),
    path('panel/pending_appointments/', views.pending_appointments),
    path('panel/approve_appointment/', views.approve_appointment),
    path('panel/confirmed_appointments/', views.confirmed_appointments),








]