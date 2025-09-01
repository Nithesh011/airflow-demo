from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def get_current_date():
    return datetime.now()

def process_date(ti):
    c=ti.xcom_pull(task_id="push_date")
    print(f"Today's date is : {c}")

args={"owner":"airflow","start_date":datetime(2025,8,30),"retries":1,"depends_on_past":False,
    "retry_delay":timedelta(seconds=10),}

with DAG(
     dag_id="demo_Xcom",
     schedule_interval=None,
     default_args=args,
     catchup=False,
     )as dag:
     
     push_date=PythonOperator(
         task_id="push_date",
         python_callable=get_current_date
     )
     
     pull_date=PythonOperator(
         task_id="pull_date",
         python_callable=process_date
     )
     
     another_way=BashOperator(
             task_id="bash_way",
             bash_command="echo Today\'s date is {{ti.xcom_pull(task_ids='push_date')}}"
     )

push_date >> pull_date >> another_way
      
     
     
     
     
     
