from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql import SparkSession
import json

from pyspark.sql.functions import col, regexp_replace, lower, trim,max

import pyspark.sql.functions  as f

ss = SparkSession.builder\
    .appName("data_cleam")\
     .getOrCreate()

if ss:
    print(ss.sparkContext.appName)
else:
    print('Could not initialise pyspark session')

df = ss.read.json('hdfs://localhost:9000/user/data/')


clean_data = df.select(col("data.author_id").alias("author_id"),
col("data.created_at").alias("tweet Time"),
col("data.id").alias("id"),
col("data.public_metrics.retweet_count").alias("retweet_count"),
col("data.public_metrics.reply_count").alias("reply_count"),
col("data.public_metrics.like_count").alias("like_count"),
col("data.source").alias("application"),
col("data.text").alias("text"))

# col("data.text").alias("text"))

clean_data= clean_data.withColumn("tweet", regexp_replace("text", r"[@#&][A-Za-z0-9_-]+", " "))\
                   .withColumn("tweet", regexp_replace("tweet", r"\w+:\/\/\S+", " "))\
                   .withColumn("tweet", regexp_replace("tweet", r"[^A-Za-z]", " "))\
                   .withColumn("tweet", regexp_replace("tweet", r"\s+", " "))\
                   .withColumn("tweet", lower(col("tweet")))\
                   .withColumn("tweet", regexp_replace("tweet", r"\brt\b", " "))\
                   .withColumn("tweet", trim(col("tweet")))\
                   .drop("text")
clean_data=clean_data.filter(col("tweet").rlike(r"^(?!^[A-Za-z]+$)."))



clean_data.write.mode("append").csv("/mnt/c/Users/Lenovo/OneDrive/Desktop/twitter_data/twitter", header=True)
