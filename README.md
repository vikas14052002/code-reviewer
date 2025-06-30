## Features

- Asynchronous GitHub PR analysis using Celery
- API endpoints to trigger, track, and fetch review results
- LLM-based code review agent
- Task status and result storage using Redis
- Returns structured feedback including issues, line numbers, and suggestions



#Setup instructions:

1) Clone the repo:
```
git clone https://github.com/vikas14052002/code-reviewer.git
cd code-review-agent
```

2)Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
3) Install everything from requirements.txt file:
```
pip i -r requirements.txt
```
4) start redis(Mac OS):
```
brew install redis
brew services start redis
```
5)Start ollama after installation in your local
```
ollama run codellama
```
6)  Start FastAPI server:

```
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```
7)Finally run the celery worker, logs would be available and visible in this:
```
celery -A app.celery_worker.celery_app worker --loglevel=info
```