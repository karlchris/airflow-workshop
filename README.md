# Airflow Workshop

This is very simple repo structure of airflow.

## Steps to run Airflow:
- run ```docker-compose up airflow-init```
  The account created has the login `airflow` and the password `airflow`.
- run ```docker-compose up``` to start the Airflow services.
- The webserver is available at: http://localhost:8080. The default account has the login `airflow` and the password `airflow`.

## Add DAG
- go to [/dags](https://github.com/karlchris/airflow-workshop/tree/main/dags) to put your python script.
- 
