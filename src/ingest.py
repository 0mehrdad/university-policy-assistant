# src/ingest.py

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()
# Paths
PDF_DIR = "policies"
DB_DIR = "../db"

def load_pdfs(pdf_dir):
    """Load all PDFs from the folder into LangChain docs with metadata."""
    docs = []
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            path = os.path.join(pdf_dir, file)
            print(f"Loading {path} ...")
            loader = PyPDFLoader(path)
            pages = loader.load()
            # add metadata (source + page)
            for i, page in enumerate(pages):
                page.metadata["source"] = file
                page.metadata["page"] = i + 1
            docs.extend(pages)
    return docs

def split_docs(docs, chunk_size=1000, chunk_overlap=200):
    """Split documents into smaller chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(docs)

def create_vector_db(docs, db_dir):
    """Embed documents and save FAISS vector database."""
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(db_dir)
    print(f"✅ Vector DB saved to {db_dir}")

if __name__ == "__main__":
    docs = load_pdfs(PDF_DIR)
    print(f"Loaded {len(docs)} documents")
    
    chunks = split_docs(docs)
    print(f"Split into {len(chunks)} chunks")
    
    create_vector_db(chunks, DB_DIR)
