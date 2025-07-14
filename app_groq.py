import streamlit as st
from loader import load_pdf
from chunker import split_text
from embedder import get_embedder
from vectordb import build_vector_store
from llm_groq import load_llm
from qa_chain import build_qa_chain

st.set_page_config(page_title="RAG Chatbot (Groq)", layout="wide")
st.title("RAG Chatbot (Groq)")

uploaded = st.file_uploader("Upload a PDF", type="pdf")

if "history" not in st.session_state:
    st.session_state.history = []

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if uploaded:
    with st.spinner("Loading PDF..."):
        docs = load_pdf(uploaded)
    st.success("PDF loaded successfully.")

    with st.spinner("Chunking document..."):
        chunks = split_text(docs)
        st.session_state.chunks = chunks
    st.success(f"{len(chunks)} chunks created from the document.")

    if st.checkbox("View chunked text"):
        for i, chunk in enumerate(st.session_state.chunks):
            st.markdown(f"**Chunk {i+1}:**\n\n{chunk.page_content}")

    with st.spinner("Embedding and storing in vector DB..."):
        embedder = get_embedder()
        vectordb = build_vector_store(st.session_state.chunks, embedder)
    st.success("Chunks have been embedded and stored in the vector database.")

    with st.spinner("Loading Groq LLM..."):
        try:
            llm = load_llm()
            retriever = vectordb.as_retriever()
            st.session_state.qa_chain = build_qa_chain(llm, retriever)
            st.success("Groq QA Chain ready.")
        except Exception as e:
            st.error(f"Failed to load Groq LLM: {e}")
            st.stop()

# Chat UI
if st.session_state.qa_chain:
    st.subheader("Chat with your PDF")

    for role, content in st.session_state.history:
        with st.chat_message(role):
            st.markdown(content)

    query = st.chat_input("Ask a question from the PDF:")

    if query:
        st.session_state.history.append(("user", query))
        with st.chat_message("user"):
            st.markdown(query)

        with st.spinner("Thinking..."):
            try:
                response = st.session_state.qa_chain.run(query)
            except Exception as e:
                response = f"Error during response generation: {e}"

        st.session_state.history.append(("assistant", response))
        with st.chat_message("assistant"):
            st.markdown(response)


