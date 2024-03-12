from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import RegisterAdmin
from django.shortcuts import HttpResponse
import random

# Create your views here.

random_number = 0

def signuppage(request):
    return render(request, "registration.html")

def regispage(request) :
    
    if request.method == "POST":

        # name, email, pass1

        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password']

        # user = RegisterAdmin.objects.filter(email = email)
        # if user :
        #     pass
        # else :
        _number = random.randint(1000, 9999)
        global random_number
        random_number += _number
        subject = 'Hello, this is the subject'

        message = 'This is a test email sent from Django. and your opt is ' + str(_number)  

        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['uikeyom1234@gmail.com']  # Replace with the recipient's email address
        send_mail(subject, message, from_email, recipient_list)

        return render(request, "otp.html")
    
            
def otppage(request):

    if request.method == "POST":

        otp_num = request.POST['otp']
        otp_num = int(otp_num)
        
        print("******************************")
        print(otp_num, type(otp_num))
        print(random_number)

        if otp_num == random_number :
            return render(request, "login.html")
        else :
            return render(request, "registration.html")
