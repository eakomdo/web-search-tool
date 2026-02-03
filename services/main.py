import json
import sys
import asyncio
from app.handlers import handle_list_tools, handle_call_tool


def handle_message(message: dict) -> dict:
    method = message.get("method")
    
    if method == "initialize":
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "serverInfo": {
                "name": "web-search",
                "version": "1.0.0"
            }
        }
    elif method == "tools/list":
        return asyncio.run(handle_list_tools(message))
    elif method == "tools/call":
        return asyncio.run(handle_call_tool(message))
    else:
        return {"error": f"Unknown method: {method}"}


def main():
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            
            message = json.loads(line)
            response = handle_message(message)
            print(json.dumps(response))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
