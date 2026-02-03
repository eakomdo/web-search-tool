#!/usr/bin/env python3
"""Test script for MCP web search server with Tavily"""
import json
import subprocess
import sys

def test_mcp_server():
    """Send test messages to the MCP server"""
    
    # Start the server process
    server = subprocess.Popen(
        ["python3", "-m", "app.services.main"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd="/home/emma/Desktop/mcp"
    )
    
    tests = [
        {
            "name": "Initialize Server",
            "method": "initialize"
        },
        {
            "name": "List Available Tools",
            "method": "tools/list"
        },
        {
            "name": "Search Web (Python)",
            "method": "tools/call",
            "params": {
                "name": "web_search",
                "arguments": {"query": "4th-IR", "count": 3}
            }
        },
        {
            "name": "Search Web (MCP)",
            "method": "tools/call",
            "params": {
                "name": "web_search",
                "arguments": {"query": "Who IS JOSEPH Agyere", "count": 2}
            }
        }
    ]
    
    print("\n" + "=" * 70)
    print("MCP WEB SEARCH SERVER TEST - TAVILY API")
    print("=" * 70 + "\n")
    
    for i, test in enumerate(tests, 1):
        test_name = test.pop("name")
        print(f"[Test {i}] {test_name}")
        print("-" * 70)
        
        try:
            # Build the message
            if "params" in test:
                message = {
                    "method": test["method"],
                    "params": test["params"]
                }
            else:
                message = {"method": test["method"]}
            
            print(f"Request: {json.dumps(message, indent=2)}")
            print()
            
            # Send message to server
            server.stdin.write(json.dumps(message) + "\n")
            server.stdin.flush()
            
            # Read response
            response_line = server.stdout.readline()
            
            if response_line:
                response = json.loads(response_line)
                print(f"Response:")
                print(json.dumps(response, indent=2))
            else:
                print("✗ No response from server")
                stderr_output = server.stderr.read()
                if stderr_output:
                    print(f"Error: {stderr_output}")
                    
        except json.JSONDecodeError as e:
            print(f"✗ JSON decode error: {e}")
        except Exception as e:
            print(f"✗ Error: {e}")
        
        print()
    
    # Terminate server
    server.terminate()
    try:
        server.wait(timeout=2)
    except subprocess.TimeoutExpired:
        server.kill()
    
    print("=" * 70)
    print("✓ Tests complete!")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    test_mcp_server()
