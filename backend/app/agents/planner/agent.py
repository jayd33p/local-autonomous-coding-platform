"""Planner agent skeleton"""
from ..base.agent import BaseAgent

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("planner")

    async def plan(self, task):
        # Very simple planning: return task as plan
        print("Planner: creating plan for", task.get("title"))
        return {"plan": f"Implement {task.get('title')}", "task": task}
