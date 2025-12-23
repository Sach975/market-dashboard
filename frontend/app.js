const API_BASE = "http://127.0.0.1:8000";

async function fetchScore() {
    const res = await fetch(`${API_BASE}/score`);
    const data = await res.json();
    const lastScore = data.score[data.score.length - 1];
    document.getElementById("score").textContent = lastScore;
}

async function fetchMetrics() {
    const res = await fetch(`${API_BASE}/metrics`);
    const data = await res.json();
    document.getElementById("metrics").textContent =
        JSON.stringify(data.metrics, null, 2);
}

async function loadDashboard() {
    await fetchScore();
    await fetchMetrics();
}

loadDashboard();
