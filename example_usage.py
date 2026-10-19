"""Example usage for Markdown Mermaid Syntax Lint Healer."""
from client import MarkdownMermaidSyntaxLintHealer

if __name__ == "__main__":
    raw_mermaid = """graph TD
    A[Start (Process)] ---> B[Verify Data]
"""
    res = MarkdownMermaidSyntaxLintHealer.heal_mermaid(raw_mermaid)
    print("Healed Mermaid Diagram:")
    print(res["healed_mermaid"])
