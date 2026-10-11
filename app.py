from fastapi import FastAPI

app = FastAPI(title="RAG Lab API")

@app.get("/")
def home():
    return {"message": "Hello from RAG Lab API"}

@app.get("/health")
def health():
    return {"status": "ok"}
