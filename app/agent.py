import ollama
import json

def review_code_with_agent(diff_data):
    files = []
    total_issues = 0
    critical_issues = 0

    for file in diff_data:
        prompt = f"""
Analyze the code and diff. If you find any issues, give output in JSON with. Follow the following format:
- type (style, bug, perf, best_practice)
- line
- description
- suggestion

Filename: {file['name']}
Diff: {file['diff']}
Content: {file['content']}
"""

        response = ollama.chat(model="codellama", messages=[{"role": "user", "content": prompt}])
        try:
            issues = json.loads(response["message"]["content"])
        except:
            issues = []

        files.append({"name": file["name"], "issues": issues})
        total_issues += len(issues)
        critical_issues += sum(1 for i in issues if i["type"] == "bug")

    return {
        "files": files,
        "summary": {
            "total_files": len(files),
            "total_issues": total_issues,
            "critical_issues": critical_issues
        }
    }
