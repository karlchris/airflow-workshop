# Airflow Workshop

This is very simple repo structure of airflow.

## Steps to run Airflow:
- run ```docker-compose up airflow-init```
  The account created has the login `airflow` and the password `airflow`.
- run ```docker-compose up``` to start the Airflow services.
- The webserver is available at: http://localhost:8080. The default account has the login `airflow` and the password `airflow`.

## Google BigQuery
- go to this [url](https://console.cloud.google.com/projectselector2/home/dashboard?_ga=2.189591977.383272846.1656521391-950865466.1656521391)
- login with your gmail.
- your first project ID will be created.

## Add GCP connections
- Go to `Admin` tab above and choose `Connections`.
- click on plus sign to create one.
- fill `Connection ID` with `google_cloud_default`.
- choose `Connection Type` to `Google Cloud`.
- copy JSON key from GCP IAM, put it in `Keyfile JSON` box.
- connection is ready.

## Add DAG
- go to [dags](https://github.com/karlchris/airflow-workshop/tree/main/dags) to put your pipeline python script.
- put the sql files in [dags/sql/](https://github.com/karlchris/airflow-workshop/tree/main/dags/sql).
- if you want to have some default functions, commonly called `utils`, you can put [dags/utils/](https://github.com/karlchris/airflow-workshop/tree/main/dags/utils)
- your added DAG will show in airflow UI shortly.
