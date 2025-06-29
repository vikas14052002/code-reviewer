from app.git_util import fetch_pr_diff
from app.agent import review_code_with_agent
from app.db import save_result
from app.celery_worker import celery_app

@celery_app.task(bind=True)
def analyze_pr_task(self, data):
    print(f"Starting task for PR: {data.get('repo_url')} #{data.get('pr_number')}")

    try:
        print("Fetching PR diff...")
        diff = fetch_pr_diff(data["repo_url"], data["pr_number"], data.get("github_token"))

        print("Calling LLM to review code...")
        result = review_code_with_agent(diff)

        print("Saving result to DB...")
        save_result(self.request.id, result)

        print("Task finished successfully.")
        return result

    except Exception as e:
        print("Something went wrong:", e)
        return {"error": str(e)}
