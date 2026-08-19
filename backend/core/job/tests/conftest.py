import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from jobs.models import Job
from account.models import UserProfile


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    user = User.objects.create_user(
        username="john@example.com",
        email="john@example.com",
        password="password123"
    )

    UserProfile.objects.create(
        user=user,
        resume="resume.pdf"
    )

    return user


@pytest.fixture
def another_user():
    return User.objects.create_user(
        username="owner@example.com",
        email="owner@example.com",
        password="password123"
    )


@pytest.fixture
def jwt_client(api_client, user):
    response = api_client.post(
        "/api/token/",
        {
            "username": "john@example.com",
            "password": "password123",
        },
        format="json",
    )

    token = response.data["access"]

    api_client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token}"
    )

    return api_client


@pytest.fixture
def job(user):
    return Job.objects.create(
        title="Python Developer",
        description="Django Developer",
        email="hr@test.com",
        address="New York",
        salary=5000,
        company="ABC",
        user=user
    )