# AWS CloudWatch Monitoring & Auto-Remediation Architecture

## Overview

This project demonstrates a complete monitoring, observability, alerting, and automated remediation workflow using AWS services.

The architecture simulates a real production environment where application logs are collected, monitored, analyzed, and used to trigger automated recovery actions.

---

## Architecture Components

### Amazon EC2

The EC2 instance hosts the application and generates logs and system metrics.

Responsibilities:

* Run application workload
* Generate INFO, WARN, and ERROR logs
* Produce CPU, network, and disk metrics

---

### Amazon CloudWatch Agent

Installed on the EC2 instance.

Responsibilities:

* Collect application logs
* Send logs to CloudWatch Logs
* Publish custom metrics

---

### Amazon CloudWatch Logs

Centralized log storage service.

Responsibilities:

* Store application logs
* Enable log retention
* Support log analytics

---

### Amazon CloudWatch Log Insights

Log analytics engine.

Responsibilities:

* Search logs
* Detect errors
* Generate operational insights
* Support AI-assisted analysis

---

### Amazon CloudWatch Alarms

Monitoring and alerting service.

Responsibilities:

* Monitor CPU utilization
* Detect abnormal behavior
* Trigger notifications
* Launch remediation workflows

---

### Amazon SNS

Notification service.

Responsibilities:

* Deliver email alerts
* Notify operators during incidents

---

### AWS Lambda (cloudwatch-demo)

Serverless application endpoint.

Responsibilities:

* Simulate application traffic
* Generate successful and failed requests
* Produce realistic logs

---

### Amazon API Gateway

Public API endpoint.

Responsibilities:

* Receive HTTP requests
* Route traffic to Lambda

---

### AWS Lambda (auto-remediate-ec2)

Automated recovery service.

Responsibilities:

* Receive CloudWatch Alarm events
* Reboot EC2 instances automatically
* Restore service availability

---

## Monitoring Flow

EC2 Instance

↓

CloudWatch Agent

↓

CloudWatch Logs

↓

CloudWatch Log Insights

↓

CloudWatch Alarms

↓

SNS Email Notifications

or

↓

Lambda Auto Remediation

↓

EC2 Reboot

---

## Skills Demonstrated

* Cloud Monitoring
* Observability
* Incident Response
* Log Analytics
* Infrastructure Troubleshooting
* Serverless Computing
* Auto Remediation
* AWS Operations
* DevOps Practices

---

## Author

Bakary Camara

AWS Cloud Portfolio Project
