from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import CommonRegisterView, upgrade_me

app_name = 'sign'

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),
    path('signup/',
         CommonRegisterView.as_view(template_name = 'sign/signup.html'),
         name='signup'),
    path('upgrade/', upgrade_me, name='upgrade'),
]