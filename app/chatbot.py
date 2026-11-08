"""Cadeia LangChain com Fake LLM: respostas pré-definidas, sem rede e sem custo."""
from langchain_core.language_models.fake import FakeListLLM
from langchain_core.prompts import PromptTemplate

# Respostas pré-definidas; o FakeListLLM as devolve em ordem circular.
PREDEFINED_RESPONSES = [
    "Olá! Sou um chatbot de demonstração. Como posso ajudar?",
    "Nosso horário de atendimento é de segunda a sexta, das 9h às 18h.",
    "Posso encaminhar você para um atendente humano, se preferir.",
    "Obrigado pelo contato! Tenha um ótimo dia.",
]

PROMPT = PromptTemplate.from_template(
    "Você é um assistente de atendimento cordial.\nUsuário: {message}\nAssistente:"
)


def build_chain():
    llm = FakeListLLM(responses=PREDEFINED_RESPONSES)
    return PROMPT | llm  # LCEL: prompt -> LLM
