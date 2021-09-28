import os
import time
from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import get_json_object


ss = SparkSession.builder\
     .appName("Kafka_tweet")\
     .getOrCreate()

if ss:
    print(ss.sparkContext.appName)
else:
    print('Could not initialise pyspark session')



df = ss.readStream\
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("startingOffsets","latest")\
    .option("subscribe", "twitter") \
    .load()

df.printSchema()

trainData = df.selectExpr('CAST(value AS STRING)')





query=trainData.writeStream.outputMode('append').format("text")\
    .trigger(processingTime='30 seconds')\
    .option("path","hdfs://localhost:9000/user/data/")\
    .option("checkpointLocation", "hdfs://localhost:9000/user/chk")\
    .start()


time.sleep(2800) 

while query.isActive:
    if query.lastProgress:
        while query.status['isDataAvailable']:
            print(query.status['isDataAvailable'])
            pass
        # print(query.lastProgress)
        break
# qy.awaitTermination(60)
sc = ss.sparkContext
hdfsConf=sc._jsc.hadoopConfiguration()
hdfsConf.set("fs.defaultFS","hdfs://localhost:9000")
fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(hdfsConf)
fs.exists(sc._jvm.org.apache.hadoop.fs.Path("hdfs://localhost:9000/user/chk"))
fs.delete(sc._jvm.org.apache.hadoop.fs.Path("hdfs://localhost:9000/user/chk"), True)
ss.stop()
