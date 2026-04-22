from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from services.llm_service import generate_answer

# ✅ THIS FUNCTION (required for upload)
def create_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="db"
    )

    db.persist()


# ✅ THIS FUNCTION (required for query)
def search_documents(question):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    docs = db.max_marginal_relevance_search(question, k=8)

    context = "\n\n".join([doc.page_content for doc in docs])

    answer = generate_answer(context, question)

    return answer