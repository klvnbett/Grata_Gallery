from django.db import models

# Create your models here.
class Photos(models.Model):
    image=models.ImageField(upload_to='photos/')
    image_name=models.CharField(max_length=40)
    image_description=models.TextField(blank=False)