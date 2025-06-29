from typing import Optional
from pydantic import BaseModel

class PRRequest(BaseModel):
    repo_url: str
    pr_number: int
    github_token: Optional[str] = None 