import streamlit as st
from qa import main as get_answer

st.set_page_config(page_title="University Policy Assistant", page_icon="📚")

st.title("📚 University of London Policy Assistant")
st.write("Ask me about University of London policies and documents.")

# Keep chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display past chat
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if query := st.chat_input("Ask a question..."):
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer, sources = get_answer(query)

            # Format sources
            source_text = "\n".join(
                [f"- {s}" for s in sources]
            )
            response = f"**Answer:** {answer}\n\n**Sources:**\n{source_text}"

            st.markdown(response)

    # Save bot response
    st.session_state["messages"].append({"role": "assistant", "content": response})
