from dataclasses import dataclass, field
from typing import Any

@dataclass
class ToolCall:
    id: str
    name: str
    arguments: dict[str, Any] = field(default_factory=dict)

    def is_valid(self, allowed_tools: list[str]) -> bool:
        """检查这次工具调用是否在允许的工具列表内"""
        return self.name in allowed_tools

t2 = ToolCall(id="call_002", name="delete_all_files")
print(t2.is_valid(["search", "calculator"]))
print(t2.is_valid(["search", "delete_all_files"]))

# t = ToolCall(id="call_001", name="search")
# print(t)
# print(t.arguments is ToolCall(id="x", name="y").arguments)

