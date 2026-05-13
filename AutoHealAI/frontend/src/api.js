import axios from "axios";

// Prefer VITE_API_URL when set (e.g. production behind a gateway).
// Default to relative /api/v1 so Vite's dev proxy forwards to the backend.
const baseURL = import.meta.env.VITE_API_URL || "/api/v1";

const API = axios.create({
  baseURL,
});

let token = "";

export const bootstrapAuth = async () => {
  if (token) return token;
  const { data } = await API.post("/auth/login", {
    email: "admin@autohealai.local",
    password: "admin123",
  });
  token = data.access_token;
  API.defaults.headers.common.Authorization = `Bearer ${token}`;
  return token;
};

export const getMetrics = () => API.get("/telemetry/latest");
export const getPredictions = () => API.get("/predictions/");
export const getIncidents = () => API.get("/incidents/");
export const getDecisions = () => API.get("/decisions/");
