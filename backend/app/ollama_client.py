"""Simple Ollama client wrapper (placeholder)."""
import httpx

class OllamaClient:
    def __init__(self, base_url: str = "http://127.0.0.1:11434"):
        self.base_url = base_url
        self._client = httpx.AsyncClient()

    async def generate(self, model: str, prompt: str):
        # Placeholder: adapt to your local Ollama HTTP API if available
        try:
            resp = await self._client.post(f"{self.base_url}/api/generate", json={"model": model, "prompt": prompt}, timeout=30)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

# single client
ollama = OllamaClient()
