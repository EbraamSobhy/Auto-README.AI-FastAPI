from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import shutil
import git
import json
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RepoRequest(BaseModel):
    repo_url: str

OUTPUT_DIR = "vitepress_documentation"

def setup_vitepress(repo_name: str, readme_content: str, output_path: str):
    """
    Scaffolds a basic VitePress project.
    """
    docs_dir = os.path.join(output_path, "docs")
    vitepress_config_dir = os.path.join(docs_dir, ".vitepress")
    
    os.makedirs(vitepress_config_dir, exist_ok=True)
    
    # 1. Write package.json
    package_json = {
        "name": f"{repo_name}-docs",
        "version": "1.0.0",
        "scripts": {
            "docs:dev": "vitepress dev docs",
            "docs:build": "vitepress build docs",
            "docs:preview": "vitepress preview docs"
        },
        "devDependencies": {
            "vitepress": "^1.0.0"
        }
    }
    
    with open(os.path.join(output_path, "package.json"), "w") as f:
        json.dump(package_json, f, indent=2)
    
    frontmatter = "---\nlayout: doc\n---\n\n"
    
    with open(os.path.join(docs_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write(frontmatter + readme_content)
        
    # 3. Write docs/.vitepress/config.mts
    config_content = f"""import {{ defineConfig }} from 'vitepress'

export default defineConfig({{
  title: "{repo_name}",
  description: "Documentation for {repo_name}",
  themeConfig: {{
    nav: [
      {{ text: 'Home', link: '/' }}
    ],
    sidebar: [
      {{
        text: 'Guide',
        items: [
          {{ text: 'Introduction', link: '/' }}
        ]
      }}
    ],
    socialLinks: [
    ]
  }}
}})
"""
    with open(os.path.join(vitepress_config_dir, "config.mts"), "w") as f:
        f.write(config_content)


@app.post("/generate-vitepress")
def generate_vitepress(data: RepoRequest):
    temp_repo = "repo-vitepress"
    
    # Cleanup previous runs
    if os.path.exists(temp_repo):
        shutil.rmtree(temp_repo)
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
        
    try:
        # Clone
        print(f"Cloning {data.repo_url}...")
        git.Repo.clone_from(data.repo_url, temp_repo)
        
        # Find README
        readme_content = "# No README found"
        repo_name = data.repo_url.split("/")[-1].replace(".git", "")
        
        # Search for README (case insensitive)
        for file in os.listdir(temp_repo):
            if file.lower().startswith("readme"):
                with open(os.path.join(temp_repo, file), "r", encoding="utf-8") as f:
                    readme_content = f.read()
                break
        
        # Create VitePress Structure
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        setup_vitepress(repo_name, readme_content, OUTPUT_DIR)

        subprocess.run(
            "npm install && npm run docs:dev",
            cwd=OUTPUT_DIR,
            shell=True,
            check=True
        )
        
        return {
            "status": "success",
            "message": "VitePress documentation generated successfully.",
            "output_directory": os.path.abspath(OUTPUT_DIR),
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Cleanup temp repo but keep output
        if os.path.exists(temp_repo):
            shutil.rmtree(temp_repo)