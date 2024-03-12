from django.shortcuts import render

# Create your views here.


def registerpage(request):
    return render(request, "Myregistration.html")