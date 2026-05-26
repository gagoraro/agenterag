# 🤖 Agente RAG — Atlas

Agente de recuperação e geração aumentada (RAG) desenvolvido como projeto final do curso **"Agents For Everything"**. O agente, chamado **Atlas**, responde perguntas sobre o **Oscar 2026** com base em uma base de conhecimento local, utilizando busca semântica via FAISS e geração de respostas com Gemini.

---

## 🧠 Como funciona

1. A base de conhecimento (`.txt`) é lida e dividida em chunks
2. Os chunks são transformados em embeddings via Gemini
3. A pergunta do usuário também é convertida em embedding
4. O FAISS busca os trechos mais relevantes por similaridade
5. O Gemini gera a resposta final com base no contexto recuperado

---

## 🛠️ Tecnologias

- Python
- [Gemini API](https://ai.google.dev/) — embeddings e geração de texto
- [FAISS](https://github.com/facebookresearch/faiss) — busca vetorial por similaridade
- dotenv — gerenciamento de variáveis de ambiente

---

## 📁 Estrutura

```
agenterag/
├── agenterag.py   # Código principal do agente
├── ragpuc.txt     # Base de conhecimento (Oscar 2026)
├── .env           # Variáveis de ambiente (não versionar)
└── README.md
```

---

## ⚙️ Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/gagoraro/agenterag.git
cd agenterag
```

### 2. Instale as dependências
```bash
pip install google-genai faiss-cpu numpy python-dotenv
```

### 3. Configure o `.env`
```env
api_gemini=SUA_CHAVE_AQUI
prompt_agente=SEU_PROMPT_AQUI
```

### 4. Execute
```bash
python agenterag.py
```

---

## 💬 Exemplo de uso

```
Sou Atlas, e sei tudo sobre o Oscar 2026. Como posso ajudar?
Qual a sua pergunta? Quem venceu o Oscar de Melhor Ator?

Atlas está pensando...

Atlas responde:
Michael B. Jordan venceu o Oscar de Melhor Ator pelo seu papel duplo em Pecadores (Sinners).
```
