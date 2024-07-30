# Ventes de vélos en Europe

## Source de donnée

[Dataset des ventes de vélos en Europe](https://www.kaggle.com/datasets/sadiqshah/bike-sales-in-europe)

Ce dataset offre des données structurées, idéales pour nos besoins en traitement batch et streaming.

## Objectif

L'objectif est de questionner le fichier de vente.
Voici une liste de question que nous voulons aborder:

1. Quel est le revenu réalisé pour chaque catégorie de produit ?
2. Quel est le revenu réalise poru chaque sous-catégorie de produit ?
3. Quel est le top 20 des produits générant le plus de revenu ?
4. Un top 10 des produits générant le plus de revenu en France ?
5. Quel tranche d'âge de client réalise le plus d'achats ?

## Lancement

### Mise en place du projet

```bash
source init.sh #ou ./init.sh
```

### Lancer le script 01 -> Revenu par catégories

```bash
# Mettre en place le script dans le container
docker cp bike_sales_analysis/batch/revenue_per_category/revenue_per_category.py hadoop-master:/root/sales
```

```bash
# Lancer le job
# Alimenter la table revenue par catégorie
spark-submit --jars /opt/spark/jars/postgresql-42.7.3.jar ./sales/revenue_per_category.py

# Alimenter la table top 10 produits france
spark-submit --jars /opt/spark/jars/postgresql-42.7.3.jar ./sales/top_10_products_france.py
```

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
