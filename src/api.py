from fastapi import FastAPI
from pydantic import BaseModel
from src.qa import main as get_answer

app = FastAPI(title="UoL Policy Assistant API")

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_api(payload: Query):
    answer, sources = get_answer(payload.question)
    return {
        "answer": answer,
        "sources": sources
    }

@app.get("/")
def root():
    return {"status": "ok"}