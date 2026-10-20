#!/usr/bin/env python
#
# harness.py
#

import asyncio

from pydantic_ai import Agent
from pydantic_ai_harness.coder import Coder

from pydantic_ai.capabilities import Instrumentation
from pydantic_ai.models.instrumented import InstrumentationSettings

import json
from pydantic_core import to_jsonable_python


import telemetry


model_name = "ollama:qwen3-coder:30b"
#model_name = "github-copilot:claude-haiku-4.5"
#model_name = "github-copilot:claude-opus-5"
#model_name = "github-copilot:gpt-5.4"
print(f"{model_name = }")



async def main():

    telemetry.initialize_global_tracer_provider()

    try:
        agent = Agent(
            model=model_name,
            name='coder',
            capabilities=[
                Coder('.'),
                # Instrumentation: sends info to opentelemetry
                # global tracer provider
                Instrumentation(settings=
                    InstrumentationSettings(include_content=True)),
            ],
        )

        print("Calling agent.run()")
        #response = await agent.run("Tell me what the hello_harness.py program does.")
        response = await agent.run("Please fix Hello.java so that it compiles and runs.")

        with open("response.output", "w") as f:
            print(response.output, file=f)

        with open("response.all_messages", "w") as f:
            json.dump(to_jsonable_python(response.all_messages()), f, indent=2)

    except Exception as e:
        print(f"Exception caught:\n{e}")


if __name__ == '__main__':
    asyncio.run(main())
