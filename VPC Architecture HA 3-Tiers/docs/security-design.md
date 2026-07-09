# Security Design - AWS Production 3-Tier High Availability Architecture

## 1. Introduction

La sécurité de cette architecture AWS repose sur plusieurs couches de protection :

* Isolation réseau avec VPC
* Segmentation des sous-réseaux
* Security Groups avec principe du moindre privilège
* Contrôle d'accès IAM
* Accès administrateur sécurisé avec Systems Manager Session Manager
* Base de données privée non exposée sur Internet

L'objectif est de limiter les accès uniquement aux flux nécessaires au fonctionnement de l'application.

---

# 2. Architecture de sécurité réseau

L'infrastructure utilise une séparation en trois niveaux :

```text
Internet

   |

   ↓

Public Layer
(ALB)

   |

   ↓

Application Layer
(EC2 Private)

   |

   ↓

Database Layer
(RDS Private)
```

Chaque couche possède ses propres règles de sécurité.

---

# 3. Isolation réseau VPC

## VPC

Configuration :

```
CIDR : 10.0.0.0/16
DNS Support : Enabled
DNS Hostnames : Enabled
```

Le VPC fournit un environnement réseau isolé pour toutes les ressources AWS.

---

# 4. Sécurité des sous-réseaux

## Public Subnets

Utilisation :

* Application Load Balancer
* NAT Gateway

Accessible depuis Internet uniquement via :

```
Internet
   |
   ↓
Internet Gateway
   |
   ↓
ALB
```

---

## Private Application Subnets

Utilisation :

* Instances EC2
* Serveurs applicatifs

Caractéristiques :

* Pas d'adresse IP publique
* Pas d'accès direct Internet entrant
* Accès sortant via NAT Gateway uniquement

---

## Private Database Subnets

Utilisation :

* Amazon RDS MySQL

Caractéristiques :

* Pas d'accès Internet
* Pas d'adresse IP publique
* Accessible uniquement depuis la couche application

---

# 5. Security Groups

Les Security Groups appliquent le principe :

```
Deny by default
Allow only required traffic
```

---

# SG-ALB

## Objectif

Contrôler le trafic entrant vers le Load Balancer.

Règles entrantes :

| Source    | Port | Protocol | Usage             |
| --------- | ---- | -------- | ----------------- |
| 0.0.0.0/0 | 80   | HTTP     | Accès utilisateur |

Règles sortantes :

| Destination   | Port |
| ------------- | ---- |
| SG-AppServers | 80   |

Flux autorisé :

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

# SG-AppServers

## Objectif

Protéger les serveurs applicatifs.

Règles entrantes :

| Source | Port | Protocol | Usage              |
| ------ | ---- | -------- | ------------------ |
| SG-ALB | 80   | HTTP     | Trafic application |

Aucun accès :

```
Internet ❌
SSH public ❌
```

Flux autorisé :

```
ALB

 ↓ HTTP 80

EC2 Application Servers
```

---

# SG-DB

## Objectif

Protéger la base de données.

Règles entrantes :

| Source        | Port | Protocol | Usage                       |
| ------------- | ---- | -------- | --------------------------- |
| SG-AppServers | 3306 | MySQL    | Application database access |

Aucun accès :

```
Internet ❌
ALB ❌
Utilisateur direct ❌
```

Flux autorisé :

```
EC2

 ↓ MySQL 3306

RDS MySQL
```

---

# 6. IAM Security

## EC2 Instance Role

Les instances EC2 utilisent un rôle IAM au lieu de clés d'accès statiques.

Politique attachée :

```
AmazonSSMManagedInstanceCore
```

Permet :

* Connexion Session Manager
* Gestion distante sécurisée
* Aucun échange de clé SSH

---

# 7. Accès administrateur sécurisé

## AWS Systems Manager Session Manager

Méthode traditionnelle :

```
Administrateur

 ↓

SSH Port 22

 ↓

EC2
```

Ancienne approche :

* Gestion de clés privées
* Ouverture du port 22
* Risque de brute force

Nouvelle approche :

```
Administrateur

 ↓

AWS Systems Manager

 ↓

EC2 Private Instance
```

Avantages :

* Aucun port SSH ouvert
* Aucun fichier .pem
* Traçabilité CloudWatch
* Contrôle IAM

---

# 8. Sécurité RDS MySQL

Configuration :

* Deployment privé
* Multi-AZ
* Encryption activée
* Backup automatique
* Public Access désactivé

Accès :

```
SG-AppServers

      |

      ↓

 MySQL 3306

      |

      ↓

RDS Database
```

---

# 9. Protection des données

Mesures appliquées :

## Encryption

Données chiffrées :

* Volumes EBS
* Base RDS
* Snapshots

## Backup

RDS utilise :

* Automated Backups
* Point-in-Time Recovery

---

# 10. Monitoring sécurité

## VPC Flow Logs

Permet :

* Analyse du trafic réseau
* Détection d'activités suspectes
* Audit sécurité

Destination :

```
CloudWatch Logs

/aws/vpc/production-flow-logs
```

---

## CloudWatch Monitoring

Surveillance :

* CPU EC2
* Status Check
* ALB Requests
* ALB Response Time

---

# 11. Matrice des flux réseau

| Source   | Destination | Port | Autorisé |
| -------- | ----------- | ---- | -------- |
| Internet | ALB         | 80   | Oui      |
| ALB      | EC2         | 80   | Oui      |
| EC2      | RDS         | 3306 | Oui      |
| Internet | EC2         | Tous | Non      |
| Internet | RDS         | Tous | Non      |
| ALB      | RDS         | 3306 | Non      |

---

# 12. Bonnes pratiques appliquées

✅ Least Privilege Security Groups
✅ Private Database Layer
✅ No Public SSH Access
✅ IAM Roles instead of Access Keys
✅ Multi-AZ Deployment
✅ Encryption Enabled
✅ Network Segmentation
✅ Centralized Logging
✅ Infrastructure as Code

---

# Conclusion

Cette architecture applique les principes fondamentaux de sécurité AWS :

* Défense en profondeur
* Moindre privilège
* Isolation réseau
* Accès contrôlé par identité
* Surveillance continue

Elle fournit une base sécurisée adaptée à un environnement de production Cloud.
