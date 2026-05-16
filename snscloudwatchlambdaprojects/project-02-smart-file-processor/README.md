Parfait, je vois exactement le style que tu veux 👍
Je t’ai donc réécrit ton **Projet 02 dans le même format professionnel, structuré et “recruteur-ready”** que ton Projet 01.

---

# 🚀 Projet 02 — Smart File Processor (AWS Serverless)

## 📌 Présentation du projet

Ce projet démontre comment construire un système de traitement de fichiers automatisé sur AWS basé sur une architecture événementielle (Event-Driven Architecture) utilisant :

* Amazon S3
* AWS Lambda (Python 3.12)
* Amazon CloudWatch Logs
* IAM (Identity & Access Management)

Le système permet de traiter automatiquement les fichiers uploadés dans un bucket S3, de valider leur type, de renommer les fichiers images valides, de les déplacer vers un dossier de traitement, et de journaliser toutes les actions dans CloudWatch.

---

# 🎯 Objectifs du projet

Les objectifs de ce projet étaient :

* Comprendre les événements S3 (S3 Event Notifications)
* Créer un pipeline de traitement de fichiers automatisé
* Utiliser AWS Lambda pour le traitement serverless
* Filtrer et valider les types de fichiers
* Automatiser le déplacement des fichiers dans S3
* Implémenter un système de logs structuré
* Appliquer le principe du moindre privilège IAM
* Construire une architecture cloud scalable et automatisée

---

# 🏗️ Architecture

## 📊 Diagramme d’architecture

![Architecture Diagram](architecture/diagram.png)

---

# ⚙️ Services AWS utilisés

| Service AWS       | Rôle                                        |
| ----------------- | ------------------------------------------- |
| Amazon S3         | Stockage des fichiers (uploads & processed) |
| AWS Lambda        | Traitement automatique des fichiers         |
| Amazon CloudWatch | Logs et monitoring des exécutions           |
| IAM               | Gestion des permissions sécurisées          |
| Python boto3      | Interaction avec les services AWS           |

---

# 🔄 Fonctionnement de l’architecture

```text
Utilisateur
     ↓
Upload fichier dans S3 (uploads/)
     ↓
Event S3 déclenche AWS Lambda
     ↓
Lambda valide le type de fichier
     ↓
┌───────────────────────────────┐
│                               │
│  Fichier valide (.jpg/.png)   │ → renommé + déplacé vers processed/
│                               │
│  Fichier invalide             │ → ignoré (SKIPPED)
└───────────────────────────────┘
     ↓
CloudWatch Logs (JSON structuré)
```

---

# 🚀 Fonctionnalités du projet

## ✅ Validation des fichiers

Seuls les formats suivants sont acceptés :

* .jpg
* .jpeg
* .png

---

## ⚡ Traitement automatique

Le système effectue automatiquement :

* Renommage des fichiers avec timestamp
* Déplacement vers le dossier `processed/`
* Suppression du fichier original après traitement

---

## 📊 Logging structuré

Chaque exécution génère un log CloudWatch :

### États possibles :

* **PROCESSED** → fichier traité avec succès
* **SKIPPED** → fichier ignoré (format non supporté)
* **ERROR** → erreur d’exécution ou permission

### Exemple de log :

```json
{
  "action": "PROCESSED",
  "source": "uploads/image.jpg",
  "destination": "processed/image_20260515_180000.jpg",
  "timestamp": "2026-05-15T18:00:00"
}
```

---

# 🔐 Permissions IAM (Important)

Le rôle Lambda doit inclure :

```json
{
  "Effect": "Allow",
  "Action": [
    "s3:ListBucket"
  ],
  "Resource": "arn:aws:s3:::smart-processor"
},
{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "s3:PutObject",
    "s3:DeleteObject"
  ],
  "Resource": "arn:aws:s3:::smart-processor/*"
}
```

Et également :

* AWSLambdaBasicExecutionRole

---

# 🧪 Scénario de test

## ✔️ Test 1 : Fichier valide

Upload :

* .jpg / .png

Résultat :

* fichier déplacé vers `processed/`
* renommage avec timestamp
* log = PROCESSED

---

## ❌ Test 2 : Fichier invalide

Upload :

* .txt / .pdf / .docx

Résultat :

* fichier ignoré
* log = SKIPPED

---

## ⚠️ Test 3 : Erreur IAM

Mauvaise configuration IAM :

Résultat :

* log = ERROR
* AccessDenied dans CloudWatch

---

# 🧠 Concepts clés appris

## Architecture événementielle

Utilisation des événements S3 pour déclencher automatiquement Lambda.

---

## Serverless computing

Traitement sans serveur avec AWS Lambda.

---

## Observabilité Cloud

Utilisation de CloudWatch pour suivre les exécutions.

---

## Automatisation des workflows

Traitement automatique des fichiers sans intervention humaine.

---

## Sécurité IAM

Application du principe du moindre privilège.

---

# 🔥 Concepts professionnels démontrés

* Architecture serverless AWS
* Event-driven architecture
* Automatisation cloud
* Gestion des permissions IAM
* Logging et monitoring
* Pipeline de traitement de fichiers
* Déploiement cloud scalable

---

# ⚠️ Difficultés rencontrées

* Configuration des triggers S3
* Gestion des permissions IAM
* Débogage des erreurs Lambda
* Compréhension des logs CloudWatch
* Synchronisation S3 ↔ Lambda

---

# ✅ Résultat final

Mise en place réussie d’un système AWS capable de :

* détecter automatiquement les uploads S3
* filtrer les fichiers
* traiter et déplacer les images valides
* journaliser toutes les actions dans CloudWatch

---

# 🚀 Améliorations futures

* Ajout de DynamoDB pour tracking des fichiers
* Génération de thumbnails (redimensionnement d’images)
* Notifications SNS en cas d’erreur
* Orchestration avec AWS Step Functions
* Retry automatique des échecs
* Intégration CI/CD avec AWS CodePipeline

---

# 👨‍💻 Auteur

## Aboubacar Camara

Futur AWS Cloud & DevOps Engineer

GitHub :
[https://github.com/Aboubacar-tech](https://github.com/Aboubacar-tech)

---

Si tu veux, prochaine étape je peux te faire :

🔥 une version **ENGLISH parfaite pour recruteurs internationaux**
📊 ou transformer tes 2 projets en **portfolio GitHub complet (homepage + design)**
💼 ou même préparer ton **CV DevOps basé sur ces projets (niveau entretien AWS)**
