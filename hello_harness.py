#!/usr/bin/env python
#
# hello_harness.py
#


import asyncio

from pydantic_ai import Agent
from pydantic_ai_harness.coder import Coder


#model_name = "ollama:qwen3-coder:30b"
#model_name = "github-copilot:claude-haiku-4.5"
#model_name = "github-copilot:claude-opus-5"
model_name = "github-copilot:gpt-5.4"
print(f"{model_name = }")


async def main():

    agent = Agent(
        model=model_name,
        name='coder',
        capabilities=[Coder('.')],
    )

    print("Calling agent.run()")
    #response = await agent.run("Tell me what the hello_harness.py program does.")
    response = await agent.run("Please fix Hello.java so that it compiles and runs.")
    print(response.output)


if __name__ == '__main__':
    asyncio.run(main())
