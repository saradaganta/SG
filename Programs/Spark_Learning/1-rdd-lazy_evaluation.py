# Transformations are not executed immediately. Instead they executed when action is called.
import os
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("lazy").getOrCreate()

rdd = spark.sparkContext.parallelize([1,2])
new_rdd = rdd.map(lambda x : x+2)
print(new_rdd)

print(new_rdd.collect())