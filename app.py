from fastapi import FastAPI
from pydantic import BaseModel
import os
import shutil
import git
from dotenv import load_dotenv
import requests

app = FastAPI()
load_dotenv()


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_readme_with_ollama(prompt: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.1:8b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


SUPPORTED_EXTENSIONS = {
    # Web
    ".html", ".css", ".scss",

    # JavaScript / TypeScript
    ".js", ".ts", ".tsx", ".jsx",

    # Backend
    ".py", ".java", ".go", ".rs",
    ".cpp", ".c", ".h", ".cs", ".php",

    # Mobile
    ".kt", ".swift", ".dart",

    # Data / AI
    ".r", ".ipynb", ".sql",

    # Docs / Config
    ".md", ".yaml", ".yml", ".json", ".toml", ".tf", ".sh", ".dockerfile"

}

class RepoRequest(BaseModel):
    repo_url: str

def read_repository(repo_path):
    content = ""

    for root, _, files in os.walk(repo_path):

        if any(skip in root for skip in ["node_modules", ".git", "__pycache__", "dist", "build"]):
            continue

        for file in files:
            ext = os.path.splitext(file)[1]
            file_path = os.path.join(root, file)

            if ext in SUPPORTED_EXTENSIONS:
                try:
                    if os.path.getsize(file_path) > 50_000:
                        continue

                    with open(file_path, "r", encoding="utf-8") as f:
                        content += f"\n\n### File: {file}\n{f.read()}"

                except:
                    pass

    return content

@app.post("/generate-readme")
def generate_readme(data: RepoRequest):
    repo_path = "temp_repo"

    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)

    git.Repo.clone_from(data.repo_url, repo_path)

    repo_content = read_repository(repo_path)

    prompt = f"""
You are a senior software engineer.

Generate a PROFESSIONAL README.md file for the following repository.

Include:
- Project title
- Description
- Features
- Tech stack
- Installation
- Usage
- Folder structure
- API (if exists)
- Future improvements

Repository content:
{repo_content}
"""

    readme = generate_readme_with_ollama(prompt)

    shutil.rmtree(repo_path)

    return {"readme": readme}


# ollama pull llama3.1:8b