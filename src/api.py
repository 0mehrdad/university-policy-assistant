import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.qa import get_answer

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="UoL Policy Assistant API")

class Query(BaseModel):
    question: str

@app.on_event("startup")
def startup_event():
    logging.info("API starting...")
    try:
        # simple test call
        get_answer("test")
        logging.info("QA system loaded successfully")
    except Exception as e:
        logging.error(f"Startup failed: {e}")
        raise e

@app.post("/ask")
def ask_api(payload: Query):
    try:
        logging.info(f"Question: {payload.question}")

        answer, sources = get_answer(payload.question)

        return {
            "answer": answer,
            "sources": sources
        }

    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/")
def root():
    return {"status": "ok"}