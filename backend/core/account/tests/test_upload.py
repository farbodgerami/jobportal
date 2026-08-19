import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from accounts.models import UserProfile


@pytest.mark.django_db
def test_upload_resume(jwt_client, user):
    UserProfile.objects.filter(user=user).delete()

    pdf_file = SimpleUploadedFile(
        "resume.pdf",
        b"%PDF-1.4 test content",
        content_type="application/pdf"
    )

    response = jwt_client.put(
        "/upload/resume/",
        {"resume": pdf_file},
        format="multipart",
    )

    assert response.status_code == 200

    profile = UserProfile.objects.get(user=user)

    assert profile.resume
    assert profile.resume.name.endswith(".pdf")