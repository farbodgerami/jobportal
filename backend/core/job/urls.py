from django.urls import path
from .views import *

urlpatterns = [
    path('jobs/', getAllJobs, name='jobs'),
    path('jobs/newJob/', newJob, name='new_job'),
    path('jobs/<str:pk>/', getJob, name='job'),
    path('jobs/<str:pk>/update/', updateJob, name='update_job'),
    path('jobs/<str:pk>/delete/', deleteJob, name='delete_job'),
    path('jobs/<str:id>/apply/', applyToJob, name='apply_to_job'),
    path('jobs/<str:id>/check/', isApplied, name='is_applied_to_job'),
    path('jobs/<str:id>/candidate/', getCandidatesApplied,name='get_candidates_applied'),
    path('job/candidate/me/', getCandidatesAppliedme,name='get_candidates_applied'),
    path('stats/<str:topic>/', getTopicStats, name='get_topic_stats'),
    path('me/jobs/applied/', getCurrentUserAppliedJobs,name='current_user_applied_jobs'),
    path('me/jobs/', getCurrentUserJobs, name='current_user_jobs'),
]

 

 