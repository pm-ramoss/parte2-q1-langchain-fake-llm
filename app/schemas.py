from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000, examples=["Qual o horário de atendimento?"])


class ChatResponse(BaseModel):
    message: str
    reply: str
    llm: str = "FakeListLLM"
