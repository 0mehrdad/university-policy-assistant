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

``` university-policy-assistant/
│── policies/                # 29 PDFs
│
│── notebooks/               # testing & experiments
│   ├── 01_ingest_test.ipynb
│
│── src/                     # production code
│   ├── ingest.py
│   ├── qa.py
│   ├── app.py
│
│── db/                      # persisted FAISS index (generated after ingest)
│
│── requirements.txt
│── README.md
│── .gitignore 
```
Setup

Clone the repo and install dependencies:

pip install -r requirements.txt


Add your API key in .env:

OPENAI_API_KEY=your_key_here



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
