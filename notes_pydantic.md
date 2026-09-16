# Notes on pydantic-ai

Official docs:  
- [https://pydantic.dev/docs/ai/overview/](https://pydantic.dev/docs/ai/overview/)

GitHub repositories:
- [https://github.com/pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)
- [https://github.com/pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness)

Articles:
- [(pydantic.dev) Pydantic AI v2](https://pydantic.dev/articles/pydantic-ai-v2)
- [(pydantic.dev) Pydantic Monty secure interpreter](https://pydantic.dev/articles/pydantic-monty)

## pydantic-ai-harness


`pydantic-ai-harness` is an agent and harness library, making available high-level abstractions
for communicating with LLMs.  Models can be hosted or served locally (e.g. ollama).

One fundamental abstraction is the `Capability`, which is a reusable and
composable collection of tools, instructions and model settings.

There are dozens of 
[capabilities](https://pydantic.dev/docs/ai/capabilities/overview/)
provided by the library, including a full [`Coder` harness](https://pydantic.dev/docs/ai/harness/coder/).

`hello_harness.py` demonstrates the use of `Coder` with the `qwen3-coder:30b`
model served locally via `ollama`.


## first notes

Agent
    system_prompt -> added to message history
    instructions not part of message history

toolsets

built in tools
    - web search
        from pydantic_ai import WebSearchTool
    - code execution
        from pydantic_ai import CodeExecutionTool

embedding models
    from pydantic_ai import Embedder
    embedder.embed_query("I love Python")

MCP servers
    from pydantic_ai import Agent
    from pydantic_ai.mcp import MCPServerStreamableHTTP
    server = HCPServerStreamableHTTP('http://localhost:8000/mcp')
    agent = Agent('', toolsets = [server])

