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
    