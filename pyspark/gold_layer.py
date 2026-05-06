from pyspark.sql import SparkSession

# Spark with Delta
spark = SparkSession.builder \
    .appName("Gold Layer") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# ---------------------------
# READ SILVER (DELTA)
# ---------------------------

orders = spark.read.format("delta").load("silver/orders")
customers = spark.read.format("delta").load("silver/customers")
products = spark.read.format("delta").load("silver/products")

# ---------------------------
# DIMENSION TABLES
# ---------------------------

dim_customer = customers.select(
    "customer_id",
    "name",
    "city",
    "state"
)

dim_product = products.select(
    "product_id",
    "product_name",
    "category",
    "price"
)

# ---------------------------
# FACT TABLE
# ---------------------------

fact_orders = orders.select(
    "order_id",
    "customer_id",
    "product_id",
    "amount",
    "quantity",
    "order_date"
)

# ---------------------------
# WRITE DIM + FACT (DELTA)
# ---------------------------

dim_customer.write.format("delta").mode("overwrite").save("gold/dim_customer")
dim_product.write.format("delta").mode("overwrite").save("gold/dim_product")
fact_orders.write.format("delta").mode("overwrite").save("gold/fact_orders")

# ---------------------------
# ANALYTICS LAYER
# ---------------------------

final_df = fact_orders \
    .join(dim_customer, "customer_id") \
    .join(dim_product, "product_id")

# Revenue by City
sales_by_city = final_df.groupBy("city").sum("amount")

# Revenue by Category
sales_by_category = final_df.groupBy("category").sum("amount")

# Daily Sales
daily_sales = final_df.groupBy("order_date").sum("amount")

# ---------------------------
# SAVE ANALYTICS
# ---------------------------

sales_by_city.write.format("delta").mode("overwrite").save("gold/sales_by_city")
sales_by_category.write.format("delta").mode("overwrite").save("gold/sales_by_category")
daily_sales.write.format("delta").mode("overwrite").save("gold/daily_sales")

print("Gold Layer Created Successfully")
