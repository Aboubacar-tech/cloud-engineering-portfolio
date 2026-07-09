# Deployment Guide - AWS Production 3-Tier High Availability Architecture

## 1. Prérequis

Avant de commencer le déploiement, les éléments suivants doivent être disponibles :

* Compte AWS actif
* AWS CLI configuré
* Permissions IAM suffisantes pour CloudFormation
* Région AWS sélectionnée : `us-east-1`

Installation et configuration AWS CLI :

```bash
aws configure
```

Vérification :

```bash
aws sts get-caller-identity
```

---

# 2. Structure des fichiers CloudFormation

Organisation recommandée :

```text
cloudformation/

├── network/
│   └── vpc.yaml
│
├── security/
│   └── security-groups.yaml
│
├── compute/
│   ├── launch-template.yaml
│   └── alb-asg.yaml
│
├── database/
│   └── rds-mysql.yaml
│
└── monitoring/
    ├── cloudwatch-alarms.yaml
    └── vpc-flow-logs.yaml
```

---

# 3. Ordre de déploiement

Les stacks doivent être déployées dans cet ordre :

```text
1. VPC Network

        ↓

2. Security Groups

        ↓

3. Launch Template

        ↓

4. ALB + Auto Scaling Group

        ↓

5. RDS MySQL

        ↓

6. CloudWatch Monitoring

        ↓

7. VPC Flow Logs
```

---

# 4. Déploiement du réseau VPC

Création de la stack réseau :

```bash
aws cloudformation create-stack \
--stack-name production-network \
--template-body file://network/vpc.yaml
```

Vérification :

```bash
aws cloudformation describe-stacks \
--stack-name production-network
```

Ressources créées :

* VPC
* Public Subnets
* Private App Subnets
* Private Database Subnets
* Internet Gateway
* NAT Gateway
* Route Tables

---

# 5. Déploiement des Security Groups

Créer les groupes de sécurité :

```bash
aws cloudformation create-stack \
--stack-name production-security \
--template-body file://security/security-groups.yaml \
--parameters \
ParameterKey=VPCId,ParameterValue=<VPC_ID>
```

Security Groups créés :

* SG-ALB
* SG-AppServers
* SG-DB

---

# 6. Création du Launch Template

Déploiement :

```bash
aws cloudformation create-stack \
--stack-name production-launch-template \
--template-body file://compute/launch-template.yaml
```

Configuration :

* Image Amazon Linux
* Apache installé automatiquement
* Agent SSM activé
* Rôle IAM `AmazonSSMManagedInstanceCore`
* User Data configuré

---

# 7. Déploiement ALB et Auto Scaling Group

Création :

```bash
aws cloudformation create-stack \
--stack-name production-alb-asg \
--template-body file://compute/alb-asg.yaml \
--parameters \
ParameterKey=VPCId,ParameterValue=<VPC_ID> \
ParameterKey=PublicSubnetA,ParameterValue=<SUBNET_A> \
ParameterKey=PublicSubnetB,ParameterValue=<SUBNET_B> \
ParameterKey=AppSubnetA,ParameterValue=<APP_SUBNET_A> \
ParameterKey=AppSubnetB,ParameterValue=<APP_SUBNET_B> \
ParameterKey=ALBSecurityGroup,ParameterValue=<SG_ALB> \
ParameterKey=LaunchTemplateId,ParameterValue=<LAUNCH_TEMPLATE_ID>
```

Créé :

* Application Load Balancer
* Target Group
* Listener HTTP 80
* Auto Scaling Group
* Instances EC2 privées

---

# 8. Déploiement RDS MySQL

Création :

```bash
aws cloudformation create-stack \
--stack-name production-database \
--template-body file://database/rds-mysql.yaml
```

Configuration :

* MySQL 8.0
* Private Subnets uniquement
* Multi-AZ activé
* Encryption activé
* Backup automatique

---

# 9. Déploiement CloudWatch Monitoring

Création :

```bash
aws cloudformation create-stack \
--stack-name production-monitoring \
--template-body file://monitoring/cloudwatch-alarms.yaml
```

Alarmes créées :

## EC2

* CPU Utilization
* Status Check

## ALB

* Request Count
* Target Response Time

---

# 10. Activation VPC Flow Logs

Déploiement :

```bash
aws cloudformation create-stack \
--stack-name production-flowlogs \
--template-body file://monitoring/vpc-flow-logs.yaml \
--capabilities CAPABILITY_NAMED_IAM
```

Configuration :

* Destination : CloudWatch Logs
* Traffic : ALL
* Rétention : 30 jours

---

# 11. Vérifications après déploiement

## Vérifier les stacks

```bash
aws cloudformation list-stacks
```

Statut attendu :

```text
CREATE_COMPLETE
```

---

## Vérifier ALB

```bash
aws elbv2 describe-load-balancers
```

---

## Vérifier Target Group

```bash
aws elbv2 describe-target-health \
--target-group-arn <TARGET_GROUP_ARN>
```

Résultat attendu :

```text
healthy
healthy
```

---

## Vérifier Auto Scaling

```bash
aws autoscaling describe-auto-scaling-groups
```

Résultat attendu :

```text
DesiredCapacity: 2
HealthyInstances: 2
```

---

## Vérifier RDS

```bash
aws rds describe-db-instances
```

Statut attendu :

```text
available
```

---

# 12. Test applicatif

Flux de validation :

```text
Browser

 ↓

ALB DNS

 ↓

EC2 Application Server

 ↓

RDS MySQL
```

Résultat attendu :

* Application accessible
* Instances Healthy
* Connexion base fonctionnelle

---

# 13. Suppression de l'infrastructure

Ordre inverse :

```text
Monitoring

↓

RDS

↓

ALB + ASG

↓

Launch Template

↓

Security Groups

↓

VPC
```

Suppression exemple :

```bash
aws cloudformation delete-stack \
--stack-name production-alb-asg
```

---

# Conclusion

Ce guide permet de déployer une architecture AWS 3-Tier complète, reproductible et sécurisée en utilisant CloudFormation comme outil Infrastructure as Code.
