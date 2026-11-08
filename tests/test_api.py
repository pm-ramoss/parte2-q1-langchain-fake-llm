from fastapi.testclient import TestClient

from app.chatbot import PREDEFINED_RESPONSES
from app.main import app

client = TestClient(app)


def test_chat_returns_predefined_response():
    r = client.post("/chat", json={"message": "Oi"})
    assert r.status_code == 200
    assert r.json()["reply"] in PREDEFINED_RESPONSES


def test_chat_empty_message_rejected():
    r = client.post("/chat", json={"message": ""})
    assert r.status_code == 422
