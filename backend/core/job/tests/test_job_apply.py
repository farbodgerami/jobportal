import pytest

from jobs.models import CandidatesApplied


@pytest.mark.django_db
def test_apply_to_job(jwt_client, job):
    response = jwt_client.post(
        f"/jobs/{job.id}/apply/"
    )

    assert response.status_code == 200

    assert response.data["applied"] is True

    assert CandidatesApplied.objects.filter(
        job=job
    ).exists()


import pytest

from jobs.models import CandidatesApplied


@pytest.mark.django_db
def test_apply_twice(jwt_client, user, job):
    CandidatesApplied.objects.create(
        user=user,
        job=job,
        resume="resume.pdf"
    )

    response = jwt_client.post(
        f"/jobs/{job.id}/apply/"
    )

    assert response.status_code == 400

    assert response.data["error"] == (
        "you have already applied to this job"
    )


import pytest

from jobs.models import CandidatesApplied


@pytest.mark.django_db
def test_is_applied(jwt_client, user, job):
    CandidatesApplied.objects.create(
        user=user,
        job=job,
        resume="resume.pdf"
    )

    response = jwt_client.get(
        f"/jobs/{job.id}/check/"
    )

    assert response.status_code == 200
    assert response.data is True


import pytest

from jobs.models import CandidatesApplied


@pytest.mark.django_db
def test_current_user_applied_jobs(jwt_client, user, job):
    CandidatesApplied.objects.create(
        user=user,
        job=job,
        resume="resume.pdf"
    )

    response = jwt_client.get(
        "/me/jobs/applied/"
    )

    assert response.status_code == 200
    assert len(response.data) == 1

