from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


from . import views

urlpatterns=[
    url(r'^$',views.images,name='images'),
    url(r'^search$',views.search,name='search'),
    url(r'^image/(\d+)',views.image,name='image'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)