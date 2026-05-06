# 🚀 Food Delivery Data Engineering Pipeline

## 📌 Overview
End-to-end data pipeline using PySpark, Delta Lake, and Airflow.

## 🏗️ Architecture
- Bronze → Raw ingestion
- Silver → Data cleaning
- Gold → Fact & Dimension tables
- SCD Type 2 → Historical tracking

## ⚙️ Tech Stack
- PySpark
- Delta Lake
- Apache Airflow
- Streamlit

## 📂 Data Setup
Place CSV files in:
data/raw/

Files:
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
