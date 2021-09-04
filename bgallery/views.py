from django.shortcuts import render

from .models import *
import datetime as dt


# Create your views here.

def images(request):
    images=Photo.objects.all()
    date=dt.date.today()
    users=User.objects.all()
    return render(request,'major/images.html',{'images':images,'date':date})

def search(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET('image')
        searched_image = Photo.search(search_term)
        message = f'{search_term}'
        params = {
            'images': searched_image,
            'message': message,
        }

        return render(request, 'major/search.html', params())

    else:
        message = 'Ooppss, You did not search for anything.'
        return render(request, 'major/search.html', {"message":message})

