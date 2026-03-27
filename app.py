import streamlit as st
import requests
import os

API_URL = 'http://University-chat-bot-env-1.eba-znhr7bta.us-east-1.elasticbeanstalk.com/ask'

st.set_page_config(page_title="Policy Assistant", page_icon="📚")
st.title("📚 University Policy Assistant")

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
            try:
                r = requests.post(
                    API_URL,
                    json={"question": query},
                    timeout=10
                )

                r.raise_for_status()
                data = r.json()

                answer = data.get("answer", "No answer")
                sources = data.get("sources", [])

                source_text = "\n".join([f"- {s}" for s in sources])
                response = f"**Answer:** {answer}"

                if sources:
                    response += f"\n\n**Sources:**\n{source_text}"

            except Exception as e:
                response = "⚠️ Error: Unable to get response from server."

    st.markdown(response)
    st.session_state["messages"].append({"role": "assistant", "content": response})