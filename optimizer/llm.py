import ollama
from enum import Enum


class LLMs(Enum):
    DEEPSEEK_R1 = "deepseek-r1:1.5b"


def llm_chat(prompt: str, model_name: LLMs):
    response = ollama.chat(model=model_name.value, messages=[
        {
            "role": "user",
            "content": prompt,
        },
    ])
    return response.message.content


class TokenCounter:
    def __init__(self):
        self._count = 0

    def __add__(self, other):
        self._count += other
        return self

    def add(self, other):
        self._count += other

    def total_token_used(self):
        return self._count
