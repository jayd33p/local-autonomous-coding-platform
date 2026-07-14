"""Simple in-memory task queue used for initial development."""
import asyncio
from typing import Any, Dict

class InMemoryQueue:
    def __init__(self):
        self._q = asyncio.Queue()

    async def put(self, item: Dict[str, Any]):
        await self._q.put(item)

    async def get(self):
        return await self._q.get()

    def empty(self):
        return self._q.empty()

# Single global queue for the process
global_queue = InMemoryQueue()
