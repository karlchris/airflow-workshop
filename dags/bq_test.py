import datetime
import logging

from airflow import models
from airflow.providers.google.cloud.operators import bigquery
from airflow.operators.dummy_operator import DummyOperator


today_date = datetime.datetime.now().strftime("%Y%m%d")
table_name = 'airflow_test.random_table'
yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time()
)
location = 'US'

default_dag_args = {
    # Setting start date as yesterday starts the DAG immediately when it is
    # detected in the Cloud Storage bucket.
    'start_date': yesterday,
    # To email on failure or retry set 'email' arg to your email and enable
    # emailing here.
    'email_on_failure': False,
    'email_on_retry': False,
    # If a task fails, retry it once after waiting at least 5 minutes
    'retries': 0,
    'retry_delay': datetime.timedelta(minutes=5),
    'project_id': 'test-project-karl'
}

with models.DAG(
    dag_id='airflow_test_karl',
    # Continue to run DAG once per day
    schedule_interval=datetime.timedelta(days=1),
    default_args=default_dag_args
) as dag:

    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')

    logging.error('trying to bq_query: ')
    logging.error('table name: ' + table_name)

    sql = """ SELECT 1 as val """

    bq_query = bigquery.BigQueryInsertJobOperator(
        task_id="bq_query",
        configuration={
            "query": {
                "query": sql,
                "useLegacySql": False,
                "destinationTable": {
                    "projectId": "test-project-karl",
                    "datasetId": "airflow_test",
                    "tableId": "random_table",
                }
            }
        },
        location=location,
    )

start >> bq_query >> end
