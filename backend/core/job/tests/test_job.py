import pytest
from jobs.models import Job

 
 
@pytest.mark.django_db
def test_get_all_jobs(api_client, user):
    Job.objects.create(
        title="Python Developer",
        address="New York",
        salary=5000,
        user=user
    )

    response = api_client.get("/jobs/")

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert len(response.data["jobs"]) == 1


@pytest.mark.django_db
def test_get_job(api_client, job):
    response = api_client.get(f"/jobs/{job.id}/")

    assert response.status_code == 200
    assert response.data["job"]["title"] == "Python Developer"
    assert response.data["candidates"] == 0

 


@pytest.mark.django_db
def test_create_job(jwt_client):
    payload = {
        "title": "Backend Engineer",
        "description": "Python",
        "email": "jobs@test.com",
        "address": "London",
        "salary": 7000,
        "positions": 2,
        "company": "OpenAI"
    }

    response = jwt_client.post(
        "/jobs/newJob/",
        payload,
        format="json"
    )

    assert response.status_code == 200

    assert Job.objects.filter(
        title="Backend Engineer"
    ).exists()


import pytest


@pytest.mark.django_db
def test_update_own_job(jwt_client, job):
    payload = {
        "title": "Senior Python Developer",
        "description": job.description,
        "email": job.email,
        "address": job.address,
        "jobType": job.jobType,
        "education": job.education,
        "industry": job.industry,
        "experience": job.experience,
        "salary": 9000,
        "positions": job.positions,
        "company": job.company,
    }

    response = jwt_client.put(
        f"/jobs/{job.id}/update/",
        payload,
        format="json"
    )

    assert response.status_code == 200

    job.refresh_from_db()

    assert job.title == "Senior Python Developer"
    assert job.salary == 9000


import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_update_other_user_job_denied(api_client, another_user, job):
    response = api_client.post(
        "/api/token/",
        {
            "username": another_user.username,
            "password": "password123",
        },
        format="json"
    )

    token = response.data["access"]

    api_client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token}"
    )

    payload = {
        "title": "Hack",
        "description": job.description,
        "email": job.email,
        "address": job.address,
        "jobType": job.jobType,
        "education": job.education,
        "industry": job.industry,
        "experience": job.experience,
        "salary": job.salary,
        "positions": job.positions,
        "company": job.company,
    }

    response = api_client.put(
        f"/jobs/{job.id}/update/",
        payload,
        format="json"
    )

    assert response.status_code == 400




@pytest.mark.django_db
def test_delete_job(jwt_client, job):
    response = jwt_client.delete(
        f"/jobs/{job.id}/delete/"
    )

    assert response.status_code == 200

    assert not Job.objects.filter(
        id=job.id
    ).exists()








