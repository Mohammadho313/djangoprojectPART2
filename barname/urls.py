from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_login_or_main),
    path('login/', views.login_page),
    path('signup/', views.signup_page),