# Architecture Overview - AWS Production 3-Tier High Availability Architecture

## 1. Vue générale de l'architecture

Cette architecture AWS implémente une application web hautement disponible basée sur un modèle **3-Tier Architecture**.

Les trois couches principales sont :

* **Presentation Tier** : Application Load Balancer (ALB)
* **Application Tier** : Instances EC2 privées gérées par Auto Scaling Group
* **Database Tier** : Amazon RDS MySQL privé en configuration Multi-AZ

L'infrastructure est déployée dans un VPC isolé avec deux Availability Zones afin d'assurer la disponibilité, la résilience et la scalabilité.

---

# 2. Architecture réseau

## VPC

Configuration :

* Région : us-east-1
* CIDR Block : 10.0.0.0/16
* DNS Support : Activé
* DNS Hostnames : Activé
* Architecture Multi-AZ

## Subnets

### Public Subnets

Utilisation :

* Application Load Balancer
* NAT Gateway
* Internet Gateway

| Subnet   | CIDR        | Availability Zone |
| -------- | ----------- | ----------------- |
| Public-A | 10.0.1.0/24 | us-east-1a        |
| Public-B | 10.0.2.0/24 | us-east-1b        |

---

### Private Application Subnets

Utilisation :

* Instances EC2
* Serveurs applicatifs

| Subnet | CIDR         | Availability Zone |
| ------ | ------------ | ----------------- |
| App-A  | 10.0.10.0/24 | us-east-1a        |
| App-B  | 10.0.11.0/24 | us-east-1b        |

---

### Private Database Subnets

Utilisation :

* Amazon RDS MySQL
* Stockage des données

| Subnet | CIDR         | Availability Zone |
| ------ | ------------ | ----------------- |
| DB-A   | 10.0.20.0/24 | us-east-1a        |
| DB-B   | 10.0.21.0/24 | us-east-1b        |

---

# 3. Flux réseau de l'application

## Requête utilisateur

Flux principal :

```
Internet
   |
   |
HTTP/HTTPS
   |
   ↓
Application Load Balancer
   |
   |
HTTP 80
   |
   ↓
EC2 Auto Scaling Group
   |
   |
MySQL 3306
   |
   ↓
Amazon RDS MySQL
```

---

# 4. Couche Load Balancing

## Application Load Balancer

Service :

Amazon Application Load Balancer

Configuration :

* Type : Internet-facing
* Listener : HTTP Port 80
* Déployé dans deux subnets publics
* Distribution automatique du trafic

Rôle :

* Recevoir les requêtes utilisateurs
* Vérifier la santé des instances
* Distribuer le trafic vers les serveurs applicatifs

---

# 5. Couche Application

## Auto Scaling Group

Configuration :

```
Minimum instances : 2
Desired capacity : 2
Maximum instances : 4
```

Instances :

* EC2 dans les subnets privés
* Déployées sur plusieurs Availability Zones
* Créées avec un Launch Template

Fonctionnement :

```
Instance EC2 Failure

        ↓

Auto Scaling détecte la panne

        ↓

Nouvelle instance créée automatiquement

        ↓

ALB ajoute la nouvelle cible
```

---

# 6. Couche Database

## Amazon RDS MySQL

Configuration :

* Engine : MySQL 8.0
* Déploiement : Multi-AZ
* Accès public : Désactivé
* Chiffrement : Activé
* Backup automatique activé

Sécurité :

La base de données accepte uniquement :

```
SG-AppServers
       |
       |
       ↓
MySQL Port 3306
       |
       |
       ↓
SG-DB
```

---

# 7. Sécurité réseau

## Security Groups

## SG-ALB

Autorise :

```
Internet
   |
   ↓
HTTP 80
   |
   ↓
ALB
```

---

## SG-AppServers

Autorise uniquement :

```
SG-ALB

   ↓

HTTP 80

   ↓

EC2 Instances
```

Aucun accès direct Internet.

---

## SG-DB

Autorise uniquement :

```
SG-AppServers

      ↓

MySQL 3306

      ↓

RDS
```

---

# 8. Haute disponibilité

La disponibilité est assurée par :

## Multi Availability Zones

Ressources réparties :

```
Availability Zone A

- Public Subnet
- Private App Subnet
- Private DB Subnet


Availability Zone B

- Public Subnet
- Private App Subnet
- Private DB Subnet
```

---

# 9. Monitoring et observabilité

Services utilisés :

## Amazon CloudWatch

Surveillance :

* CPU Utilization EC2
* StatusCheckFailed
* ALB RequestCount
* ALB TargetResponseTime

## VPC Flow Logs

Objectifs :

* Analyse du trafic réseau
* Détection des problèmes
* Audit sécurité

## Systems Manager Session Manager

Utilisation :

* Accès sécurisé aux instances privées
* Aucun accès SSH nécessaire
* Aucun fichier clé `.pem`

---

# 10. Infrastructure as Code

L'ensemble de l'infrastructure est déployé avec :

```
AWS CloudFormation
```

Avantages :

* Déploiement reproductible
* Gestion versionnée avec Git
* Automatisation complète
* Réduction des erreurs manuelles

---

# 11. Résumé de l'architecture

```
                 Users
                   |
                   |
              Internet
                   |
                   |
             ALB (Public)
                   |
        ---------------------
        |                   |
     EC2 AZ-A            EC2 AZ-B
   Private App        Private App
        |                   |
        ---------------------
                   |
             RDS MySQL
              Multi-AZ
          Private Database
```

Cette architecture fournit :

* Haute disponibilité
* Scalabilité automatique
* Sécurité réseau renforcée
* Isolation des couches
* Monitoring complet
* Résilience face aux pannes
