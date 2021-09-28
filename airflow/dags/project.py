from airflow.models import DAG
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_kafka import main
from predict import main_predict
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.python import PythonOperator


args = {
    'owner':'Nilesh'
}

dag = DAG(
    dag_id='Project',
    default_args=args,
	start_date=days_ago(1),
    schedule_interval=None,
)

def twitter_start(**kwargs):
	keyword=kwargs['dag_run'].conf.get('Keyword')
	timeout=kwargs['dag_run'].conf.get('time')
	main(keyword)


# def youtube_param(**kwargs):
	# keyword=kwargs['dag_run'].conf.get('link')
	# main_yt(link)
	
twitter_kafka = PythonOperator(
    task_id='Kafka_twitter_Stream',
	provide_context=True,
    python_callable=twitter_start,
	#op_kwargs={context["Keyword"],context["time"]},
    dag=dag
)

predict_twitter = PythonOperator(
    task_id='twitter_predict',
    python_callable=main_predict,
    dag=dag
)
# youtube = PythonOperator(
    # task_id='yotube_predict',
	# provide_context=True,
    # python_callable=youtube_param,
    # dag=dag
# )


kafka_spark=SparkSubmitOperator(
    task_id='kafka_spark',
    #name="airflow-spark",
    application='/home/nilu/project/spark_kafka.py',
    env_vars={'PYSPARK_DRIVER_PYTHON':'python3', 'HADOOP_CONF_DIR':'$HADOOP_HOME/etc/hadoop', 'PYSPARK_PYTHON':'/usr/bin/python3'}, 
	packages= "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2",
    dag=dag
)

data_clean=SparkSubmitOperator(
    task_id='data_clean',
    #name="airflow-spark",
    application='/home/nilu/project/data_clean.py',
    env_vars={'PYSPARK_DRIVER_PYTHON':'python3', 'HADOOP_CONF_DIR':'$HADOOP_HOME/etc/hadoop', 'PYSPARK_PYTHON':'/usr/bin/python3'}, 
    dag=dag
)

#if {{ params }}['key']==0:
[twitter_kafka,kafka_spark]>>data_clean>>predict_twitter
#else:
#	youtube
