import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile

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
        last_name="Doe",
    )

    UserProfile.objects.create(
        user=user,
        test="sample test"
    )

    return user


@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.mark.django_db
def test_register_success(api_client):
    payload = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "password": "password123"
    }

    response = api_client.post("/register/", payload, format="json")

    assert response.status_code == 200
    assert response.data["message"] == "user created"

    assert User.objects.filter(
        username="john@example.com"
    ).exists()


@pytest.mark.django_db
def test_register_existing_user(api_client):
    User.objects.create_user(
        username="john@example.com",
        email="john@example.com",
        password="password123"
    )

    payload = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "password": "password123"
    }

    response = api_client.post("/register/", payload, format="json")

    assert response.status_code == 400
    assert response.data["error"] == "User already exists"


@pytest.mark.django_db
def test_current_user(authenticated_client, user):
    response = authenticated_client.get("/me/")

    assert response.status_code == 200
    assert response.data["first_name"] == "John"
    assert response.data["last_name"] == "Doe"
    assert response.data["email"] == "john@example.com"


@pytest.mark.django_db
def test_update_user(authenticated_client, user):
    payload = {
        "first_name": "Jane",
        "last_name": "Smith",
        "username": "jane@example.com",
        "email": "jane@example.com",
        "password": "newpassword123"
    }

    response = authenticated_client.put(
        "/me/update/",
        payload,
        format="json"
    )

    assert response.status_code == 200

    user.refresh_from_db()

    assert user.first_name == "Jane"
    assert user.last_name == "Smith"
    assert user.username == "jane@example.com"
    assert user.email == "jane@example.com"
    assert user.check_password("newpassword123")


@pytest.mark.django_db
def test_update_user_without_password_change(authenticated_client, user):
    old_password_hash = user.password

    payload = {
        "first_name": "Jane",
        "last_name": "Smith",
        "username": "jane@example.com",
        "email": "jane@example.com",
        "password": ""
    }

    response = authenticated_client.put(
        "/me/update/",
        payload,
        format="json"
    )

    assert response.status_code == 200

    user.refresh_from_db()

    assert user.password == old_password_hash


@pytest.mark.django_db
def test_upload_resume(authenticated_client, user):
    UserProfile.objects.filter(user=user).delete()

    pdf_file = SimpleUploadedFile(
        "resume.pdf",
        b"dummy pdf content",
        content_type="application/pdf"
    )

    response = authenticated_client.put(
        "/upload/resume/",
        {"resume": pdf_file},
        format="multipart"
    )

    assert response.status_code == 200

    profile = UserProfile.objects.get(user=user)

    assert profile.resume.name.endswith("resume.pdf")