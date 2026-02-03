from app.V1.tools import get_tools, handle_tool_call


async def handle_list_tools(_: dict) -> dict:
    return {
        "tools": get_tools()
    }


async def handle_call_tool(request: dict) -> dict:
    tool_name = request.get("params", {}).get("name")
    tool_input = request.get("params", {}).get("arguments", {})
    
    try:
        result = handle_tool_call(tool_name, tool_input)
        return {
            "content": [
                {
                    "type": "text",
                    "text": str(result)
                }
            ]
        }
    except (ValueError, KeyError, AttributeError) as e:
        return {
            "content": [
                {
                    "type": "text",
                    "text": f"Error: {str(e)}"
                }
            ],
            "isError": True
        }