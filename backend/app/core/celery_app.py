from celery import Celery

from app.core import config


celery_app = Celery("worker",
                    broker=config.CELERY_BROKER,
                    backend=config.CELERY_BACKEND,)