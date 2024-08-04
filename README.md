# Ventes de vélos en Europe

![Docker](https://img.shields.io/badge/Docker-blue) ![Bash](https://img.shields.io/badge/Bash-lightgrey) ![Python](https://img.shields.io/badge/Python-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-green) ![Spark](https://img.shields.io/badge/Spark-orange) ![Kafka](https://img.shields.io/badge/Kafka-brown) ![Hadoop](https://img.shields.io/badge/Hadoop-yellow) ![Grafana](https://img.shields.io/badge/Grafana-red) 

<p align="center">
  <img src="./docs/screenshot-dashboard.png" alt="Screenshot du dashboard Bike Sales">
  <br>
  <em>Screenshot du dashboard Bike Sales</em>
</p>

## Source de donnée

[Dataset des ventes de vélos en Europe](https://www.kaggle.com/datasets/sadiqshah/bike-sales-in-europe)

Ce dataset offre des données structurées, idéales pour nos besoins en traitement batch et streaming.

## Objectif

### Analyser un fichier de ventes

Voici une liste de question que nous voulons aborder:

1. Quel est le revenu réalisé pour chaque catégorie de produit ?
2. Quel est le revenu réalise pour chaque sous-catégorie de produit ?
3. Quel est le top 20 des produits générant le plus de revenu ?
4. Un top 10 des produits générant le plus de revenu en France ?
5. Quel tranche d'âge de client réalise le plus d'achats ?

## Lancement

### Mise en place et lancement du projet

```bash
source init.sh #ou ./init.sh
```

#### Détails du script:

- Pull l'image du cluster hadoop
- Lancer le docker compose contenant notre base de donnée PostgreSQL et le setup de l'application Grafana
- Déplacer les scripts Spark et les fichiers à traiter vers le cluster hadoop
- Lancer les scripts et alimenter la base de donnée

<p align="center">
  <img src="./docs/schema-architecture.png" alt="Schéma de l'architecture">
  <br>
  <em>Schéma de l'architecture (voir le détails dans le dossier tp00-pipeline-architecture)</a></em>
</p>

#### Visualiser les données traitées

Enfin, veuillez vous rendre sur http://localhost:3000d/ddtc9zkmxla80e/bike-sales-analytics?orgId=1 et vous connecter sur Grafana (username: admin, password: admin) afin d'avoir la visualisation des [questions](#objectif).


## Ressources

- L'image initial du cluster hadoop vient du [TP BigData de l'Ecole Centrale de Lyon](https://gitlab.ec-lyon.fr/sderrode/TP_BigData_ECL) proposé par Stéphane DERRODE.
- [Documentation pySpark]()
- [Documentation Grafana]()

## Groupe

- Faustine CHARRIER
- Mattis ALMEIDA LIMA
- Louisan TCHITOULA
- Djédjé GBOBLE
- Julien HEITZ
