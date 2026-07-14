"""Reviewer agent skeleton"""
from ..base.agent import BaseAgent

class ReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__("reviewer")

    async def review(self, result):
        print("Reviewer: reviewing result")
        return {"review": "Looks ok", "issues": []}
