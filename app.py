import streamlit as st
import time
import boto3
from botocore.exceptions import ClientError

# Criar o client Bedrock Runtime na região AWS de uso.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

model_id = "amazon.titan-text-premier-v1:0"

    
# Streamed response emulator
def response_generator():
    conversation = [
        {
            "role": "user",
            "content": [{"text": prompt}],
        }
    ]
    
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extrair e printar a resposta.
    response = response["output"]["message"]["content"][0]["text"]
    
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("Academia")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})