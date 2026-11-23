from dataclasses import dataclass, field
from typing import Any

@dataclass
class ToolCall:
    id: str
    name: str
    arguments: dict[str, Any] = field(default_factory=dict)


t = ToolCall(id="call_001", name="search")
print(t)
print(t.arguments is ToolCall(id="x", name="y").arguments)
