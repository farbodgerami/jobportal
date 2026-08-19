from django.shortcuts import render
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.permissions import IsAuthenticated


"""
API views for user registration, authentication, profile management,
and resume uploads.

This module provides Django REST Framework endpoints that allow users to:
- Register a new account.
- Retrieve the currently authenticated user's information.
- Update the authenticated user's profile and password.
- Upload and associate a resume with their user profile.

Authenticated endpoints require the `IsAuthenticated` permission.
"""

@api_view(["POST"])
def register(request):
    """
    Register a new user account.

    Validates the submitted registration data using `SignUpSerializer`.
    If the email is not already associated with an existing user, a new
    Django `User` object is created with a securely hashed password.

    Args:
        request: HTTP request containing the user's registration data,
            including first name, last name, email, and password.

    Returns:
        Response:
            HTTP 200 with a success message if the user is created.
            HTTP 400 if a user with the provided email already exists.
            Validation errors if the submitted data is invalid.
    """
    data=request.data
    user=SignUpSerializer(data=data)
    if user.is_valid():
       
        if not User.objects.filter(username=data['email']).exists():
            user=User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password'])
            )
             
            return Response({'message':"user created"},status=status.HTTP_200_OK)
        else:
            return Response({'error':"User already exists"},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user.errors)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def currentUser(request):
    """
    Retrieve the currently authenticated user's information.

    This endpoint requires authentication and serializes the authenticated
    Django user using `UserSerializer`.

    Args:
        request: HTTP request containing the authenticated user.

    Returns:
        Response: Serialized information about the authenticated user.
    """
   
    user=UserSerializer(request.user)
    return Response(user.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateUser(request):
    """
    Update the currently authenticated user's profile.

    Updates the user's first name, last name, username, and email.
    If a new password is provided, it is securely hashed before being saved.

    Args:
        request: HTTP request containing the updated user information.

    Returns:
        Response: Serialized information about the updated user.
    """
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
    """
    Upload a resume for the currently authenticated user.

    Retrieves the uploaded resume from the request, validates its file
    extension, and associates it with the authenticated user's profile.

    Args:
        request: HTTP request containing the resume file under the
            `resume` field.

    Returns:
        Response:
            Serialized user information after the resume is uploaded.

    Raises:
        KeyError: If the request does not contain a `resume` file.
    """

    user = request.user
    resume = request.FILES['resume']

    if resume == '':
        return Response({ 'error': 'Please upload your resume.' }, status=status.HTTP_400_BAD_REQUEST)

    isValidFile = validate_file_extension(resume.name)

     
    userprofile=UserProfile.objects.create(user=user,resume=resume)
    serializer = UserSerializer(user, many=False)
    
    userprofile.resume = resume
    userprofile.save()

    return Response(serializer.data)