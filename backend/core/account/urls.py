from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register, name='register'),
    path('me/', currentUser, name='currentuser'),
    path('me/update/',updateUser,name='updateuser'),
    
    path('upload/resume/',uploadResume, name='upload_resume'),

]
