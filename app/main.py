"""Parte 2 - Questão 1: chatbot simples com LangChain + Fake LLM exposto via FastAPI."""
from fastapi import FastAPI, HTTPException

from app.chatbot import build_chain
from app.schemas import ChatRequest, ChatResponse

app = FastAPI(
    title="Chatbot com Fake LLM (LangChain)",
    description="Protótipo de chatbot que usa um LLM simulado para testes rápidos.",
    version="1.0.0",
)

chain = build_chain()


@app.get("/", tags=["health"])
def health():
    return {"status": "ok", "llm": "FakeListLLM"}


@app.post("/chat", response_model=ChatResponse, tags=["chat"])
def chat(payload: ChatRequest):
    try:
        reply = chain.invoke({"message": payload.message})
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"Erro no chatbot: {exc}") from exc
    return ChatResponse(message=payload.message, reply=reply)
