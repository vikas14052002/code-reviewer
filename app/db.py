import redis
import json
from app.config import REDIS_URL

r = redis.Redis.from_url(REDIS_URL)

def save_result(task_id, result):
    r.setex(f"task_result:{task_id}", 3600, json.dumps(result))  # 1-hour expiry
