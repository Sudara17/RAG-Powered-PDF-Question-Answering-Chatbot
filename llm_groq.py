from langchain_groq import ChatGroq

def load_llm():
    return ChatGroq(
        model="llama3-8b-8192",
        api_key="YOUR_GROQ_API_KEY"
    )

