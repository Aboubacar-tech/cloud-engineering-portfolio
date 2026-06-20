
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
architecture/aws-cloudwatch-monitoring/architecture/ChatGPT Image 20 juin 2026, 00_04_25.png
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
=======
# ☁️ Cloud Engineering Portfolio

Bienvenue dans mon portfolio de projets Cloud Engineering & DevOps.

Ce dépôt regroupe mes projets pratiques réalisés sur AWS afin de développer des compétences concrètes en :

- Architecture Cloud
- Automatisation AWS
- Infrastructure as Code
- Monitoring & Observabilité
- Conteneurisation
- Haute disponibilité
- Reprise après sinistre
- Serverless Computing
- Event-Driven Architecture
- DevOps & Cloud Operations

---

# 👨‍💻 À propos de moi

Je suis **Bakary Camara**, futur **AWS Cloud & DevOps Engineer**.

Je construis ce portfolio pour :

- développer des compétences pratiques sur AWS
- concevoir des architectures cloud réelles
- maîtriser l’automatisation et les systèmes distribués
- apprendre les bonnes pratiques DevOps et Cloud Engineering
- préparer des opportunités professionnelles dans le Cloud

---

# 🎯 Objectifs du portfolio

Ce portfolio a pour objectif de démontrer :

✅ mes compétences techniques AWS  
✅ ma capacité à documenter des architectures cloud  
✅ ma compréhension des systèmes distribués  
✅ ma maîtrise du monitoring et de l’automatisation  
✅ ma capacité à concevoir des architectures évolutives et résilientes  

Chaque projet contient :

- une documentation complète
- une architecture détaillée
- des captures d’écran
- le code source
- les services AWS utilisés
- les leçons apprises

---

# 📁 Exemple de structure d’un projet

```text
project-name/
│
├── README.md
├── architecture/
├── screenshots/
├── lambda/
├── scripts/
└── docs/
>>>>>>> 5ece64fc702785e85f8bf837c204e70328ac157e
```

---

<<<<<<< HEAD
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
=======
# 🧠 Approche d’apprentissage

Je ne me limite pas à suivre des tutoriels.

Chaque projet est conçu pour :

- comprendre le fonctionnement réel des services AWS
- apprendre à résoudre des problèmes d’ingénierie
- construire des architectures proches des environnements de production
- développer une logique DevOps et Cloud Engineering

---

# 🔥 Compétences développées

## Cloud Engineering
- Monitoring AWS
- Automatisation cloud
- Gestion des événements
- Serverless
- Gestion des incidents
- Optimisation des coûts

## DevOps
- Infrastructure as Code
- CI/CD
- Conteneurisation
- Observabilité
- Automatisation

## Architecture
- Haute disponibilité
- Scalabilité
- Résilience
- Découplage des systèmes
- Gestion des défaillances

---

# 📌 Projets en cours

- Architecture Event-Driven avec SNS, Lambda et CloudWatch
- Automatisation EC2 avec EventBridge
- Pipelines Serverless
- Infrastructure as Code avec CloudFormation
- Déploiements conteneurisés avec Docker & ECS
- Monitoring avancé AWS
- Architectures haute disponibilité

---

# 📖 Certifications AWS (Objectif)

- AWS Certified Cloud Practitioner
- AWS Certified Solutions Architect – Associate
- AWS Certified Developer – Associate
- AWS Certified SysOps Administrator

---

# 📸 Documentation des projets

Chaque projet contient :

✅ Diagrammes d’architecture  
✅ Captures AWS réelles  
✅ Journaux CloudWatch  
✅ Scripts et code source  
✅ Explications détaillées  
✅ Bonnes pratiques AWS  

---

# 🌍 Objectif professionnel

Mon objectif est de devenir :

- AWS Cloud Engineer
- DevOps Engineer
- Solutions Architect Associate
- Cloud Support Engineer

---

# 📫 Contact

## GitHub
https://github.com/Aboubacar-tech



---

# ⭐ Remarque

Ce dépôt évolue continuellement au fur et à mesure de mon apprentissage et de mes nouveaux projets Cloud & DevOps.

