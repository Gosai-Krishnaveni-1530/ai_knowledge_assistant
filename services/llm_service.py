import requests

def generate_answer(context, question):

    prompt = f"""
You are an AI assistant.

Use the context below to answer the question.
If the question asks for a summary, summarize all available context clearly.

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]