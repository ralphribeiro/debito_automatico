import time

from app.tasks.send_email import email_task


def test_send_email_task():
    status = "accepted"
    email = "test@test.com"
    output = email_task(status, email)
    assert output == f"sended status: {status} to: {email}"
