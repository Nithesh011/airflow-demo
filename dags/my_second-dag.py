from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator

default_args = {
    'owner': 'nithesh',
    'start_date': datetime(2023, 1, 1),
    'retries': 3,
}

def my_hello_function():
    print("Hello, Nithesh!")

with DAG(
    dag_id='my_dag_with_defaults',
    default_args=default_args,
    schedule_interval='@yearly',
    catchup=False
) as dag:

    task_1 = PythonOperator(
        task_id="print_my_name",
        python_callable=my_hello_function,
    )

    task_2 = PythonOperator(
        task_id="just_for_fun",
        python_callable=my_hello_function,
    )
    
    date_task=BashOperator(
        task_id="print_current_date&time",
        bash_command="echo {{ds}}"
    )
    #date than (ds)
        #bash_command="echo 'Airflow DS: {{ ds }}' && date"
     
    send_success_email = EmailOperator(
    task_id='send_success_email',
    to='my.team@example.com',
    subject='Data Processing Job Completed',
    html_content='The daily data job has finished successfully!'
)
task_1 >> task_2 >> date_task >> send_success_email

