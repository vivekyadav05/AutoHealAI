CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  hashed_password VARCHAR(255) NOT NULL,
  role VARCHAR(50) DEFAULT 'viewer',
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS metrics (
  id SERIAL PRIMARY KEY,
  service VARCHAR(128),
  cpu FLOAT,
  memory FLOAT,
  latency FLOAT,
  error_rate FLOAT,
  restarts INTEGER,
  timestamp TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS predictions (
  id SERIAL PRIMARY KEY,
  service VARCHAR(128),
  failure_probability FLOAT,
  severity VARCHAR(32),
  confidence FLOAT,
  recommendation TEXT,
  model_version VARCHAR(64),
  timestamp TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS incidents (
  id SERIAL PRIMARY KEY,
  service VARCHAR(128),
  status VARCHAR(32),
  root_cause TEXT,
  detected_at TIMESTAMP DEFAULT NOW(),
  resolved_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS remediation_actions (
  id SERIAL PRIMARY KEY,
  incident_id INTEGER,
  service VARCHAR(128),
  action_type VARCHAR(64),
  status VARCHAR(32),
  explanation TEXT,
  executed_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS deployment_history (
  id SERIAL PRIMARY KEY,
  service VARCHAR(128),
  version VARCHAR(64),
  deployed_by VARCHAR(128),
  risk_score FLOAT DEFAULT 0,
  is_rolled_back BOOLEAN DEFAULT FALSE,
  deployed_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS logs (
  id SERIAL PRIMARY KEY,
  service VARCHAR(128),
  level VARCHAR(16),
  message TEXT,
  timestamp TIMESTAMP DEFAULT NOW()
);

INSERT INTO users (email, hashed_password, role)
VALUES ('admin@autohealai.local', '$2b$12$6vA8QgZk6ysWY6n.n3zS2OEH2Jf6T7U3V.eA4VhRZVsR4ybKACsdu', 'admin')
ON CONFLICT (email) DO NOTHING;
