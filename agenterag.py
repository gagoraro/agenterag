import os
import numpy as np
import faiss
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key_gemini = os.getenv("api_gemini")
prompt = os.getenv("prompt_agente")

usuario_gemini = genai.Client(api_key=api_key_gemini)

def ler_arquivo_em_chunks(caminho_arquivo, tamanho_chunk=500):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    chunks = []
    for i in range(0, len(conteudo), tamanho_chunk):
        chunk = conteudo[i:i + tamanho_chunk]
        chunks.append(chunk.strip())
    return chunks

def gerar_embeddings(textos):
    response = usuario_gemini.models.embed_content(
        model="models/text-embedding-004",
        contents=textos
    )
    embeddings = [embedding.values for embedding in response.embeddings]
    return np.array(embeddings).astype('float32')

arquivo_pc = "/Users/jose/Documents/puc/ragpuc.txt" 

print("Sou Atlas, e sei tudo sobre o Oscar2026. Como posso ajudar?")
pergunta = input("Qual a sua pergunta? ")

chunks = ler_arquivo_em_chunks(arquivo_pc, tamanho_chunk=500)

print("Atlas está pensando...")
embeddings_chunks = gerar_embeddings(chunks)
dimensao = embeddings_chunks.shape[1]

index = faiss.IndexFlatIP(dimensao)
faiss.normalize_L2(embeddings_chunks)
index.add(embeddings_chunks)

embedding_pergunta = gerar_embeddings([pergunta])
faiss.normalize_L2(embedding_pergunta)

k = 3
distancias, indices = index.search(embedding_pergunta, k)

contexto_filtrado = ""
for rank, idx in enumerate(indices[0]):
    if idx != -1: 
        contexto_filtrado += f"[Trecho Relevante {rank+1}]:\n{chunks[idx]}\n\n"
prompt_completo = f"{prompt}\n\n{contexto_filtrado}\n\n{pergunta}"

resposta = usuario_gemini.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt_completo,
    config=types.GenerateContentConfig(temperature=0.3)
)

print("\nAtlas responde:")
print(resposta.text)
