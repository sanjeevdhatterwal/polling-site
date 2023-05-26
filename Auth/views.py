from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView as Logout
# Create your views here.
class Login(LoginView):
    template_name = 'Auth/login.html'
    redirect_authenticated_user = True
