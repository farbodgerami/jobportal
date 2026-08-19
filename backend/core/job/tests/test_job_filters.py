import pytest

from jobs.models import Job


@pytest.mark.django_db
def test_filter_by_keyword(api_client, user):
    Job.objects.create(
        title="Python Developer",
        salary=4000,
        user=user
    )

    Job.objects.create(
        title="Java Developer",
        salary=4000,
        user=user
    )

    response = api_client.get(
        "/jobs/?keyword=Python"
    )

    assert response.status_code == 200
    assert response.data["count"] == 1


@pytest.mark.django_db
def test_filter_by_salary(api_client, user):
    Job.objects.create(
        title="Junior",
        salary=1000,
        user=user
    )

    Job.objects.create(
        title="Senior",
        salary=10000,
        user=user
    )

    response = api_client.get(
        "/jobs/?min_salary=5000"
    )

    assert response.status_code == 200
    assert response.data["count"] == 1
