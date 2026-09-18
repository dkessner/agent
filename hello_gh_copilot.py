#!/usr/bin/env python
#
# hello_gh_copilot.py
#


import asyncio
from pydantic_ai import Agent


model_name = "github-copilot:claude-haiku-4.5"

system_prompt="""
You are a snarky assistant. You always lead with a playful insult. But you
always give useful information.
"""

# export GITHUB_COPILOT_API_KEY="gho_blahblah"

agent = Agent(model_name,
              system_prompt=system_prompt)


async def main():

    print(f"{model_name = }")

    print("Calling agent.run()")
    response = await agent.run("What is Python?")
    print(response.output)


if __name__ == '__main__':
    asyncio.run(main())


