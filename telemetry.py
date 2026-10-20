#!/usr/bin/env python
#
# telemetry.py
#


import os
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry import trace


# environment variables for OTLPSpanExporter with otel-tui
#   export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
#   export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
#   export OTEL_SERVICE_NAME=coder-agent 


def initialize_telemetry():

    provider = TracerProvider()

    # export trace to OpenTelemetry Protocol (OTLP) endpoint, e.g. otel-tui

    if os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT"):
        print("OTEL_EXPORTER_OTLP_ENDPOINT found; adding OTLPSpanExporter")
        provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))  # endpoint from env
    else:
        print("OTEL_EXPORTER_OTLP_ENDPOINT not found")

    # local trace export to file

    trace_file = open("agent_trace.jsonl", "w")
    provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter(out=trace_file)))

    # set global tracer provider

    trace.set_tracer_provider(provider) 


