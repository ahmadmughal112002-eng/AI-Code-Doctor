import os
from google.adk.models.lite_llm import LiteLlm

os.environ.setdefault("OLLAMA_API_BASE", "http://localhost:11434")

MODEL = "ollama_chat/qwen2.5-coder:7b"

def get_model():
    return LiteLlm(model=MODEL)