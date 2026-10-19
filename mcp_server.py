"""MCP Server wrapper for Markdown Mermaid Syntax Lint Healer."""
import json
import sys
from client import MarkdownMermaidSyntaxLintHealer

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "heal_mermaid_syntax",
                    "description": "Audit and automatically heal common Mermaid diagram syntax errors from LLMs",
                    "inputSchema": {
                        "type": "object",
                        "properties": {"mermaid_code": {"type": "string"}},
                        "required": ["mermaid_code"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        res = MarkdownMermaidSyntaxLintHealer.heal_mermaid(args.get("mermaid_code", ""))
        return {
            "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
        }
    return {}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            try:
                r = json.loads(line)
                out = handle_request(r)
                print(json.dumps(out), flush=True)
            except Exception as e:
                print(json.dumps({"error": str(e)}), flush=True)
