import streamlit as st
import utils as ut


ut.local_css("public/styles/style.css")

st.image('public/Black and Logo.webp', width=128)
# Inicializar o histórico de chat

if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir as mensagens do chat do histórico quando o app for reiniciado
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        

# recebe a entrada do usuário
if prompt := st.chat_input("O que está acontecendo?"):
    # Exibir a mensagem do usuário no container de mensagens de chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt, "avatar":"./public/face.webp"}, )
    
    # Exibir a resposta do assistente no container de mensagens de chat
    with st.chat_message("assistant", avatar="./public/face.webp"):
        response = st.write_stream(ut.response_generator(prompt))
    # Adicionar a resposta do assistente ao histórico de chat
    st.session_state.messages.append({"role": "assistant", "content": response, "avatar":"./public/face.webp"}, )
