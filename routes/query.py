from fastapi import APIRouter, Form
from services.vector_store import search_documents

router = APIRouter()

@router.post("/query")
async def query_knowledge(question: str = Form(...)):

    result = search_documents(question)

    return {
        "question": question,
        "answer": result
    }