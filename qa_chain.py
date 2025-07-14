from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def build_qa_chain(llm, retriever):
    prompt_template = """
You are a helpful assistant that extracts specific, concise answers from a medical PDF.

Only return the exact value asked for:
- Return full dates (e.g., "January 28, 1995")
- If the answer is a test name or diagnosis, return **only that term**
- Do not include headings, formatting, or multiple sentences
- If the value is not found, return "Not found."

Context:
{context}

Question: {question}
Answer:
"""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    ) 