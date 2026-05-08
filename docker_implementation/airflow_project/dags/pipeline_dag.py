from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'usaid',
    'start_date': datetime(2024, 1, 1),
    'retries': 2,
}

dag = DAG(
    'data_pipeline_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

fetch_data = BashOperator(
    task_id='fetch_data',
    bash_command='python /opt/airflow/scripts/fetch_api_data.py',
    dag=dag
)

clean_data = BashOperator(
    task_id='clean_data',
    bash_command='python /opt/airflow/scripts/clean_data.py',
    dag=dag
)

load_data = BashOperator(
    task_id='load_data',
    bash_command='python /opt/airflow/scripts/load_to_mysql.py',
    dag=dag
)
fetch_data >> clean_data >> load_data
