import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from accounts.models import UserProfile


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    user = User.objects.create_user(
        username="john@example.com",
        email="john@example.com",
        password="password123",
        first_name="John",
        last_name="Doe"
    )

    UserProfile.objects.create(
        user=user,
        test="sample test"
    )

    return user


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

    assert response.status_code == 200

    token = response.data["access"]

    api_client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token}"
    )

    return api_client