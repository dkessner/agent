#!/usr/bin/env python
#
# hello_harness.py
#


import asyncio

from pydantic_ai import Agent
from pydantic_ai_harness.coder import Coder

from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider



model_name = "qwen3-coder:30b"
print(f"{model_name = }")

ollama_model = OllamaModel(
    model_name=model_name,
    provider=OllamaProvider(base_url='http://localhost:11434/v1'),
)


async def main():

    agent = Agent(
        model=ollama_model,
        name='coder',
        capabilities=[Coder('.')],
    )

    print("Calling agent.run()")
    #response = await agent.run("Tell me what the hello_harness.py program does.")
    response = await agent.run("Please fix Hello.java so that it compiles and runs.")
    print(response.output)


if __name__ == '__main__':
    asyncio.run(main())
