# 📚 University Policy Q&A Assistant

An interactive Q&A assistant that lets you ask questions about University of London policies.  
This project combines document ingestion, vector search (FAISS), and LLMs (OpenAI) into a simple Streamlit chat app.

---

## ✨ Features
- Ingests and indexes PDF policy documents  
- Splits text into chunks for efficient semantic search  
- Stores embeddings in a FAISS vector database  
- Retrieves relevant sections and answers queries with GPT-3.5  
- Provides sources with filename + page for transparency  
- Streamlit front-end with a clean chat-like interface  
- 🚀 **Now supports Docker for easy deployment**  

---

## 📂 Project Structure

    university-policy-assistant/
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
    │── Dockerfile
    │── .dockerignore
    │── README.md
    │── .gitignore

---

## ⚙️ Setup (without Docker)

Clone the repo and install dependencies:

```bash
pip install -r requirements.txt
```

Add your API key in `.env`:

```bash
OPENAI_API_KEY=your_key_here
```

Run ingestion (creates the FAISS DB):

```bash
python src/ingest.py
```

Start the app:

```bash
streamlit run src/app.py
```

---

## 🐳 Setup with Docker

### 1. Build the image
```bash
docker build -t university-policy-assistant .
```

### 2. Run ingestion (to build the FAISS DB inside the container)
Mount your `policies/` folder and persist the `db/`:

```bash
docker run --rm \
  -v $(pwd)/policies:/app/policies \
  -v $(pwd)/db:/app/db \
  --env-file .env \
  university-policy-assistant \
  python src/ingest.py
```

### 3. Run the Streamlit app
Expose the Streamlit port (default `8501`):

```bash
docker run -it \
  -v $(pwd)/db:/app/db \
  --env-file .env \
  -p 8501:8501 \
  university-policy-assistant \
  streamlit run src/app.py --server.address=0.0.0.0
```

The app will be available at:  
👉 http://localhost:8501  

---

## 💡 Usage

Ask questions like:

- “Who is responsible for Business Continuity at the University of London?”  
- “What steps are outlined in the Harassment and Sexual Misconduct Policy?”  

The assistant will answer and cite the exact document + page.

---

## 📊 Evaluation

The retrieval component was evaluated using a manually curated dataset of 38 question–answer pairs with known source documents and page numbers.

The system retrieves the top 3 most relevant chunks (**Recall@3**) and is assessed based on whether the correct document and page appear among the retrieved results.

| Metric | Score |
|----------|----------|
| Document-Level Recall@3 | 97.37% |
| Page-Level Recall@3 | 76.32% |

This evaluation demonstrates that the system reliably retrieves the correct policy document while maintaining strong page-level retrieval performance.

---

## 🌍 Why This Project Matters
This demonstrates how organisations can make policy documents and compliance handbooks more accessible. Instead of digging through PDFs, users get direct answers with **traceable references**.
