from datetime import datetime
import os

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.dummy_operator import DummyOperator
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020,8,1),
    'retries': 0,
}


with DAG('1_init_once_seed_data', default_args=default_args, schedule_interval='@once') as dag:
    task_1 = BashOperator(
        task_id='load_seed_data_once',
        #bash_command='cd',
        bash_command='cd /opt/airflow/dbt && sudo dbt deps && sudo dbt seed --profiles-dir .',
        env={
            'DBT_USER': os.getenv('DBT_USER'),
            'DBT_PASSWORD': os.getenv('DBT_PASSWORD'),
            'SNOWFLAKE_ACCOUNT': os.getenv('SNOWFLAKE_ACCOUNT'),
            **os.environ
        },
        dag=dag
    )

task_1  