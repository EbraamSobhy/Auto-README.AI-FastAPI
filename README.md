# Auto-README & VitePress Documentation Generator

This backend project provides two main services:
1.  **Auto-README**: Automatically generates a professional `README.md` for a given repository URL using a local LLM (Ollama).
2.  **VitePress Generator**: Scaffolds and launches a VitePress documentation site based on a repository's `README.md`.

## Prerequisites

*   **Python 3.12+**
*   **Node.js & npm** (Required for VitePress generation)
*   **Git**
*   **Ollama** running locally (Required for Auto-README generation)
    *   Ensure Ollama is serving on `http://localhost:11434`.
    *   The system will automatically attempt to pull `llama3.1:8b` if not present.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone [<your-repo-url>](https://github.com/EbraamSobhy/Auto-README.AI-FastAPI.git)
    cd Auto-README.AI-FastAPI
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Python dependencies**:
    ```bash
    pip install fastapi uvicorn requests python-dotenv gitpython
    ```

---

## 1. Auto-README Service (`app.py`)

This service analyzes a remote Git repository (file structure and content) and uses a local LLM to generate a comprehensive `README.md`.

### Start the Server
```bash
uvicorn app:app --reload --port 8000
```

### Usage

**Generate a README:**
Send a POST request to `/generate-readme` with the repository URL.

```bash
curl -X POST http://localhost:8000/generate-readme \
     -H "Content-Type: application/json" \
     -d '{"repo_url": "https://github.com/username/repo"}'
```

**Notes:**
*   The first request might be slow if the system needs to download the LLM model (~4.7GB).
*   Check the terminal output for download progress.

---

## 2. VitePress Generator Service (`vitpress.py`)

This service clones a repository, reads its README, scaffolds a VitePress project, and starts the VitePress development server.

### Start the Server
```bash
uvicorn vitpress:app --reload --port 8001
```
*(Note: Use a different port if running alongside `app.py`, e.g., 8001)*

### Usage

**Generate and Serve Documentation:**
Send a POST request to `/generate-vitepress`.

```bash
curl -X POST http://localhost:8001/generate-vitepress \
     -H "Content-Type: application/json" \
     -d '{"repo_url": "https://github.com/username/repo"}'
```

**What happens:**
1.  The repo is cloned to a temporary directory.
2.  The `README.md` is extracted.
3.  A VitePress project is created in `vitepress_documentation`.
4.  Dependencies are installed (`npm install`).
5.  The docs are served (`npm run docs:dev`).

### Directory Structure

*   `app.py`: Main logic for LLM-based README generation.
*   `vitpress.py`: Logic for VitePress scaffolding and serving.
*   `vitepress_documentation/`: Output directory for the generated docs site.
