from fastapi import APIRouter, UploadFile, File
import os 
from services.rag_service import load_and_chunk_document
from services.vector_store import create_vector_store

router = APIRouter()

UPLOAD_FOLDER = "documents"

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    
    with open(file_path, "wb") as f:
        f.write(await file.read())
        
    chunks = load_and_chunk_document(file_path)
    create_vector_store(chunks)
    
    return {"message":"File uploaded and processed successfully", "filename":file.filename, "chunks":len(chunks)}
