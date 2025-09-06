#branching and join in airflow code 
from airflow import DAG
from airflow.operators.python import PythonOperator,BranchPythonOperator
from datetime import datetime,timedelta
from airflow.operators.empty import EmptyOperator
def check_number_parity():
    num=7
    if num % 2 ==0:
       return "even_task"
    else:
       return "odd_task"
       
def print_even ():
    print("The number is even")
       
       
def print_odd ():
    print("The number is odd")

args={'owner':'I am',
      'depends_on_past':False,
      'start_date':datetime(2025,8,30),
      'retries':2,
      'retry_delay':timedelta(seconds=10),}
      
      
with DAG(
      "branching_dag",
      schedule_interval="@daily",
      catchup=False,
      default_args=args,
      ) as dag:
      
      start=EmptyOperator(task_id="start")
      
      branch=BranchPythonOperator(task_id='branch_task',
             python_callable=check_number_parity)
             
      even_task=PythonOperator(task_id="even_task",
                python_callable=print_even)
      
      odd_task=PythonOperator(task_id="odd_task",
               python_callable=print_odd)
       
      finished_task=EmptyOperator(task_id="Tasks_are_succeeded",
               trigger_rule="all_done")

start >> branch >> [even_task,odd_task] >> finished_task
      
