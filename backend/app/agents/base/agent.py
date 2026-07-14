"""Base agent classes and shared utilities."""
from typing import Any, Dict

class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    async def plan(self, task: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

    async def execute(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

    async def review(self, result: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError
