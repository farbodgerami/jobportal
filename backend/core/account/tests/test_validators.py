import pytest

from accounts.validators import validate_file_extension


@pytest.mark.parametrize(
    "filename,expected",
    [
        ("resume.pdf", True),
        ("resume.PDF", True),
        ("resume.docx", False),
        ("resume.txt", False),
        ("resume.jpg", False),
    ],
)
def test_validate_file_extension(filename, expected):
    assert validate_file_extension(filename) is expected