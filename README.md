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

### Mise en place de la base de donnée

1. 

TODO: [Set up du cluster Hadoop](https://gitlab.ec-lyon.fr/sderrode/TP_BigData_ECL)

```bash
# In local terminal
cd bike_sales_analysis
docker cp Sales_extract100.csv hadoop-master:/root/sales
```

```bash
# In hadoop-master container terminal
hdfs dfs -mkdir input
hdfs dfs -put sales/Sales.csv input
```

## Groupe

- Faustine CHARRIER
- Mattis ALMEIDA LIMA
- Louisan TCHITOULA
- Djédjé GBOBLE
- Julien HEITZ
