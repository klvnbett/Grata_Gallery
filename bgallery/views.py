from django.shortcuts import render

# from .models import *


# Create your views here.

def images(request):
    return render(request,'major/images.html')