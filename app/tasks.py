from app.git_util import fetch_pr_diff
from app.agent import review_code_with_agent
from app.db import save_result
from app.celery_worker import celery_app

@celery_app.task(bind=True)
def analyze_pr_task(self, data):
    try:
        diff = fetch_pr_diff(data["repo_url"],
         data["pr_number"], data.get("github_token"))
        result = review_code_with_agent(diff)
        save_result(self.request.id, result)
        return result
    except Exception as e:
        return {"error": str(e)}
