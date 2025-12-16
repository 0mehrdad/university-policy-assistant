import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="University Policy Assistant", page_icon="📚")

st.title("📚 University of London Policy Assistant")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if query := st.chat_input("Ask a question..."):
    st.session_state["messages"].append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            r = requests.post(API_URL, json={"question": query})
            data = r.json()

            answer = data["answer"]
            sources = data.get("sources", [])

            source_text = "\n".join([f"- {s}" for s in sources])
            if sources:
                response = f"**Answer:** {answer}\n\n**Sources:**\n{source_text}"
            else:
                response = f"**Answer:** {answer}"

            st.markdown(response)

    st.session_state["messages"].append({"role": "assistant", "content": response})
