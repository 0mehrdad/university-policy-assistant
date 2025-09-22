📚 University Policy Q&A Assistant

An interactive Q&A assistant that lets you ask questions about University of London policies.
This project combines document ingestion, vector search (FAISS), and LLMs (OpenAI) into a simple Streamlit chat app.

Features

Ingests and indexes PDF policy documents.

Splits text into chunks for efficient semantic search.

Stores embeddings in a FAISS vector database.

Retrieves relevant sections and answers queries with GPT-3.5.

Provides sources with filename + page for transparency.

Streamlit front-end with a clean chat-like interface.

Project Structure
├── app.py        # Streamlit chat interface  
├── ingest.py     # Load PDFs, split text, create FAISS index  
├── qa.py         # Query interface using RetrievalQA  
├── policies/     # Folder for PDFs  
├── db/           # Vector database (created after ingest)  
└── .env          # Store your OPENAI_API_KEY here  

Setup

Clone the repo and install dependencies:

pip install -r requirements.txt


Add your API key in .env:

OPENAI_API_KEY=your_key_here


Place PDF policies in policies/.

Run ingestion (creates the FAISS DB):

python ingest.py


Start the app:

streamlit run app.py

Usage

Ask questions like:

“Who is responsible for Business Continuity at the University of London?”

“What steps are outlined in the Harassment and Sexual Misconduct Policy?”

The assistant will answer and cite the exact document + page.

Why This Project Matters

This is a demonstration of how organisations can make policy documents and compliance handbooks more accessible. Instead of digging through PDFs, users can get direct answers with traceable references.
