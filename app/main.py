from fastapi import FastAPI
from app.models import PRRequest
from app.tasks import analyze_pr_task
from celery.result import AsyncResult
from app.config import REDIS_URL
from app.celery_worker import celery_app
import redis
import json

app = FastAPI()
r = redis.Redis.from_url(REDIS_URL)

@app.post("/analyze-pr")
def analyze_pr(pr: PRRequest):
    task = analyze_pr_task.delay(pr.dict())
    return {"task_id": task.id}

@app.get("/status/{task_id}")
def get_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {"task_id": task_id, "status": result.status}

@app.get("/results/{task_id}")
def get_results(task_id: str):
    result = r.get(f"task_result:{task_id}")
    if result is not None:
        result_str = result.decode('utf-8') if isinstance(result, bytes) else str(result)
        return {"task_id": task_id, "result": json.loads(result_str)}
    return {"task_id": task_id, "result": "Results still not ready or not found"}
