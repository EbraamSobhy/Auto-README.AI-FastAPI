```bash
1. Start the Server:
   1     uvicorn vitpress:app --reload --port 8000

   2. Generate Documentation (Example):
      Open a new terminal and run:

        curl -X POST http://localhost:8000/generate-vitepress \
             -H "Content-Type: application/json" \
             -d '{"repo_url": "https://github.com/fastapi/fastapi"}'

   3. View the Documentation:
      The API will create a vitepress_dist directory. To view the site:
        cd vitepress_documentation
        npm install
        npm run docs:dev
```