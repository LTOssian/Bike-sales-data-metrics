# TP00 - Architecture Pipeline: Ventes de Vélos en Europe

## Schéma

![Schéma de l'Architecture](../docs/schema-architecture.png)

## Choix du Dataset

Nous avons choisi un dataset de "Bike Sales in Europe" disponible sur Kaggle. Ce dataset offre des données structurées, idéales pour nos besoins en traitement batch et streaming.

## Détails de l'Architecture

### Ingestion des Données

- **Hadoop (HDFS)** : Utilisé pour stocker les données batch initiales.
- **Kafka** : Utilisé pour capturer les données en streaming. Les ventes de vélos en temps réel seront simulées avec un script Python.

### Traitement des Données avec Spark

#### Batch Processing avec Spark

1. Lecture des données depuis HDFS.
2. Traitement (nettoyage, transformation) des données avec Spark.
3. Écriture des données traitées dans PostgreSQL.

#### Streaming Processing avec Spark Streaming

1. Lecture des données en temps réel depuis Kafka.
2. Traitement en temps réel des données (nettoyage, transformation) avec Spark Streaming.
3. Écriture des résultats en temps réel dans PostgreSQL.

### Visualisation

- **Grafana** : Connexion à PostgreSQL pour créer des dashboards interactifs.

## Conclusion

Ce projet illustre comment intégrer différentes technologies pour gérer et traiter des flux de données en temps réel et en batch, puis visualiser les résultats de manière efficace. Grâce à l'utilisation de Hadoop, Kafka, Spark, PostgreSQL et Grafana, nous pouvons obtenir une architecture robuste et évolutive pour le traitement des données de ventes de vélos en Europe.
