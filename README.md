# 🚀 FAANG-Level Data Engineering Project

## 📌 Overview
This project implements an end-to-end data pipeline using PySpark and Delta Lake with Medallion Architecture.

## 🏗️ Architecture
- Bronze Layer: Raw data ingestion
- Silver Layer: Data cleaning and transformation
- Gold Layer: Data modeling (Fact & Dimension tables)
- SCD Type 2: Historical tracking of customer changes

## ⚙️ Tech Stack
- PySpark
- Delta Lake
- Apache Airflow
- Streamlit

## 📊 Features
- Incremental data processing
- Slowly Changing Dimensions (Type 2)
- Star schema data modeling
- Automated workflows using Airflow
- Interactive dashboard

## 🚀 How to Run

pip install -r requirements.txt

python pyspark/bronze_layer.py
python pyspark/silver_layer.py
python pyspark/scd_type2.py
python pyspark/gold_layer.py

streamlit run dashboard/app.py

## 🎯 Future Improvements
- Kafka streaming
- Cloud deployment (AWS/GCP)
- Partitioning optimization