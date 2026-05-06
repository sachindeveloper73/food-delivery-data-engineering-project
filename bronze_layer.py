from pyspark.sql import SparkSession

# Create Spark Session with Delta Support
spark = SparkSession.builder \
    .appName("Bronze Layer") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# ---------------------------
# READ RAW DATA
# ---------------------------

orders = spark.read.csv("data/raw/orders.csv", header=True, inferSchema=True)
customers = spark.read.csv("data/raw/customers.csv", header=True, inferSchema=True)
products = spark.read.csv("data/raw/products.csv", header=True, inferSchema=True)

# ---------------------------
# WRITE TO BRONZE (DELTA FORMAT)
# ---------------------------

orders.write.format("delta").mode("overwrite").save("bronze/orders")
customers.write.format("delta").mode("overwrite").save("bronze/customers")
products.write.format("delta").mode("overwrite").save("bronze/products")

print("Bronze Layer Created Successfully")