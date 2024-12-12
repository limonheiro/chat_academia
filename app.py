import streamlit as st
import time
import boto3
from botocore.exceptions import ClientError

# Criar o cliente Bedrock Runtime na região da AWS de uso.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

model_id = "amazon.titan-text-premier-v1:0"

# Envia a resposta do chatbot

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
        inferenceConfig={"maxTokens": 1024, "temperature": 0.5, "topP": 0.9},
    )

    # Extrair e imprimir a resposta.
    response = response["output"]["message"]["content"][0]["text"]
    
    for word in response.split():
        yield word + " "
        time.sleep(0.06)


st.image("./public/Black and Logo.webp", width=128)


# Inicializar o histórico de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir as mensagens do chat do histórico quando o app for reiniciado
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Aceitar a entrada do usuário
if prompt := st.chat_input("O que está acontecendo?"):
    # Exibir a mensagem do usuário no container de mensagens de chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Exibir a resposta do assistente no container de mensagens de chat
    with st.chat_message("assistant", avatar="./public/face.webp"):
        response = st.write_stream(response_generator())
    # Adicionar a resposta do assistente ao histórico de chat
    st.session_state.messages.append({"role": "assistant", "content": response, "avatar":"./public/face.webp"}, )

