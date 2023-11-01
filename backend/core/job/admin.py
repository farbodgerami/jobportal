from django.contrib import admin
from .models import *
# Register your models here.


class jobShow(admin.ModelAdmin):
    list_display=['title','user','jobType','education','industry','salary']
admin.site.register(Job,jobShow)



class candidateShow(admin.ModelAdmin):
    list_display=['id','user','job','resume']
admin.site.register(CandidatesApplied,candidateShow)