 
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# from django.contrib.gis.db import models as gismodels
# from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from datetime import *
# import geocoder
import os

class JobType(models.TextChoices):
    Permanent="Permanent"
    Temporary="Temporary"
    Internship="Internship"

class Education(models.TextChoices):
    Bachelors="Bachelors"
    Masters='Masters'
    Phd='Phd'
# from enum import Enum
# class Education(Enum):
#     Bachelors="Bachelors"
#     Masters='Masters'
#     Phd='Phd'
# JobType={"Permanent":"Permanent","Temporary":"Temporary","InterShip":"InterShip",}

class Industry(models.TextChoices):
    Business="Business"
    IT="IT"
    Banking="Banking"
    EducationTelecommunication="Telecommunication"
    Others="Others"

class Experience(models.TextChoices):
    NO_EXPERIENCE="No Experience"
    ONE_YEAR="1 year"
    TWO_YAER="2 years"
    THREE_YEAR_PLUS="3 years above"

def return_date_time():
    now=datetime.now()
    return now+timedelta(days=10)

class Job(models.Model):
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    email=models.EmailField(null=True)
    address=models.CharField(max_length=255,null=True)
    jobType=models.CharField(max_length=20,choices=JobType.choices,default=JobType.Permanent)
    education=models.CharField(max_length=20,choices=Education.choices,default=Education.Bachelors)
    industry=models.CharField(max_length=20,choices=Industry.choices,default=Industry.Business)
    experience=models.CharField(max_length=20,choices=Experience.choices,default=Experience.NO_EXPERIENCE)
    salary=models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(1000000)])
    positions=models.IntegerField(default=1)
    company= models.CharField(max_length=100,null=True)
    # point=gismodels.PointField(default=Point(0.0,0.0))
    lastDate=models.DateTimeField(default=return_date_time)
    user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    createdAt=models.DateTimeField(auto_now_add=True)

    # def save(self,*args,**kwargs):
    #     g=geocoder.mapquest(self.address,key=os.environ.get('GEOCODER_API'))
    #     lng =g.lng
    #     lat =g.lat

    #     self.point =Point(lng,lat)
    #     super(Job,self).save(*args,**kwargs)
     

class CandidatesApplied(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    resume=models.CharField(max_length=200)
    appliedAt=models.DateTimeField(auto_now_add=True)
    