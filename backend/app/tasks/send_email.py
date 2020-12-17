from app.core.celery_app import celery_app


@celery_app.task()
def email_task(status: str, email: str):
    return f"sended status: {status} to: {email}"
