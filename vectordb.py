from langchain.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore
from langchain.embeddings.base import Embeddings
from langchain.vectorstores.base import VectorStoreRetriever
from langchain.vectorstores.faiss import FAISS as FAISS_DB

def build_vector_store(chunks, embedder: Embeddings):
    # Create FAISS vector store from the chunks
    vectorstore = FAISS_DB.from_documents(chunks, embedder)
    return vectorstore

def get_retriever(vectorstore, k=5) -> VectorStoreRetriever:
    # Return a retriever limited to top-k results
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return retriever
