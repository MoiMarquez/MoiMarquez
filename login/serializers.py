from django.db.models import fields
from rest_framework import serializers
from . import models

class UsersSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields =  ["id","UserName","UserPassword","UserPicture","UserType", "UserEmail" ]