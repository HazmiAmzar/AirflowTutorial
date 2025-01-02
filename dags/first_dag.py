from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner' : 'hazmi',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2)
}


with DAG(
    dag_id = 'first_dag',
    default_args=default_args,
    description= 'first dag for github that i write on 2/1/2025',
    start_date=datetime(2025, 1, 2, 2),
    schedule_interval= '@daily'
) as dag:
    
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command = 'echo hello world, this is my first task'
    )
    task1
