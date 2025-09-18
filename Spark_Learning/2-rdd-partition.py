# Small chunks of data stored and processed on single node. User can define partitions
import os
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("lazy").getOrCreate()
print("**** repartition ****")
rdd = spark.sparkContext.parallelize([1,2,3,4,5,6,7,8,9])
print(rdd.getNumPartitions())

new_rdd = rdd.repartition(20)
print(new_rdd.getNumPartitions())

# repartition() - can increase or decrease the partition
# coalesce() - only to decrease the partition
print("***** coalesce partitions *****")
# Below two examples coalesce can only decrease partitions
rdd_col = rdd.coalesce(40)
print(rdd_col.getNumPartitions())

rdd_col1 = rdd.coalesce(10)
print(rdd_col1.getNumPartitions())