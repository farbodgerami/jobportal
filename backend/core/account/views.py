from django.shortcuts import render
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
def register(request):
    data=request.data
    user=SignUpSerializer(data=data)
    if user.is_valid():
        # print(user)
        if not User.objects.filter(username=data['email']).exists():
            user=User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password'])
            )
            # print('done......................')
            return Response({'message':"user created"},status=status.HTTP_200_OK)
        else:
            return Response({'error':"User already exists"},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user.errors)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def currentUser(request):
   
    user=UserSerializer(request.user)
    return Response(user.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateUser(request):
    user=request.user
    data=request.data
    user.first_name=data['first_name']
    user.last_name=data['last_name']
    user.username=data['username']
    user.email=data['email']
    if data['password']!='':
        user.password=make_password(data['password'])
    user.save()
    user=UserSerializer(request.user)
    return Response(user.data)




from .validators import validate_file_extension
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def uploadResume(request):

    user = request.user
    resume = request.FILES['resume']

    if resume == '':
        return Response({ 'error': 'Please upload your resume.' }, status=status.HTTP_400_BAD_REQUEST)

    isValidFile = validate_file_extension(resume.name)

    # if not isValidFile:
    #   return Response({ 'error': 'Please upload only pdf file.' }, status=status.HTTP_400_BAD_REQUEST)
    userprofile=UserProfile.objects.create(user=user,resume=resume)
    serializer = UserSerializer(user, many=False)
    
    userprofile.resume = resume
    userprofile.save()

    return Response(serializer.data)