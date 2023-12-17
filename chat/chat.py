import os
from dotenv import load_dotenv

from dataclasses import dataclass
from typing import Optional
from openai import OpenAI


@dataclass()
class Chat:
    openai_client: OpenAI

    def complete(self, prompt: str) -> Optional[str]:
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo-0613",
                messages=[{"role": "user", "content": prompt}],
            )

            return response.choices[0].message.content
        except Exception as e:
            raise e


def build_chat() -> Chat:
    load_dotenv()

    openai_key = os.getenv("OPENAI_API_KEY")
    openai_client = OpenAI(api_key=openai_key)

    return Chat(openai_client=openai_client)
