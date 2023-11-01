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
@api_view(["GET"])
def getAllJobs(request):
    # print('ddddddddddddddd',request.GET )#ddddddddddddddd <QueryDict: {'keyword': [''], 'location': [''], 'a': ['t,y']}>>
    # jobs = Job.objects.all()
    filterset=JobsFilter(request.GET,queryset=Job.objects.all().order_by('id'))
    # pagination
    count=filterset.qs.count() 
    resPerPage=3
    paginator=PageNumberPagination()
    paginator.page_size=resPerPage
    queryset=paginator.paginate_queryset(filterset.qs,request)
    serializer = JobSerializer(queryset, many=True)
    # print("aaaad")
    # to go to next page: jobs/?page=2
    return Response({"count":count,"resPerPage":resPerPage,"jobs":serializer.data})


@api_view(["GET"])
def getJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    candidates=CandidatesApplied.objects.filter(job=job).count()
    serializer = JobSerializer(job, many=False)
 
    return Response({'job':serializer.data,'candidates':candidates})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def newJob(request):
    # adding user to request.data
    request.data['user']=request.user
    data = request.data
    job = Job.objects.create(**data)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    # print('llllllllllllll',job.user)
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
    # print(serializer.data)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    if request.user!=job.user:
        return Response({'message':'you cannot delete this job'},status=status.HTTP_400_BAD_REQUEST)
    job.delete()
    serializer = JobSerializer(job, many=False)
    return Response({"message": "job is deleted"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getTopicStats(requeset, topic):
    args = {'title__contains': topic}
    # print(topic)
    jobs = Job.objects.filter(**args)
    # print(jobs)
    if len(jobs) == 0:
        return Response({"message": f"Not Status found for ${topic}"})
    stats = jobs.aggregate(total_jobs=Count('title'),
                             avg_positions=Avg('positions'),
          avg_salary=Avg('salary'), 
          min_salary=Min('salary'), 
          max_salary=Max('salary'))
    # print(stats)
    return Response(stats)

from django.utils import timezone
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def applyToJob(request,id):
    user=request.user
    # print('ddddddddddddddddddd',user)
    job=get_object_or_404(Job,id=id)
    userprofile=get_object_or_404(UserProfile,user=user)
    if userprofile.resume == "":
        return Response({"error":'please upload your resume first'},status=status.HTTP_400_BAD_REQUEST)
    if job.lastDate < timezone.now():
        return Response({"error":'you can not applyn to this job. Date is over'},status=status.HTTP_400_BAD_REQUEST)
    
 
    alreadyApplied=CandidatesApplied.objects.filter(user=user,job=job).exists()
    # related name for CandidatesApplied
    # alreadyApplied=job.candidatesapplied_set.filter(user=user).exists()

    if alreadyApplied:
        return Response({"error":'you have already applied to this job'},status=status.HTTP_400_BAD_REQUEST)
    
    jobApplied=CandidatesApplied.objects.create(job=job,user=user,resume=userprofile.resume)

    return Response({'applied':True,'job_id':jobApplied.id},status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getCurrentUserAppliedJobs(request):
    # args={'user_id': request.user.id}
    candidates=CandidatesApplied.objects.filter(user_id= request.user.id)
    # candidates=CandidatesApplied.objects.filter(**args)
    serializer=CandidatesAppliedSerializer(candidates,many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def isApplied(request,id):
    user=request.user
    job=get_object_or_404(Job,id=id)
    # applied=job.candidatesapplied_set.filter(user=user).exists()
    # return Response(applied)
    alreadyApplied=CandidatesApplied.objects.filter(user=user,job=job).exists()
    return Response(alreadyApplied)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getCurrentUserJobs(request,):
    jobs=Job.objects.filter(user_id=request.user.id)
    serializers=JobSerializer(jobs,many=True)
    return Response(serializers.data)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getCandidatesApplied(request,id):
    # print(id)
    user=request.user
    job=get_object_or_404(Job,id=id)
    if job.user != user:
        return Response({'error':'you can not access this job'},status=status.HTTP_403_FORBIDDEN)
    
    candidates=job.candidatesapplied_set.all()
    # candidates=CandidatesApplied.objects.filter(job=job)
    serializer=CandidatesAppliedSerializer(candidates,many=True)
    return Response(serializer.data)

# vase khodam:
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getCandidatesAppliedme(request):
    user=request.user
    job=get_object_or_404(Job,id=user.id)
    candidates=CandidatesApplied.objects.filter(job=job)
    serializer=CandidatesAppliedSerializer(candidates,many=True)
    return Response(serializer.data)