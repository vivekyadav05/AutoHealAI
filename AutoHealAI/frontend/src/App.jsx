import { NavLink, Route, Routes } from "react-router-dom";
import { useEffect, useMemo, useState } from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from "recharts";
import { bootstrapAuth, getMetrics, getPredictions, getIncidents, getDecisions } from "./api";

// Explicit paths avoid subtle NavLink / Route mismatches (e.g. "Infrastructure Map").
const NAV_ROUTES = [
  { path: "/", label: "Dashboard", end: true },
  { path: "/monitoring", label: "Monitoring" },
  { path: "/predictions", label: "Predictions" },
  { path: "/logs", label: "Logs" },
  { path: "/incidents", label: "Incidents" },
  { path: "/ai-decisions", label: "AI Decisions" },
  { path: "/infrastructure-map", label: "Infrastructure Map" },
  { path: "/settings", label: "Settings" },
];

const Card = ({ title, value, subtitle }) => (
  <div className="rounded-2xl bg-slate-900 border border-slate-700 p-4">
    <p className="text-slate-400 text-sm">{title}</p>
    <p className="text-2xl font-semibold mt-2">{value}</p>
    {subtitle && <p className="text-xs text-slate-500 mt-1">{subtitle}</p>}
  </div>
);

function Dashboard() {
  const [metrics, setMetrics] = useState([]);
  const [predictions, setPredictions] = useState([]);
  const [incidents, setIncidents] = useState([]);
  const [decisions, setDecisions] = useState([]);

  useEffect(() => {
    const load = async () => {
      await bootstrapAuth();
      const [m, p, i, d] = await Promise.all([getMetrics(), getPredictions(), getIncidents(), getDecisions()]);
      setMetrics(m.data.reverse());
      setPredictions(p.data);
      setIncidents(i.data);
      setDecisions(d.data);
    };
    load();
    const timer = setInterval(load, 5000);
    return () => clearInterval(timer);
  }, []);

  const latest = metrics[metrics.length - 1];
  const highRisk = useMemo(() => predictions.filter((x) => x.severity === "critical" || x.severity === "high").length, [predictions]);

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Autonomous AI Infrastructure Intelligence</h1>
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card title="CPU Usage" value={`${latest?.cpu ?? 0}%`} subtitle="Live cluster avg" />
        <Card title="Memory Usage" value={`${latest?.memory ?? 0}%`} subtitle="Live cluster avg" />
        <Card title="High Risk Predictions" value={highRisk} subtitle="AI failure warnings" />
        <Card title="Open Incidents" value={incidents.filter((x) => x.status === "open").length} subtitle="Needs validation" />
      </div>
      <div className="rounded-2xl bg-slate-900 border border-slate-700 p-4 h-72">
        <p className="mb-3 text-slate-300">Resource Trend</p>
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={metrics}>
            <CartesianGrid stroke="#334155" strokeDasharray="3 3" />
            <XAxis dataKey="timestamp" hide />
            <YAxis />
            <Tooltip />
            <Line dataKey="cpu" stroke="#38bdf8" dot={false} />
            <Line dataKey="memory" stroke="#a78bfa" dot={false} />
            <Line dataKey="latency" stroke="#f97316" dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>
      <div className="rounded-2xl bg-slate-900 border border-slate-700 p-4">
        <p className="mb-3 text-slate-300">Latest AI Remediation Decisions</p>
        <div className="space-y-2 text-sm">
          {decisions.slice(0, 5).map((d) => (
            <div key={d.id} className="border border-slate-700 rounded-xl p-3">
              <p className="font-medium">{d.action_type} ({d.status}) - {d.service}</p>
              <p className="text-slate-400">{d.explanation}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

const Placeholder = ({ title }) => <div className="text-xl font-semibold">{title} module configured.</div>;

export default function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex">
      <aside className="w-64 border-r border-slate-800 p-4 space-y-2">
        <h2 className="text-xl font-bold mb-4">AutoHealAI</h2>
        {NAV_ROUTES.map(({ path, label, end }) => (
          <NavLink
            key={path}
            to={path}
            end={Boolean(end)}
            className={({ isActive }) =>
              `block rounded-lg px-3 py-2 text-sm ${isActive ? "bg-sky-600 text-white" : "text-slate-300 hover:bg-slate-800"}`
            }
          >
            {label}
          </NavLink>
        ))}
      </aside>
      <main className="flex-1 p-6">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/monitoring" element={<Placeholder title="Monitoring" />} />
          <Route path="/predictions" element={<Placeholder title="Predictions" />} />
          <Route path="/logs" element={<Placeholder title="Logs" />} />
          <Route path="/incidents" element={<Placeholder title="Incidents" />} />
          <Route path="/ai-decisions" element={<Placeholder title="AI Decisions" />} />
          <Route path="/infrastructure-map" element={<Placeholder title="Infrastructure Map" />} />
          <Route path="/settings" element={<Placeholder title="Settings" />} />
        </Routes>
      </main>
    </div>
  );
}
