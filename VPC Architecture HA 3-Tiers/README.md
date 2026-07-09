# AWS Production 3-Tier High Availability Architecture ☁️

## 📌 Présentation du projet

Ce projet consiste à concevoir et déployer une infrastructure AWS **hautement disponible, sécurisée et scalable** suivant les bonnes pratiques d'architecture Cloud en environnement de production.

L'objectif est de mettre en place une application web basée sur une architecture **3-Tier** séparant :

* la couche présentation (Load Balancer)
* la couche application (serveurs privés)
* la couche base de données (RDS privé)

L'ensemble de l'infrastructure est déployé avec **AWS CloudFormation (Infrastructure as Code)** afin de garantir une architecture reproductible et automatisée.

---

# 🎯 Objectifs

Ce projet démontre la capacité à :

* Concevoir une architecture AWS Production Ready
* Implémenter une architecture réseau sécurisée
* Déployer des ressources Multi-AZ
* Automatiser l'infrastructure avec CloudFormation
* Mettre en place la haute disponibilité
* Appliquer le principe du moindre privilège
* Configurer la supervision et les alertes
* Réaliser des tests de résilience et de récupération

---

# 🏗️ Architecture globale

Architecture déployée dans une région AWS avec deux Availability Zones :

```
                    Internet
                       |
                       |
              Application Load Balancer
                       |
          -----------------------------
          |                           |
     Public Subnet AZ-A          Public Subnet AZ-B
          |
          |
    Auto Scaling Group (EC2)
          |
 -------------------------------
 |                             |
Private App Subnet AZ-A   Private App Subnet AZ-B
 |                             |
 |                             |
        RDS MySQL Multi-AZ
               |
 -------------------------------
 Private Database Subnets
```

---

# 🌐 Conception réseau VPC

## VPC

Configuration :

* CIDR : `10.0.0.0/16`
* DNS Support activé
* DNS Hostnames activé
* Déploiement Multi-AZ

---

## Sous-réseaux

### Public Subnets

Utilisés pour :

* Application Load Balancer
* NAT Gateway

Exemple :

```
10.0.1.0/24  → us-east-1a
10.0.2.0/24  → us-east-1b
```

---

### Private Application Subnets

Utilisés pour :

* Instances EC2
* Serveurs applicatifs

Exemple :

```
10.0.10.0/24 → us-east-1a
10.0.11.0/24 → us-east-1b
```

---

### Private Database Subnets

Utilisés pour :

* Amazon RDS MySQL

Exemple :

```
10.0.20.0/24 → us-east-1a
10.0.21.0/24 → us-east-1b
```

---

# ⚙️ Services AWS utilisés

## Networking

| Service          | Utilisation                  |
| ---------------- | ---------------------------- |
| Amazon VPC       | Réseau isolé                 |
| Internet Gateway | Accès Internet public        |
| NAT Gateway      | Accès Internet sortant privé |
| Route Tables     | Routage réseau               |
| VPC Flow Logs    | Analyse trafic réseau        |

---

## Compute

| Service            | Utilisation             |
| ------------------ | ----------------------- |
| Amazon EC2         | Serveurs application    |
| Launch Template    | Configuration instances |
| Auto Scaling Group | Scaling automatique     |
| Systems Manager    | Accès sans SSH          |

---

## Load Balancing

| Service                   | Utilisation              |
| ------------------------- | ------------------------ |
| Application Load Balancer | Distribution trafic HTTP |
| Target Group              | Gestion des instances    |

---

## Database

| Service          | Utilisation            |
| ---------------- | ---------------------- |
| Amazon RDS MySQL | Base de données privée |
| Multi-AZ         | Haute disponibilité    |

---

## Monitoring

| Service           | Utilisation         |
| ----------------- | ------------------- |
| CloudWatch        | Supervision         |
| CloudWatch Alarms | Alertes             |
| CloudWatch Logs   | Centralisation logs |

---

# 🔐 Sécurité

Le projet applique le principe du **Least Privilege**.

## Security Groups

### SG-ALB

Autorise :

```
Internet → HTTP 80
```

---

### SG-AppServers

Autorise uniquement :

```
SG-ALB → HTTP 80
```

Aucune connexion directe depuis Internet.

---

### SG-DB

Autorise uniquement :

```
SG-AppServers → MySQL 3306
```

La base de données n'est jamais exposée publiquement.

---

# 🚀 Haute disponibilité

La disponibilité est assurée par :

## Multi Availability Zones

Les ressources sont réparties sur :

```
us-east-1a
us-east-1b
```

---

## Auto Scaling

Configuration :

```
Minimum : 2 instances
Desired : 2 instances
Maximum : 4 instances
```

En cas de panne :

```
EC2 Failure
      |
      ↓
Auto Scaling détecte
      |
      ↓
Nouvelle instance créée
```

---

## RDS Multi-AZ

Configuration :

* MySQL 8.0
* Backup automatique
* Chiffrement activé
* Déploiement Multi-AZ

---

# 📊 Monitoring

Des alarmes CloudWatch sont configurées :

## EC2

* CPUUtilization
* StatusCheckFailed

## ALB

* RequestCount
* TargetResponseTime

---

# 🏗️ Infrastructure as Code

Toutes les ressources sont déployées avec :

```
AWS CloudFormation
```

Avantages :

* Infrastructure reproductible
* Versionnement Git
* Déploiement automatisé
* Suppression contrôlée

---

# 🧪 Tests réalisés

## Test End-to-End

Flux testé :

```
Browser
   |
   ↓
ALB DNS
   |
   ↓
EC2 Application Server
   |
   ↓
RDS MySQL
```

Résultat :

✅ Application accessible
✅ Instances Healthy
✅ Connexion base fonctionnelle

---

## Session Manager Test

Validation :

```
AWS Console
      |
      ↓
Systems Manager Session Manager
      |
      ↓
EC2 Private Instance
```

Résultat :

✅ Accès sans clé SSH
✅ Aucun port 22 exposé

---

## Disaster Recovery Tests

Tests réalisés :

* Suppression instance EC2
* Vérification Auto Scaling
* Validation remplacement automatique
* Vérification disponibilité ALB

---

## Failover Tests

Tests :

* Indisponibilité d'une instance
* Routage automatique vers une autre cible
* Vérification santé Target Group

---

# 📂 Structure du projet

```
aws-production-3tier/

├── cloudformation/
│
├── network/
│
├── security/
│
├── compute/
│
├── database/
│
├── monitoring/
│
├── scripts/
│
├── tests/
│
├── docs/
│
└── README.md
```

---

# 🧠 Compétences démontrées

Ce projet démontre des compétences en :

* AWS Cloud Architecture
* Amazon VPC
* EC2
* Auto Scaling
* Application Load Balancer
* RDS MySQL
* IAM
* Systems Manager
* CloudWatch
* Infrastructure as Code
* Network Security
* High Availability
* Disaster Recovery

---

# 🔮 Améliorations futures

Évolutions possibles :

* Ajouter un pipeline CI/CD avec GitHub Actions
* Ajouter Terraform
* Ajouter Docker et ECS
* Ajouter AWS WAF
* Ajouter Route 53 + domaine personnalisé
* Ajouter HTTPS avec ACM
* Ajouter tests automatisés

---

# 👨‍💻 Auteur

Cloud Engineer Junior spécialisé AWS

Projet réalisé dans le cadre de la pratique Cloud Engineering et préparation aux environnements professionnels AWS.
