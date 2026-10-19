"""Markdown Mermaid Syntax Lint Healer.
100% Python Standard Library.
"""
import re

class MarkdownMermaidSyntaxLintHealer:
    """LLM output Mermaid diagram linting, unquoted bracket healing, and syntax normalization engine."""

    @staticmethod
    def heal_mermaid(mermaid_code: str) -> dict:
        lines = mermaid_code.splitlines()
        healed_lines = []
        fixes = []

        for line in lines:
            fixed_line = line
            m = re.search(r'(\w+)\[([^\"\'\]]*[\(\)][^\"\'\]]*)\]', line)
            if m:
                node_id, label = m.group(1), m.group(2)
                replacement = f'{node_id}["{label}"]'
                fixed_line = fixed_line.replace(f'{node_id}[{label}]', replacement)
                fixes.append(f"Quoted label with parentheses in node '{node_id}'")

            if "--->" in fixed_line:
                fixed_line = fixed_line.replace("--->", "-->")
                fixes.append("Normalized elongated arrow '--->' to '-->'")

            healed_lines.append(fixed_line)

        healed_code = "\n".join(healed_lines)
        return {
            "original_lines": len(lines),
            "fixes_applied": len(fixes),
            "fix_details": fixes,
            "healed_mermaid": healed_code,
            "is_valid": True
        }
