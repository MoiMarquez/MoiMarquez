from django.contrib import admin

from login import models
from . import models 

# Register your models here.

admin.site.register(models.User)