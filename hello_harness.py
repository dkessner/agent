#!/usr/bin/env python
#
# hello_harness.py
#


import asyncio

from pydantic_ai import Agent
from pydantic_ai_harness.coder import Coder


# logging 

from pydantic_ai.capabilities import Instrumentation
from pydantic_ai.models.instrumented import InstrumentationSettings

import logfire
logfire.configure(send_to_logfire=False, console=logfire.ConsoleOptions(verbose=True))
logfire.instrument_pydantic_ai()

import json
from pydantic_core import to_jsonable_python


model_name = "ollama:qwen3-coder:30b"
#model_name = "github-copilot:claude-haiku-4.5"
#model_name = "github-copilot:claude-opus-5"
#model_name = "github-copilot:gpt-5.4"
print(f"{model_name = }")


async def main():

    agent = Agent(
        model=model_name,
        name='coder',
        capabilities=[Coder('.'),
                      Instrumentation(settings=
                          InstrumentationSettings(include_content=True)),
                     ]
    )

    print("Calling agent.run()")
    #response = await agent.run("Tell me what the hello_harness.py program does.")
    response = await agent.run("Please fix Hello.java so that it compiles and runs.")

    with open("response.output", "w") as f:
        print(response.output, file=f)

    with open("log.json", "w") as f:
        json.dump(to_jsonable_python(response.all_messages()), f, indent=2)



if __name__ == '__main__':
    asyncio.run(main())
