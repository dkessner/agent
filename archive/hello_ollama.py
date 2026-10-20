#!/usr/bin/env python
#
# hello_ollama.py
#


import asyncio

from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider



model_name = "qwen3-coder:30b"

system_prompt="""
You are a snarky assistant. You always lead with a playful insult. But you
always give useful information.
"""

# instantiating Agent by name requires environment variable
#   export OLLAMA_BASE_URL=http://localhost:11434/v1

agent = Agent(f"ollama:{model_name}",
              system_prompt=system_prompt)

# or instantiate with an explicit OllamaModel object

#ollama_model = OllamaModel(
#    model_name=model_name,
#    provider=OllamaProvider(base_url='http://localhost:11434/v1'),
#)

#agent = Agent(
#    model=ollama_model,
#    system_prompt=system_prompt
#)


async def main():

    print(f"{model_name = }")

    print("Calling agent.run()")
    response = await agent.run("What is Python?")
    print(response.output)


if __name__ == '__main__':
    asyncio.run(main())

