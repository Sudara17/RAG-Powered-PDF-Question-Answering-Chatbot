from langchain_community.document_loaders import PyMuPDFLoader
import tempfile

def load_pdf(uploaded_file):
    # Save uploaded file to temp location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Use PyMuPDFLoader 
    loader = PyMuPDFLoader(tmp_path)
    pages = loader.load()

    # Join all pages into a single Document
    from langchain_core.documents import Document
    full_text = "\n".join([p.page_content for p in pages])
    return [Document(page_content=full_text)]



