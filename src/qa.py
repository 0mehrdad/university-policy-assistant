import sys
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

def main(query):

    # Load FAISS index
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.load_local(
        "../db", 
        embeddings, 
        allow_dangerous_deserialization=True
    )
    # Set up LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


    qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectordb.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True
        )
    result = qa_chain({"query": query})

    
    answer = result["result"]
    sources = []
    for doc in result["source_documents"]:
        source = doc.metadata.get("source", "Unknown file")
        page = doc.metadata.get("page", "?")
        sources.append(f"{source}, page {page}")
    return answer, sources

if __name__ == "__main__":
    main()
