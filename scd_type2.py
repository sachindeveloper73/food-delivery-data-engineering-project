from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date, lit
from delta.tables import DeltaTable

# ---------------------------
# SPARK WITH DELTA
# ---------------------------

spark = SparkSession.builder \
    .appName("SCD Type 2") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# ---------------------------
# LOAD SOURCE (SILVER)
# ---------------------------

source_df = spark.read.format("delta").load("silver/customers")

# Add metadata columns