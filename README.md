## Features

- Asynchronous GitHub PR analysis using Celery
- API endpoints to trigger, track, and fetch review results
- LLM-based code review agent
- Task status and result storage using Redis
- Returns structured feedback including issues, line numbers, and suggestions



#Setup instructions:

1) git clone https://github.com/vikas14052002/code-reviewer.git
cd code-review-agent


2)Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate