# DevOps Automation & Monitoring

This repository contains solutions to a three-part DevOps assignment focused on automation scripting, log monitoring, and Kubernetes prioritization.

---

## Section 1: Python Automation Script

**Problem Statement:**  
Create a Python script that continuously monitors Docker containers on a host and triggers an alert if any container’s CPU usage exceeds a specified threshold (e.g., 80%).

### 🧰 Features

- **Connect to Docker:** Uses Docker SDK to list running containers.
- **Monitor Resources:** Checks CPU usage for each container.
- **Threshold & Alert:** Logs the event and simulates an alert when usage exceeds a set limit.
- **Robustness:** Includes error handling, logging, and graceful exits.

---

## Section 2: Bash Log Monitoring Script

**Problem Statement:**  
Develop a Bash script that monitors a specified log file for error patterns (e.g., "ERROR", "CRITICAL") and raises alerts accordingly.

### 🧰 Features

- **Real-Time Monitoring:** Watches the log file continuously.
- **Error Counting:** Counts error pattern occurrences in a moving time window.
- **Alerting:** Triggers alerts if the count exceeds the threshold.
- **Resilience:** Handles log rotation and temporary unavailability.

---

## Section 3: DevOps Prioritization Strategy

From a DevOps engineer’s perspective, the following automation and operational tasks are prioritized based on impact, scalability, and reliability:

- **CI/CD Pipelines** are given top priority to ensure seamless, consistent delivery of microservices into Kubernetes environments.
- **Monitoring & Alerting Setup** with tools like Prometheus and Grafana follows to ensure real-time visibility and system health tracking.
- **Infrastructure as Code (IaC)** via Helm or Kustomize is key to consistent and replicable deployments.
- **Automated Testing and Code Quality Gates** are vital for maintaining standards and enabling faster releases.
- **Documentation** is important but typically follows after automation is in place.

These rankings are shaped by real-world considerations around scalability, incident response time, and developer productivity.

---

## 🧪 Running the Scripts

### Python Docker Monitor
```bash
pip install docker
python monitor_containers.py
