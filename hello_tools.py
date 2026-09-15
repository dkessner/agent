#!/usr/bin/env python
#
# hello_tools.py
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


model_name = ollama_models[4]


def get_favorite_color(name: str) -> str:
    """Function that returns the favorite color of a user based on their name."""
    if name == "Dr. Kessner":
        return 'Orange'
    elif name == "Tux":
        return 'Black'
    else:
        return 'Beige'


ollama_model = OllamaModel(
    model_name=model_name,
    provider=OllamaProvider(base_url='http://localhost:11434/v1')
)

agent = Agent(
    model=ollama_model,
    system_prompt="You are a snarky assistant. You always lead with a playful insult. But you always give useful information.",
    tools = [get_favorite_color] # tools can be passed in the Agent constructor
)


async def main():

    print(f"{model_name = }")

    print("Calling agent.run()")
    response = await agent.run("What is the favorite color of Dr. Kessner? How about his cat Tux?  Tell me the hobby of each.") 
    print(response.output)


# tools can also be defined by decorator

@agent.tool_plain
def get_hobby(name: str) -> str:
    """Function that returns the hobby of a user based on their name."""
    if name == "Dr. Kessner":
        return 'Juggling'
    elif name == "Tux":
        return 'Boxing'
    else:
        return 'Nothing'



if __name__ == '__main__':
    asyncio.run(main())
