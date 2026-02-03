import json
from typing import Any


def get_tools() -> list:
    """Define available MCP tools for web search."""
    return [
        {
            "name": "web_search",
            "description": "Search the web using Brave Search API",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query string"
                    },
                    "count": {
                        "type": "integer",
                        "description": "Number of results (1-20)",
                        "default": 10
                    }
                },
                "required": ["query"]
            }
        }
    ]


def handle_tool_call(tool_name: str, tool_input: dict) -> dict:
    """Handle tool calls from MCP requests."""
    from services.main import SearchService
    
    if tool_name == "web_search":
        service = SearchService()
        result = service.search(
            query=tool_input.get("query"),
            count=tool_input.get("count", 10)
        )
        return result.model_dump()
    
    raise ValueError(f"Unknown tool: {tool_name}")