# tests/test_password_protect.py

import pikepdf, string
from ..PDF_Password_Protect import generate_password

def test_generate_password():
    password = generate_password()
    assert len(password) == 20
    assert any(char.isdigit() for char in password)
    assert any(char.isupper() for char in password)
    assert any(char.islower() for char in password)
    assert any(char in string.punctuation for char in password)

def test_password_protect_pdf(tmp_path):
    pdf_path = tmp_path / "test.pdf"
    owner_password = "owner_password"
    user_password = generate_password()

    # Create a sample PDF file
    with pikepdf.Pdf.new() as pdf:
        pdf.save(pdf_path)

    # Password-protect the PDF file
    with pikepdf.Pdf.open(pdf_path) as pdf:
        pdf.save(
            pdf_path,
            encryption=pikepdf.Encryption(
                owner=owner_password,
                user=user_password,
                R=6,
            ),
        )

    # Open the password-protected PDF file
    with pikepdf.Pdf.open(pdf_path, password=user_password) as pdf:
        assert pdf.trailer.get("/Encrypt")
