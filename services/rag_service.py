from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_chunk_document(file_path: str):
    
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100
    )
    
    chunks = splitter.split_documents(documents)
    
    return chunks

if __name__ == "__main__":
    chunks = load_and_chunk_document("C:\\Users\\gosai\\Downloads\\Latest Resume.pdf")
    print(f"Total chunks: {len(chunks)}")
    print(chunks[0].page_content[:300])