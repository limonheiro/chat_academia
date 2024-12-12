import time
import boto3
from botocore.exceptions import ClientError
import streamlit as st

# Cria o cliente Bedrock Runtime na região da AWS de uso.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

model_id = "amazon.titan-text-premier-v1:0"

# Envia a resposta do chatbot
def response_generator(prompt):
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

    # Extrai e imprimi a resposta.
    response = response["output"]["message"]["content"][0]["text"]
    
    for word in response.split():
        yield word + " "
        time.sleep(0.06)
        
def local_css(fileName):
    with open(fileName) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)