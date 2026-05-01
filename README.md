# AI Knowledge Assistant

An AI-powered Knowledge Assistant that uses **Retrieval-Augmented Generation (RAG)** to answer questions from custom documents with accurate, contextual, and intelligent responses.

## Features

- Upload and process custom documents
- Intelligent question answering from document content
- Context-aware responses using RAG architecture
- Fast semantic search with vector embeddings
- Clean and interactive web interface
- Flask-based backend integration

## Tech Stack

- Python
- Flask
- HTML / CSS / JavaScript
- NLP
- Vector Database / Embeddings
- Generative AI Models

## Project Structure

```text
ai_knowledge_assistant/
│── app.py
│── routes/
│── services/
│── utils/
│── templates/
│── static/
│── documents/
│── db/
│── requirements.txt
=======
A FastAPI-based web application that allows users to upload PDF documents and ask questions about them using Retrieval-Augmented Generation (RAG) with local LLM inference.

## 🚀 Features

- **PDF Upload**: Upload any PDF document to the knowledge base
- **Chunking**: Automatic text extraction and chunking using LangChain
- **Vector Search**: Store document embeddings in Chroma vector database
- **Question Answering**: Ask questions about your uploaded documents
- **Local LLM**: Uses Ollama (gemma:2b) for generating answers - no external API required

## 🛠️ Technologies Used

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)**: Modern Python web framework for building APIs
  - Used for: Creating REST endpoints and routing

### Document Processing (LangChain)
- **[PyPDFLoader](https://python.langchain.com/docs/modules/data_loader/document_loaders/pdf)**: Load and extract text from PDF files
  - Used for: Reading PDF documents
- **[RecursiveCharacterTextSplitter](https://python.langchain.com/docs/modules/data_client/text_splitters)**: Split documents into overlapping chunks
  - Used for: Breaking down large documents into manageable chunks (700 chars with 100 overlap)

### Vector Database
- **[Chroma](https://docs.trychroma.com/)**: AI-native open-source vector database
  - Used for: Storing and searching document embeddings

### Embeddings
- **[HuggingFace Embeddings](https://python.langchain.com/docs/integrations/text_embedding)**: Generate text embeddings using HuggingFace models
  - Model: `sentence-transformers/all-MiniLM-L6-v2`
  - Used for: Converting text chunks into vector representations

### LLM Integration
- **[Ollama](https://ollama.ai/)**: Local LLM inference engine
  - Model: `gemma:2b`
  - Used for: Generating context-aware answers from retrieved documents

### Frontend
- **[Jinja2](https://jinja.palletsprojects.com/)**: Python template engine
  - Used for: Rendering HTML templates
- **HTML/CSS**: Basic frontend interface

## 📁 Project Structure

```
ai_knowledge_assistant/
├── app.py                 # FastAPI application entry point
├── routes/
│   ├── upload.py         # Upload endpoint
│   └── query.py          # Query endpoint
├── services/
│   ├── rag_service.py   # Document loading and chunking
│   ├── vector_store.py  # Vector database operations
│   └── llm_service.py   # LLM answer generation
├── templates/
│   └── index.html       # HTML frontend
├── static/
│   └── style.css       # CSS styling
├── utils/
│   └── file_utils.py   # Utility functions
├── documents/           # Uploaded PDFs stored here
├── db/                  # Chroma vector database
└── README.md            # This file
```

## 🔄 How It Works

### 1. Upload Document
```
User uploads PDF → Save to documents folder → Load with PyPDFLoader
→ Split into chunks using RecursiveCharacterTextSplitter
→ Create embeddings with HuggingFace
→ Store in Chroma vector database
```

### 2. Ask Question
```
User asks question → Create embeddings for the question
→ Search Chroma for similar documents (k=8)
→ Extract relevant context
→ Generate answer using Ollama (gemma:2b)
→ Return answer to user
```

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| POST | `/upload` | Upload PDF document |
| POST | `/query` | Ask a question |

## 🏃‍♂️ Getting Started

### Prerequisites
- Python 3.8+
- Ollama installed with gemma:2b model

### Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install fastapi uvicorn python-multipart jinja2
pip install langchain langchain-community langchain-text-splitters
pip install langchain-huggingface chromadb sentence-transformers
pip install requests
```

3. Start Ollama:
```bash
ollama serve
ollama pull gemma:2b
```

4. Run the application:
```bash
uvicorn app:app --reload
```

5. Open browser at `http://127.0.0.1:8000`

## 💡 Key Concepts

### Retrieval-Augmented Generation (RAG)
A technique that combines retrieval-based and generation-based AI models. The system:
1. Retrieves relevant documents from a knowledge base
2. Uses them as context for the LLM to generate accurate answers

### Chunking Strategy
- **Chunk Size**: 700 characters
- **Overlap**: 100 characters
- Ensures context is preserved across chunks

### Vector Search
- Uses semantic similarity (cosine similarity) to find relevant document chunks
- Returns top 8 most similar chunks as context

## 🎯 Use Cases

- **Personal Knowledge Base**: Upload your Resume, Notes, or Research Papers
- **Document Q&A**: Ask questions about PDF documents
- **Local AI Assistant**: Keep all data private with local LLM

---

Built with ❤️ using FastAPI, LangChain, Chroma, and Ollama

