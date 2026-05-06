from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    'pipeline',
    start_date=datetime(2024,1,1),
    schedule_interval='@daily',
    catchup=False
)

t1 = BashOperator(
    task_id='bronze',
    bash_command='python pyspark/bronze_layer.py',
    dag=dag
)

t2 = BashOperator(
    task_id='silver',
    bash_command='python pyspark/silver_layer.py',
    dag=dag
)

scd = BashOperator(
    task_id='scd',
    bash_command='python pyspark/scd_type2.py',
    dag=dag
)

t3 = BashOperator(
    task_id='gold',
    bash_command='python pyspark/gold_layer.py',
    dag=dag
)

# Correct pipeline flow
t1 >> t2 >> scd >> t3