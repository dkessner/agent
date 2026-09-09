#!/usr/bin/env python
#
# hello.py
#


import asyncio

from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider


async def main():

    ollama_model = OllamaModel(
        model_name="qwen2.5:7b-instruct",
        provider=OllamaProvider(base_url='http://localhost:11434/v1'),
    )

    agent = Agent(
        model=ollama_model,
        system_prompt="You are a helpful assistant. You always answer with a single concise sentence."
    )

    response = await agent.run("What is Python?")
    print(response.output)


if __name__ == '__main__':
    asyncio.run(main())

