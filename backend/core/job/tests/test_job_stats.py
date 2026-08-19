import pytest

from jobs.models import Job


@pytest.mark.django_db
def test_topic_stats(api_client, user):
    Job.objects.create(
        title="Python Developer",
        salary=1000,
        positions=1,
        user=user
    )

    Job.objects.create(
        title="Senior Python Engineer",
        salary=3000,
        positions=3,
        user=user
    )

    response = api_client.get(
        "/stats/Python/"
    )

    assert response.status_code == 200

    assert response.data["total_jobs"] == 2
    assert response.data["min_salary"] == 1000
    assert response.data["max_salary"] == 3000