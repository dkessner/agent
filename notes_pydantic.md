# Notes on pydantic-ai

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

