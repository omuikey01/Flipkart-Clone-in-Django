from django.urls import path, include
from .views import *
# from ownauth import views

urlpatterns = [
    path("", indexpage),
    path("login/", loginpage, name="login"),
    path("registration/", registrationpage, name="registration"),
    path("regisformsubmit/", regisformsubmitpage, name="regisformsubmit"),
]

# regisformsubmit