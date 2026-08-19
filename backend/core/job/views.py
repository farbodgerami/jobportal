from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from account.models import UserProfile
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination
from .filters import *
from rest_framework.permissions import IsAuthenticated

"""
Django REST API views for managing jobs and job applications.

This module provides API endpoints for:
- Listing and filtering available jobs.
- Retrieving individual job details.
- Creating, updating, and deleting jobs.
- Retrieving job statistics by topic.
- Applying for jobs.
- Checking and retrieving a user's job applications.
- Retrieving candidates who applied to a user's job.

Authenticated endpoints require the user to be logged in and enforce
ownership checks where appropriate.
"""

@api_view(["GET"])
def getAllJobs(request):
    """
    Retrieve a paginated list of all jobs.

    Supports filtering through ``JobsFilter`` using query parameters.
    Results are ordered by job ID and limited to three jobs per page.

    Args:
        request: Django REST Framework HTTP request containing optional
            filtering and pagination query parameters.

    Returns:
        Response: JSON response containing the total number of matching
        jobs, the number of results per page, and the serialized jobs.
    """
    
 
    filterset=JobsFilter(request.GET,queryset=Job.objects.all().order_by('id'))
 
    count=filterset.qs.count() 
    resPerPage=3
    paginator=PageNumberPagination()
    paginator.page_size=resPerPage
    queryset=paginator.paginate_queryset(filterset.qs,request)
    serializer = JobSerializer(queryset, many=True)
    
    return Response({"count":count,"resPerPage":resPerPage,"jobs":serializer.data})


@api_view(["GET"])
def getJob(request, pk):
    """
    Retrieve a single job and the number of candidates who applied.

    Args:
        request: Django REST Framework HTTP request.
        pk: Primary key of the job to retrieve.

    Returns:
        Response: Serialized job information and the number of candidates
        who have applied to the job.

    Raises:
        Http404: If a job with the given primary key does not exist.
    """
    job = get_object_or_404(Job, id=pk)
    candidates=CandidatesApplied.objects.filter(job=job).count()
    serializer = JobSerializer(job, many=False)
 
    return Response({'job':serializer.data,'candidates':candidates})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def newJob(request):
    """
    Create a new job for the authenticated user.

    The authenticated user is automatically assigned as the owner of
    the newly created job.

    Args:
        request: Authenticated Django REST Framework HTTP request
            containing the job data.

    Returns:
        Response: Serialized representation of the newly created job.

    Raises:
        NotAuthenticated: If the request is not authenticated.
    """
    
    request.data['user']=request.user
    data = request.data
    job = Job.objects.create(**data)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateJob(request, pk):
    """
    Update an existing job owned by the authenticated user.

    Only the user who created the job is permitted to update it.

    Args:
        request: Authenticated Django REST Framework HTTP request
            containing the updated job data.
        pk: Primary key of the job to update.

    Returns:
        Response: Serialized representation of the updated job.

    Raises:
        Http404: If the specified job does not exist.
        NotAuthenticated: If the request is not authenticated.
    """
    job = get_object_or_404(Job, id=pk)
    
    if request.user!=job.user:
        return Response({'message':'you cannot update this job'},status=status.HTTP_400_BAD_REQUEST)
    job.title = request.data['title']
    job.description = request.data['description']
    job.email = request.data['email']
    job.address = request.data['address']
    job.education = request.data['jobType']
    job.education = request.data['education']
    job.industry = request.data['industry']
    job.experience = request.data['experience']
    job.salary = request.data['salary']
    job.positions = request.data['positions']
    job.company = request.data['company']
    job.save()
    serializer = JobSerializer(job, many=False)
 
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteJob(request, pk):
    """
    Delete a job owned by the authenticated user.

    Only the user who created the job is permitted to delete it.

    Args:
        request: Authenticated Django REST Framework HTTP request.
        pk: Primary key of the job to delete.

    Returns:
        Response: Confirmation message indicating that the job was deleted.

    Raises:
        Http404: If the specified job does not exist.
        NotAuthenticated: If the request is not authenticated.
    """
    job = get_object_or_404(Job, id=pk)
    if request.user!=job.user:
        return Response({'message':'you cannot delete this job'},status=status.HTTP_400_BAD_REQUEST)
    job.delete()
    serializer = JobSerializer(job, many=False)
    return Response({"message": "job is deleted"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getTopicStats(requeset, topic):
    """
    Calculate statistics for jobs whose titles contain a given topic.

    The statistics include the total number of matching jobs, average
    number of positions, average salary, minimum salary, and maximum salary.

    Args:
        request: Django REST Framework HTTP request.
        topic: Text used to search job titles.

    Returns:
        Response: Aggregated statistics for matching jobs, or an error
        message if no matching jobs are found.
    """
    args = {'title__contains': topic}
 
    jobs = Job.objects.filter(**args)
  
    if len(jobs) == 0:
        return Response({"message": f"Not Status found for ${topic}"})
    stats = jobs.aggregate(total_jobs=Count('title'),
                             avg_positions=Avg('positions'),
          avg_salary=Avg('salary'), 
          min_salary=Min('salary'), 
          max_salary=Max('salary'))
    
    return Response(stats)

from django.utils import timezone
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def applyToJob(request,id):
    """
    Submit a job application for the authenticated user.

    The user must have uploaded a resume, the job application deadline
    must not have passed, and the user must not have already applied
    to the same job.

    Args:
        request: Authenticated Django REST Framework HTTP request.
        id: Primary key of the job to apply for.

    Returns:
        Response: Confirmation containing the application ID.

    Raises:
        Http404: If the job or user's profile does not exist.
        NotAuthenticated: If the request is not authenticated.
    """
    user=request.user
   
    job=get_object_or_404(Job,id=id)
    userprofile=get_object_or_404(UserProfile,user=user)
    if userprofile.resume == "":
        return Response({"error":'please upload your resume first'},status=status.HTTP_400_BAD_REQUEST)
    if job.lastDate < timezone.now():
        return Response({"error":'you can not applyn to this job. Date is over'},status=status.HTTP_400_BAD_REQUEST)
    
 
    alreadyApplied=CandidatesApplied.objects.filter(user=user,job=job).exists()
 
    if alreadyApplied:
        return Response({"error":'you have already applied to this job'},status=status.HTTP_400_BAD_REQUEST)
    
    jobApplied=CandidatesApplied.objects.create(job=job,user=user,resume=userprofile.resume)

    return Response({'applied':True,'job_id':jobApplied.id},status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getCurrentUserAppliedJobs(request):
    """
    Retrieve all jobs the authenticated user has applied to.

    Args:
        request: Authenticated Django REST Framework HTTP request.

    Returns:
        Response: Serialized list of the user's job applications.

    Raises:
        NotAuthenticated: If the request is not authenticated.
    """
     
    candidates=CandidatesApplied.objects.filter(user_id= request.user.id)
   
    serializer=CandidatesAppliedSerializer(candidates,many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def isApplied(request,id):
    """
    Check whether the authenticated user has applied to a specific job.

    Args:
        request: Authenticated Django REST Framework HTTP request.
        id: Primary key of the job to check.

    Returns:
        Response: Boolean indicating whether the user has already applied.

    Raises:
        Http404: If the specified job does not exist.
        NotAuthenticated: If the request is not authenticated.
    """
    user=request.user
    job=get_object_or_404(Job,id=id)
 
    alreadyApplied=CandidatesApplied.objects.filter(user=user,job=job).exists()
    return Response(alreadyApplied)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getCurrentUserJobs(request,):
    """
    Retrieve all jobs created by the authenticated user.

    Args:
        request: Authenticated Django REST Framework HTTP request.

    Returns:
        Response: Serialized list of jobs owned by the current user.

    Raises:
        NotAuthenticated: If the request is not authenticated.
    """
    jobs=Job.objects.filter(user_id=request.user.id)
    serializers=JobSerializer(jobs,many=True)
    return Response(serializers.data)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getCandidatesApplied(request,id):
    """
    Retrieve all candidates who applied to a specific job.

    Only the user who owns the job is authorized to view its applicants.

    Args:
        request: Authenticated Django REST Framework HTTP request.
        id: Primary key of the job whose applicants should be retrieved.

    Returns:
        Response: Serialized list of candidates who applied to the job.

    Raises:
        Http404: If the specified job does not exist.
        NotAuthenticated: If the request is not authenticated.
    """
 
    user=request.user
    job=get_object_or_404(Job,id=id)
    if job.user != user:
        return Response({'error':'you can not access this job'},status=status.HTTP_403_FORBIDDEN)
    
    candidates=job.candidatesapplied_set.all()
 
    serializer=CandidatesAppliedSerializer(candidates,many=True)
    return Response(serializer.data)

 
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getCandidatesAppliedme(request):
    """
    Retrieve candidates associated with the authenticated user's job.

    Args:
        request: Authenticated Django REST Framework HTTP request.

    Returns:
        Response: Serialized list of candidates associated with the job.

    Raises:
        Http404: If the corresponding job does not exist.
        NotAuthenticated: If the request is not authenticated.
    """
    user=request.user
    job=get_object_or_404(Job,id=user.id)
    candidates=CandidatesApplied.objects.filter(job=job)
    serializer=CandidatesAppliedSerializer(candidates,many=True)
    return Response(serializer.data)