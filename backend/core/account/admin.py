from django.contrib import admin

from django.contrib import admin
from .models import *

class uerprofilesg(admin.ModelAdmin):
    list_display=['id','user']
admin.site.register(UserProfile,uerprofilesg)