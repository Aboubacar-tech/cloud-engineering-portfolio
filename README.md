# 🚀 AWS CloudWatch Monitoring & Auto-Remediation Lab

## 📌 Overview

This project demonstrates a complete **AWS cloud monitoring, observability, and auto-remediation system** using real AWS services.

It simulates a **production-like environment** where logs, metrics, alerts, failures, and automated recovery are implemented end-to-end.

---

## 🏗️ Architecture

The system is built using the following AWS services:

* Amazon EC2 (Ubuntu 22.04)
* Amazon CloudWatch Agent
* Amazon CloudWatch Logs
* Amazon CloudWatch Metrics
* Amazon CloudWatch Alarms
* Amazon SNS (Email Notifications)
* AWS Lambda (Automation & API)
* Amazon API Gateway
* CloudWatch Log Insights

📸 Architecture Diagram:

```
architecture/architecture-diagram.png
```

---

## 🔄 System Workflow

### 1. Data Collection

* EC2 generates logs and system metrics
* CloudWatch Agent sends logs to CloudWatch

### 2. Monitoring

* CloudWatch tracks CPU, disk, and network usage
* Logs are centralized in CloudWatch Logs

### 3. Alerting

* CloudWatch Alarms monitor CPU > 70%
* SNS sends email notifications

### 4. Automation

* Lambda triggers automatic EC2 reboot
* Self-healing infrastructure implemented

### 5. Analysis

* CloudWatch Log Insights used for:

  * error detection
  * log filtering
  * performance analysis

---

## 🧪 Features Implemented

### 🔹 Infrastructure Setup

* EC2 instance deployment (t2.micro)
* SSH configuration
* IAM role setup

### 🔹 Logging System

* Custom application logs
* INFO / WARN / ERROR simulation
* CloudWatch Agent integration

### 🔹 Monitoring & Alerts

* CPU threshold alarms
* SNS email notifications
* Metric visualization

### 🔹 Log Analytics

* CloudWatch Log Insights queries
* AI-assisted log analysis
* Natural language query support

### 🔹 Serverless Integration

* AWS Lambda function execution
* API Gateway endpoint
* Simulated API failures (200/500 responses)

### 🔹 Auto-Remediation

* Automatic EC2 reboot on alarm
* Event-driven recovery system

### 🔹 Chaos Engineering

* CPU stress tests
* Disk pressure simulation
* Metrics gap analysis

---

## 🛠️ Project Structure

```
aws-cloudwatch-monitoring-lab/
│
├── architecture/
├── screenshots/
├── scripts/
├── lambda/
├── queries/
├── docs/
└── README.md
```

---

## ⚙️ How to Run This Project

### 1. Launch EC2

* Ubuntu 22.04 LTS
* Instance type: t2.micro
* Open ports: 22, 80

---

### 2. Install CloudWatch Agent

```bash
sudo apt update
sudo apt install amazon-cloudwatch-agent -y
```

---

### 3. Start Log Generator

```bash
chmod +x scripts/log-generator.sh
nohup scripts/log-generator.sh &
```

---

### 4. Deploy Lambda

* Upload `lambda/cloudwatch-demo`
* Configure API Gateway trigger

---

### 5. Create Alarm

* Metric: CPUUtilization
* Threshold: > 70%
* Action: SNS + Lambda

---

## 📊 CloudWatch Log Insights Queries

### Latest logs

```sql
fields @timestamp, @message
| sort @timestamp desc
| limit 50
```

### Error detection

```sql
fields @timestamp, @message
| filter @message like /ERROR/
```

### Events per minute

```sql
stats count(*) as events by bin(1m)
```

---

## 💡 Key Learnings

This project helped me master:

* AWS CloudWatch (Logs, Metrics, Alarms)
* Infrastructure Monitoring & Observability
* Incident Detection & Response
* Serverless Architecture (Lambda + API Gateway)
* Auto-Remediation Systems
* Chaos Engineering Principles
* Log Analysis & Troubleshooting

---

## 🔥 Real-World Value

This architecture simulates a **real production DevOps environment** where:

* Systems are monitored in real-time
* Failures are detected automatically
* Alerts notify engineers instantly
* Systems self-heal without manual intervention

---

## 📸 Screenshots

All steps of the project are documented in:

```
/screenshots
```

Including:

* EC2 setup
* CloudWatch logs
* Alarms
* Lambda execution
* Dashboard metrics
* Chaos testing

---

## 👨‍💻 Author

BakaryCamara**

Aspiring Cloud Engineer

---

## 🏁 Conclusion

This project demonstrates a complete **end-to-end AWS observability pipeline**, including monitoring, logging, alerting, automation, and self-healing infrastructure.

It reflects real-world DevOps practices used in production systems.

---

⭐ If you like this project, feel free to star the repository!
