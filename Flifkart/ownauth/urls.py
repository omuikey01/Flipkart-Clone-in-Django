from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", signuppage, name="signup"),
    path("regis/", regispage, name="regis"),
    path("otpsubmit/", otppage, name="otpsubmit"),
]
