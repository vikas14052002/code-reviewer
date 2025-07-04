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

8)Finally theser are api -endpoints:
-Analyze PR:
```
curl --location 'http://localhost:8000/analyze-pr' \
--header 'Content-Type: application/json' \
--data '{
  "repo_url": "https://github.com/scikit-fuzzy/scikit-fuzzy",
  "pr_number": 63
}
'
```
Expected output:
```
{
    "task_id": "a4039727-0bf9-49b9-af2a-f4a58265f0cb"
}
```

-Status endpoint:

```
curl --location 'http://localhost:8000/status/a4039727-0bf9-49b9-af2a-f4a58265f0cb'
```

Expected output:
```
{
    "task_id": "a4039727-0bf9-49b9-af2a-f4a58265f0cb",
    "status": "SUCCESS"
}
```

-Results endpoint:

```
curl --location 'http://localhost:8000/results/a4039727-0bf9-49b9-af2a-f4a58265f0cb'
```

Expected output:

```
{
    "task_id": "a4039727-0bf9-49b9-af2a-f4a58265f0cb",
    "result": {
        "files": [
            {
                "name": "DEPENDS-docs.txt",
                "issues": []
            },
            {
                "name": "docs/Makefile",
                "issues": []
            },
            {
                "name": "docs/ext/plot2rst.py",
                "issues": []
            },
            {
                "name": "docs/tools/build_modref_templates.py",
                "issues": [
                    {
                        "type": "style",
                        "line": 10,
                        "description": "Line too long",
                        "suggestion": "Break line into smaller parts"
                    }
                ]
            }
        ],
        "summary": {
            "total_files": 4,
            "total_issues": 0,
            "critical_issues": 0
        }
    }
}

```

Environment Variables
Create a .env file based on the provided .env.example:
```
REDIS_URL=redis://localhost:6379/0
```

Future improvements:

The code review agent we used is completely based on our local server. So as per the new technologies, for the github intgeration, we can totally make use of the MCP(Model context protocol).

Directly configuring our MCP with the github token , and we can see various tools predefined if using nx, or 3 tols if we use our local server as of now.

- can add multimodal language support too 
-API rate limiting and auth
-Better prompt tuning and structured agent chaining
- Deployment in docker


Testing:run tests with pytest: