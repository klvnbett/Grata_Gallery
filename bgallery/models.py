from django.db import models
import datetime as dt

# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=30)
    user = models.ForeignKey('User',on_delete=models.CASCADE,)

class User(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number=models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        return self.firstname

class Location(models.Model):
    location=models.CharField(max_length=30)
    user = models.ForeignKey('User',on_delete=models.CASCADE,)
        
class Photo(models.Model):
    photo=models.ImageField(upload_to='photos/',default="Photo")
    photo_name=models.CharField(max_length=40)
    photo_description=models.TextField(blank=False,default="Photo description")
    user = models.ForeignKey('User',on_delete=models.CASCADE,)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    pub_date=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.photo_name
    
    def save_photo(self):
        self.save()

    @classmethod
    def search(cls,search_term):
        image=cls.objects.filter(title__icontains=search_term)
        return image

