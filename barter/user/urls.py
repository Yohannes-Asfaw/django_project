from unicodedata import name
from django.urls import path

from .views import *

urlpatterns = [

    # path('index/', index, name='index'),
    path("signup/", signup, name="signup"),
    path("login/", login_handler, name="login"),

    path('logout/', logout_handler, name='logout'),
    path('delete/', delete_profile, name="delete_profile"),

    # api related access points
    path("sendcode/", send_code, name="send_code"),
    path("checkcode/", check_code, name="check_code"),
    path("checkusername/", check_username, name="check_username"),
    path("checkemail/", check_email, name="check_email"),
]
