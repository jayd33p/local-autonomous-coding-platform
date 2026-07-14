import React, { useEffect, useState } from "react";

export default function App() {
  const [agents, setAgents] = useState([]);
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    // Fetch agents from backend
    fetch("http://localhost:8000/agents")
      .then((r) => r.json())
      .then(setAgents)
      .catch((err) => console.error("Failed to fetch agents:", err));
  }, []);

  useEffect(() => {
    // Connect to WebSocket logs (backend)
    let ws;
    try {
      ws = new WebSocket("ws://localhost:8000/ws/logs");
    } catch (e) {
      console.error("WS init error", e);
      return;
    }
    ws.onopen = () => console.log("WS connected");
    ws.onmessage = (evt) => setLogs((s) => [evt.data, ...s]);
    ws.onclose = () => console.log("WS closed");
    ws.onerror = (e) => console.error("WS error", e);
    return () => ws.close();
  }, []);

  return (
    <div style={{ padding: 20, fontFamily: "system-ui, sans-serif" }}>
      <h1>Local Autonomous Coding Platform</h1>

      <section>
        <h2>Agents</h2>
        {agents.length === 0 ? (
          <div>No agents found (or failed to fetch)</div>
        ) : (
          <ul>{agents.map((a) => <li key={a}>{a}</li>)}</ul>
        )}
      </section>

      <section style={{ marginTop: 20 }}>
        <h2>Live Logs</h2>
        <div style={{ maxHeight: 300, overflow: "auto", padding: 8, border: "1px solid #eee" }}>
          {logs.length === 0 ? <div>No logs yet</div> : logs.map((l, i) => <div key={i}>{l}</div>)}
        </div>
      </section>
    </div>
  );
}
