An intelligent chatbot that allows users to upload any PDF document (e.g., medical forms, academic reports, project papers) and ask natural language questions about its content. Built using Retrieval-Augmented Generation (RAG) with Groq LLM, LangChain, and FAISS.

 Features

1) Upload any PDF file and extract clean text

2) Adaptive text chunking based on document size

3) Semantic embedding with HuggingFace transformers

4) Vector similarity retrieval using FAISS

5) Instant question-answering via Groq-hosted LLaMA3-8B-8192

6) Chat UI with conversation history using Streamlit


Tech Stack

Component	         Tool / Library
UI	             Streamlit
PDF Parsing      PyMuPDF
Chunking	     LangChain RecursiveCharacterTextSplitter + NLTK
Embeddings	     sentence-transformers/all-MiniLM-L6-v2
Vector DB	     FAISS
Retriever	     LangChain Similarity Search Retriever
LLM	             Groq API (LLaMA3-8B-8192)
Prompting	     LangChain PromptTemplate


📂 Project Structure
├── loader.py
├── chunker.py
├── embedder.py
├── vectordb.py
├── llm_groq.py
├── qa_chain.py
└── app_groq.py


How It Works

1) PDF Upload
Users upload a document via Streamlit.

2) Parsing & Chunking
The document is parsed and adaptively split into manageable chunks using NLTK or LangChain splitters.

3) Embedding & Indexing
Each chunk is transformed into an embedding and indexed using FAISS.

4) Querying
The user enters a question. The app retrieves the top-k relevant chunks and sends them + question to the LLM.

5) Answer Generation
Groq's LLaMA3 model generates an accurate, concise answer.


Installation & Run Locally

```bash
git clone https://github.com/your-username/rag-pdf-chatbot.git
cd rag-pdf-chatbot
pip install -r requirements.txt
streamlit run app_groq.py

Make sure to set your Groq API key in llm_groq.py.


🚧 Limitations
Only one PDF supported per session

No support yet for multi-document QA

Groq API key required for LLM usage


📌 Future Improvements
Support for multiple PDFs

OCR fallback for scanned PDFs

Document metadata viewer

Export Q&A sessions
