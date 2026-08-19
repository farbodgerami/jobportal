import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_get_jwt_token(api_client):
    User.objects.create_user(
        username="john@example.com",
        email="john@example.com",
        password="password123"
    )

    response = api_client.post(
        "/api/token/",
        {
            "username": "john@example.com",
            "password": "password123",
        },
        format="json",
    )

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data


 

@pytest.mark.django_db
def test_current_user_requires_authentication(api_client):
    response = api_client.get("/me/")

    assert response.status_code == 401

 
@pytest.mark.django_db
def test_current_user(jwt_client):
    response = jwt_client.get("/me/")

    assert response.status_code == 200
    assert response.data["email"] == "john@example.com"
    assert response.data["first_name"] == "John"

 

@pytest.mark.django_db
def test_update_user(jwt_client, user):
    response = jwt_client.put(
        "/me/update/",
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "username": "jane@example.com",
            "email": "jane@example.com",
            "password": "newpassword123",
        },
        format="json",
    )

    assert response.status_code == 200

    user.refresh_from_db()

    assert user.first_name == "Jane"
    assert user.last_name == "Smith"
    assert user.username == "jane@example.com"
    assert user.email == "jane@example.com"
    assert user.check_password("newpassword123")