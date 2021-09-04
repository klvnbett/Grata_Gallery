from django.shortcuts import render

from .models import *
import datetime as dt


# Create your views here.

def images(request):
    images=Photo.objects.all()
    date=dt.date.today()
    users=User.objects.all()
    return render(request,'major/images.html',{'images':images,'date':date})