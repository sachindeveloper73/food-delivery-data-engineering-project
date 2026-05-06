# 🚀 Food Delivery Data Engineering Pipeline

## 📌 Overview
End-to-end data pipeline using PySpark, Delta Lake, and Airflow with Medallion Architecture.

## 🏗️ Architecture
Bronze → Silver → SCD → Gold → Dashboard
## 🏗️ Architecture Diagram

![Architecture](Architecturediagram.png)


## ⚙️ Tech Stack
- PySpark
- Delta Lake
- Apache Airflow
- Streamlit

## 📂 Data Setup
Place CSV files inside:

data/raw/

Required files:
- customers.csv
- orders.csv
- products.csv

## 🚀 How to Run

```bash
pip install -r requirements.txt

python pyspark/bronze_layer.py
python pyspark/silver_layer.py
python pyspark/scd_type2.py
python pyspark/gold_layer.py

streamlit run dashboard/app.py
