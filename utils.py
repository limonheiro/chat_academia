import time
import boto3
from botocore.exceptions import ClientError
import streamlit as st
import os

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')

def client_config(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION):
    
    if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and AWS_DEFAULT_REGION:
        return boto3.client("bedrock-runtime",
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name=AWS_DEFAULT_REGION) 
    else:
        #iniciar com as variaveis de configurações dos arquivos credentials e config
        return boto3.client("bedrock-runtime", region_name="us-east-1")
                

# Cria o cliente Bedrock Runtime na região da AWS de uso.
client = client_config(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION)

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