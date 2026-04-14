import os
import base64
from PIL import Image
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def gera_imagem(descricao_img):
    result = client.images.generate(
        model="gpt-image-1", prompt=descricao_img, size="512x512"
    )

    image_base64 = result.data[0].b64_json

    with open("img.png", "wb") as f:
        f.write(base64.b64decode(image_base64))

    return Image.open("img.png")


st.title("Geração de Imagens com IA")

descricao_img = st.text_input("Descrição da Imagem")

if st.button("Gerar Imagem"):
    img = gera_imagem(descricao_img)
    st.image(img)
