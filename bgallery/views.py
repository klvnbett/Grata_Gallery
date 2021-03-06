from django.shortcuts import render
from django.http import Http404
from .models import *
import datetime as dt


# Create your views here.

def images(request):
    images=Photo.objects.all()
    date=dt.date.today()
    users=User.objects.all()
    category=Category.objects.all()
    location=Location.objects.all()
    return render(request,'major/images.html',{'images':images,'date':date,'category':category,'location':location})

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

def image(request,image_id):
    try:
        image=Photo.objects.get(id=image_id)
        photo_description=Photo.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'major/image.html',{'image':image,"photo_decription":photo_description})
    