from django.urls import path, include
from .views import *
from ownauth import views

# from Aunthentication import views
from Aunthentication.views import registerpage
# from Aunthentication.views import *



urlpatterns = [
    path("", indexpage),
    # path("singup/", include("ownauth.urls"), name="singup"),
    path("singup/", views.signuppage , name="singup"),
    path("newregister/", registerpage, name="newregister"),
    
]