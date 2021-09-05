from django.test import TestCase
from .models import *
import datetime as dt



# create your test here
class UserTestClass(TestCase):
    #setup method
    def setUp(self):
        self.kelvin=User(firstname="kelvin",lastname="kipkemoi",email="kelvin.bett@student.moringaschool.com",phone_number="1234567890")
    
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kelvin,User))
        
    #Testing save method
    def test_save_method(self):
        self.kelvin.save_user()
        users=User.objects.all()
        self.assertTrue(len(users)>0)
        
    #Testing delete method
    def test_delete_method(self):
        self.kelvin.save_user()
        self.kelvin.delete_user()
        users=User.objects.all()
        self.assertTrue(len(users)==0)    
    

class PhotoTestCase(TestCase):
    #setup method
    def setup(self):
        self.photo=Photo(photo="media/photos/great.PNG",photo_name="great",photo_description="This is a photo descriping strength of men",user="kelvin",category="men",location="Kenya",pub_date=dt.today())
    
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Photo))