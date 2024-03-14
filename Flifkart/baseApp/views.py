from django.shortcuts import render
import random
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def indexpage(request):

    return render(request, "mainApp/index.html")

def loginpage(request):
    return render(request, "auth/login.html")

def registrationpage(request):
    return render(request, "auth/registration.html")


def regisformsubmitpage(request):
    if request.method == 'POST':
        username = request.POST['name']
        mail = request.POST['email']
        authpass = request.POST['password']

        _number = random.randint(1000, 9999)
        print("*************************")
        print(_number)
        subject = 'Hello, this is the subject'
        message = 'This is a test email sent from Django. and your opt is ' + str(_number)  
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [mail]  # Replace with the recipient's email address
        send_mail("This is a Subject Part", message, from_email, recipient_list)
        return render(request, "auth/otp.html")

    
    else :
        return  render(request,  "auth/registration.html")