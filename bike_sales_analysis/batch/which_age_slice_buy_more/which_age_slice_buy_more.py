from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, desc

# Initialiser la session Spark
spark = SparkSession.builder \
    .appName("WhichAgeSliceBuyMore") \
    .getOrCreate()

# Lire les données depuis HDFS
df = spark.read.csv("hdfs://hadoop-master:9000/input/Sales.csv", header=True, inferSchema=True)

# Afficher le schéma pour vérifier les colonnes
df.printSchema()

# Calculer le nombre total d'achats par tranche d'âge
buy_by_age_slice = df.groupBy("Age_Group").agg(_sum(col("Unit_Price") * col("Order_Quantity")).alias("total_purchases"))
buy_by_age_slice.show()

# Trouver la tranche d'âge avec le plus d'achats
max_purchases_age_group = buy_by_age_slice.orderBy(desc("total_purchases")).first()

# Convertir la ligne en DataFrame
max_purchases_age_group_df = spark.createDataFrame([max_purchases_age_group])
max_purchases_age_group_df.show()

# Définir les propriétés de connexion PostgreSQL
jdbc_url = "jdbc:postgresql://bike_postgres:5432/bike_db"
connection_properties = {
    "user": "postgres",
    "password": "secret",
    "driver": "org.postgresql.Driver"
}

# Écrire le DataFrame dans PostgreSQL
try:
    max_purchases_age_group_df.write.jdbc(url=jdbc_url, table="age_group_purchases", mode="append", properties=connection_properties)
    print("Data written successfully to age_group_purchases table.")
except Exception as e:
    print(f"Error writing data to PostgreSQL: {e}")

# Arrêter la session Spark
spark.stop()