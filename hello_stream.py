#!/usr/bin/env python
#
# hello_ollama.py
#


import asyncio

from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider



ollama_models = [
    "gpt-oss:latest", 
    "deepseek-r1:7b-qwen-distill-q4_K_M", 
    "deepseek-coder-v2:latest", 
    "qwen2.5-coder:14b-instruct", 
    "qwen2.5:7b-instruct", 
]


model_name = ollama_models[2]


async def main():

    print(f"{model_name = }")

    ollama_model = OllamaModel(
        model_name=model_name,
        provider=OllamaProvider(base_url='http://localhost:11434/v1'),
    )

    agent = Agent(
        model=ollama_model,
        system_prompt="You are a snarky assistant. You always lead with a playful insult. But you always give useful information."
    )

    print("Calling agent.run()")

    #response = await agent.run("What is Python?")

    async with agent.run_stream('What is Python?') as run:
        async for chunk in run.stream_text(delta=True):
            print(chunk, end='', flush=True)


    #print(response.output)


if __name__ == '__main__':
    asyncio.run(main())
