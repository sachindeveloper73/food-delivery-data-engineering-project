from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

# Spark with Delta
spark = SparkSession.builder \
    .appName("Silver Layer") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# ---------------------------
# READ BRONZE (DELTA)
# ---------------------------

orders = spark.read.format("delta").load("bronze/orders")
customers = spark.read.format("delta").load("bronze/customers")
products = spark.read.format("delta").load("bronze/products")

# ---------------------------
# CLEAN ORDERS
# ---------------------------

orders_clean = orders.dropDuplicates()

orders_clean = orders_clean.filter(col("amount") > 0)

orders_clean = orders_clean.withColumn(
    "order_date",
    to_date(col("order_date"))
)

# ---------------------------
# CLEAN CUSTOMERS
# ---------------------------

customers_clean = customers.dropDuplicates()

customers_clean = customers_clean.fillna({
    "city": "Unknown",
    "state": "Unknown"
})

# ---------------------------
# CLEAN PRODUCTS
# ---------------------------

products_clean = products.dropDuplicates()

products_clean = products_clean.filter(col("price") > 0)

# ---------------------------
# WRITE TO SILVER (DELTA)
# ---------------------------

orders_clean.write.format("delta").mode("overwrite").save("silver/orders")
customers_clean.write.format("delta").mode("overwrite").save("silver/customers")
products_clean.write.format("delta").mode("overwrite").save("silver/products")

print("Silver Layer Created Successfully")
