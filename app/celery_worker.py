from celery import Celery
from app.config import REDIS_URL

celery_app = Celery(
    "worker",
    broker=REDIS_URL,
    backend=REDIS_URL 
)

celery_app.autodiscover_tasks(["app"])
