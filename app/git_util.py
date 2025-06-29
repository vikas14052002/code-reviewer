import requests
from urllib.parse import urlparse

def fetch_pr_diff(repo_url, pr_number, token=None):
    parsed = urlparse(repo_url)
    owner, repo = parsed.path.strip("/").split("/")
    headers = {"Authorization": f"token {token}"} if token else {}
    
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    res = requests.get(url, headers=headers)
    files = res.json()

    data = []
    for file in files:
        content_url = file.get("raw_url")
        content = requests.get(content_url, headers=headers).text
        data.append({
            "name": file["filename"],
            "content": content,
            "diff": file.get("patch", "")
        })
    return data
