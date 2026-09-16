# import streamlit as st
# from ollama import chat

# st.title("Chat with Llama 3 (via Ollama)")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# Display chat history
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.write(msg["content"])

# ONE chat_input only
# prompt = st.chat_input(
#     "Your message",
#     key="main_chat"
# )

# if prompt:

#     st.session_state.messages.append(
#         {
#             "role": "user",
#             "content": prompt
#         }
#     )

#     with st.chat_message("user"):
#         st.write(prompt)

#     try:

#         with st.spinner("Thinking..."):

#             response = chat(
#                 model="llama3.2:latest",
#                 messages=st.session_state.messages
#             )

#             assistant_msg = response.message.content

#             st.session_state.messages.append(
#                 {
#                     "role": "assistant",
#                     "content": assistant_msg
#                 }
#             )

#             with st.chat_message("assistant"):
#                 st.write(assistant_msg)

#     except Exception as e:
#         st.error(f"Error: {e}")

import streamlit as st
from ollama import chat
from datetime import datetime

# --------------------
# Page Configuration
# --------------------
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# --------------------
# Sidebar
# --------------------
with st.sidebar:
  

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# --------------------
# Main Header
# --------------------
st.title("🤖 AI Assistant")
st.caption("Ask me")

# --------------------
# Chat History
# --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --------------------
# User Input
# --------------------
prompt = st.chat_input(
    "Ask me anything...",
    key="chat_box"
)

if prompt:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:

        # Current date/time awareness
        system_message = {
            "role": "system",
            "content": f"""
You are a professional AI assistant.

Today's date is:
{datetime.now().strftime('%d %B %Y')}

Current time:
{datetime.now().strftime('%I:%M %p')}

Answer clearly and professionally.
"""
        }

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = chat(
                    model="llama3.2:latest",
                    messages=[
                        system_message
                    ] + st.session_state.messages
                )

                answer = response.message.content

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:
        st.error(f"Error: {str(e)}")