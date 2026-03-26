import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "db")

# Load once at startup
embeddings = OpenAIEmbeddings()
vectordb = FAISS.load_local(
    DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectordb.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True
)

def get_answer(query: str):
    result = qa_chain({"query": query})

    answer = result["result"]
    sources = [
        f"{doc.metadata.get('source', 'Unknown')}, page {doc.metadata.get('page', '?')}"
        for doc in result["source_documents"]
    ]

    return answer, sources