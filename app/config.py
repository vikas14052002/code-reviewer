# app/config.py

import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
