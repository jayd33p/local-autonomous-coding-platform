"""Coder agent skeleton"""
from ..base.agent import BaseAgent

class CoderAgent(BaseAgent):
    def __init__(self):
        super().__init__("coder")

    async def execute(self, plan):
        # Placeholder: would call Ollama or another model
        print("Coder: executing plan", plan.get("plan"))
        return {"files": [{"path": "example.txt", "content": "// TODO implement"}], "plan": plan}
