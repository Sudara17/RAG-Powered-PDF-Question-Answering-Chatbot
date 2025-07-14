from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_core.documents import Document
import nltk

nltk.download("punkt")
from nltk.tokenize import sent_tokenize

def split_text(documents, chunk_size=700, chunk_overlap=100):
    """
    Improved adaptive text chunking for RAG pipeline.
    Uses sentence, recursive, or fixed chunking based on total word count.
    """

    all_chunks = []
    total_text = " ".join([doc.page_content for doc in documents])
    total_words = len(total_text.split())

    # Determine strategy
    if total_words < 300:
        method = "sentence"
    elif total_words < 2000:
        method = "recursive"
    else:
        method = "fixed"

    print(f"[Chunking Method]: {method}, Total Words: {total_words}")

    # Sentence-level chunking
    if method == "sentence":
        for doc in documents:
            sentences = sent_tokenize(doc.page_content)
            for sentence in sentences:
                if sentence.strip():
                    all_chunks.append(Document(page_content=sentence.strip()))

    # Character-based chunking
    else:
        if method == "fixed":
            splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        else:
            splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

        for doc in documents:
            chunks = splitter.split_text(doc.page_content)
            for chunk in chunks:
                all_chunks.append(Document(page_content=chunk.strip()))

    print(f"[Total Chunks Created]: {len(all_chunks)}")
    return all_chunks
