from django.urls import path
from . import  views

urlpatterns = [
  path("signup/", views.signupaccount, name='signup'),
  path("logout/", views.logoutaccount, name='logout'),
  path("login/", views.loginaccount, name='login')
]