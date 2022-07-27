from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=100 , null=False,blank=False)


    def __str__(self):
        return self.name



class Photo(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.SET_NULL , null=True , blank= True)
    image = models.ImageField(upload_to = 'images/', null = False , blank = False)
    description = models.TextField()

    def __str__(self):
        return self.description


# class CustomUser(models.Model):
#     user = models.OneToOneField(User , on_delete=models.CASCADE)
#     name = models.CharField(max_length=150 , null = False , blank= False)
#     phone_number = models.IntegerField( blank = False , null = True)

#     def __str__(self):
#         return self.name
