#!/usr/bin/env python
#
# harness_otel_tui.py
#

import asyncio

from pydantic_ai import Agent
from pydantic_ai_harness.coder import Coder

from pydantic_ai.capabilities import Instrumentation
from pydantic_ai.models.instrumented import InstrumentationSettings

from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry import trace

# export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
# export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
# export OTEL_SERVICE_NAME=coder-agent          # shows as the service column in otel-tui

import json
from pydantic_core import to_jsonable_python


model_name = "ollama:qwen3-coder:30b"
#model_name = "github-copilot:claude-haiku-4.5"
#model_name = "github-copilot:claude-opus-5"
#model_name = "github-copilot:gpt-5.4"
print(f"{model_name = }")


async def main():

    provider = TracerProvider()
    provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))  # endpoint from env
    trace_file = open("agent_trace.jsonl", "w")
    provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter(out=trace_file)))
    trace.set_tracer_provider(provider)

    agent = Agent(
        model=model_name,
        name='coder',
        capabilities=[
            Coder('.'),
            Instrumentation(settings=InstrumentationSettings(include_content=True)),
        ],
    )

    print("Calling agent.run()")
    #response = await agent.run("Tell me what the hello_harness.py program does.")
    response = await agent.run("Please fix Hello.java so that it compiles and runs.")

    with open("response.output", "w") as f:
        print(response.output, file=f)

    with open("response.all_messages", "w") as f:
        json.dump(to_jsonable_python(response.all_messages()), f, indent=2)



if __name__ == '__main__':
    asyncio.run(main())
