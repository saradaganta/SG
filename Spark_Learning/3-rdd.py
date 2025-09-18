# Resilient Distributed Dataset. In Spark rdd and transformations are immutable(Cannot modify)
import os
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("learn_rdd").getOrCreate()

#Immutable/mutable
Alist = [0,1,2,3,4,5,6,7,8,9]
print("*******Alist******")
print(Alist)
Alist.remove(0)
print("*******mutable******")
print(Alist)

rdd = spark.sparkContext.parallelize([0,1,2,3,4,5,6,7,8,9])
print(rdd.collect())
print("******immutable******")
rdd.filter(lambda x : x != 0)
print(rdd.collect())

#rdd : Multiple ways to create rdd
# List to rdd
print("******datatype before rdd******")
my_list = ["siva", "gurram"]
print(type(my_list))

my_rdd = spark.sparkContext.parallelize(my_list)
print("****datatype after rdd***")
print(my_rdd.collect())
print(type(my_rdd))

# File to rdd
file_rdd = spark.sparkContext.textFile("/Users/sg/Project/PySpark_Learning/spark_defaults.rtf")
print("*****read-file****")
print(type(file_rdd))
print(file_rdd.collect())

#rdd to new_rdd
rdd = spark.sparkContext.parallelize([0,1,2,3,4,5,6,7,8,9,10])
print("****rdd*****")
print(rdd.collect())

new_rdd = rdd.filter(lambda x : x >= 3)
print("****new_rdd****")
print(new_rdd.collect())

#df to rdd

df = spark.read.text("/Users/sg/Project/PySpark_Learning/spark_defaults.rtf")
my_rdd = df.rdd
print("****df_rdd data type****")
print(type(my_rdd))

#emptyrdd
my_rdd = spark.sparkContext.emptyRDD()
print("*****empty rdd type****")
print(my_rdd.collect())
print(type(my_rdd))
