"""Orchestrator skeleton to wire agents and the queue."""
from .queue import global_queue
from .agents.planner.agent import PlannerAgent
from .agents.coder.agent import CoderAgent
from .agents.reviewer.agent import ReviewerAgent

_planner = PlannerAgent()
_coder = CoderAgent()
_reviewer = ReviewerAgent()

def setup():
    # Placeholder: start background tasks, worker loops, etc.
    print("Orchestrator setup: registering agents")

async def enqueue_task(task):
    await global_queue.put(task)

async def worker_loop():
    while True:
        task = await global_queue.get()
        # simple flow: planner -> coder -> reviewer
        print("Orchestrator got task:", task)
        plan = await _planner.plan(task)
        code_result = await _coder.execute(plan)
        review = await _reviewer.review(code_result)
        print("Task completed. Review:", review)
