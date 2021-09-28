# Toxic-Comment-Classification
 


The growing demand for the Internet has given rise to social issues such as abusive behaviour which comprises intolerable comments, personal attacks, online harassment, and bullying. It is indispensable to categorize the comments based on toxicity to prevent the bullying on the social network. 
Dealing with toxicity online and curbing harassment has been a growing problem since social media and online conversations have become a part of everyday life. The aim of our project is to detect toxicity in user comments by using machine-learning models. The model will classify comments into 6 types: toxic, severe toxic, obscene, threat, insult, identity hate. In addition, we will explore feasibility of using the model for real time use case where model will classify comments in real time.
Discussion on online fora can often devolve into abuse and harassment due to the anonymity of users. Internet users find it much easier to propagate harmful stereotypes and toxic commentary in comment sections. Platforms often struggle to facilitate conversation effectively forcing many communities to shut down user comments. So, the proposed model help improve online behaviours and minimize toxicity by predicting the level of toxicity of the comments.



## Dataset:


 The data set used for training the model is taken from Kaggle. 
The data set included two files: 
• train.csv - the training set 
• test.csv - the test set 
The training data set contained 159K data points. 
Data Attributes for train.csv 
• id - unique id value for a comment 
• comment text - the comment content 
• toxic - boolean field to indicate toxic 
• severe toxic - boolean field to indicate severe toxic 
• obscene - boolean field to indicate obscene 
• threat - boolean field to indicate threat 
• insult - boolean field to indicate insult 
• identity hate-boolean field to indicate identity hate 


The test data set is the real time twitter data collected for a period of time.
Data Attributes for test.csv 
• id - unique id value for a comment 
• text - the comment content 


## Architecture


![image](https://user-images.githubusercontent.com/74970837/135131453-73ba510e-92d3-420c-af30-98312090bf44.png)


The heart of the project is text classifier, which classifies input text in six levels of toxicity toxic, severe-toxic, obscene, threat, insult, identity hate. Entire architecture can be divided into data ingestion, data classification and report based on data classification. Data ingestion is sub-divided into 3 parts getting data from twitter, ingest data into HDFS and clean ingested data to serve as input for classifier module. Data classification modules classifies input clean data and saves output which is read by Power Bi to give statistics of classification.

Automation of data ingestion, data cleaning and classification is done with airflow to minimize human intervention and serves as pipeline. The twitter stream data is received as stream from internet, which through Kafka serving as data pipe is given to Spark Streaming module, which handles the job saving data in HDFS. The Data Cleaning module reads the data from HDFS to select required columns and clean tweet data, which is saved as clean data to serve as input to classifier. The output of classifier is read by Power BI which displays the statistics like number of toxic comments, non-toxic comments, etc.


## Application of Power BI in our project:

In our project we are using power bi to better understand the predictions made by our model. By just seeing the predictions in table format it is difficult to analyze the result and draw some conclusion out of it.  Power BI is one of the preeminent business intelligence tools to create insightful visualizations and showcase your sentiment analysis results. Power BI offers a number of options to display your results in easy-to-understand format using clustered column chart, funnel chart, pie chart, Tables, word cloud, Scroller etc.  
We are using, pie charts to show how much percentage of comments were toxic and non-toxic, tables with filters to show top 10 retweets, clustered column chart to show number of toxic, severe toxic, identity hate, threat, insult tweets and word cloud for showing textual data and most used words.



![image](https://user-images.githubusercontent.com/74970837/135131888-da7d5453-e014-4ee3-9c74-398c7d2081e3.png)












