from django.db import models
from django.db.models.fields import BooleanField, NullBooleanField

# Create your models here.

class User (models.Model):
    UserName = models.CharField(max_length=10,blank=False,null=False)
    UserPassword = models.CharField(max_length=8,blank=False,null=False)
    UserPicture = models.CharField(max_length=255)
    UserType = models.BooleanField(default=False)
    UserEmail = models.EmailField(blank=False,null=False)

    
    def __str__(self):
        return self.UserName

