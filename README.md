An intelligent chatbot that allows users to upload any PDF document (e.g., medical forms, academic reports, project papers) and ask natural language questions about its content. Built using Retrieval-Augmented Generation (RAG) with Groq LLM, LangChain, and FAISS.

 Features
 Upload any PDF file and extract clean text

 Adaptive text chunking based on document size

 Semantic embedding with HuggingFace transformers

 Vector similarity retrieval using FAISS

 Instant question-answering via Groq-hosted LLaMA3-8B-8192

 Chat UI with conversation history using Streamlit

Tech Stack
Component	Tool / Library
UI	Streamlit
PDF Parsing	PyMuPDF
Chunking	LangChain RecursiveCharacterTextSplitter + NLTK
Embeddings	sentence-transformers/all-MiniLM-L6-v2
Vector DB	FAISS
Retriever	LangChain Similarity Search Retriever
LLM	Groq API (LLaMA3-8B-8192)
Prompting	LangChain PromptTemplate

Project Architecture
graphql
Copy
Edit
📂 app/
├── loader.py         # PDF loader using PyMuPDF
├── chunker.py        # Adaptive text chunking (sentence/recursive/fixed)
├── embedder.py       # HuggingFace embeddings loader
├── vectordb.py       # FAISS vector store builder and retriever
├── llm_groq.py       # Loads Groq-hosted LLaMA3 model
├── qa_chain.py       # LangChain QA chain with custom prompt
└── app_groq.py       # Streamlit interface

🔄 How It Works
PDF Upload
Users upload a document via Streamlit.

Parsing & Chunking
The document is parsed and adaptively split into manageable chunks using NLTK or LangChain splitters.

Embedding & Indexing
Each chunk is transformed into an embedding and indexed using FAISS.

Querying
The user enters a question. The app retrieves the top-k relevant chunks and sends them + question to the LLM.

Answer Generation
Groq's LLaMA3 model generates an accurate, concise answer.

📥 Installation & Run Locally
bash
Copy
Edit
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