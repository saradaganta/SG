# Actions
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Actions").getOrCreate()



rdd = spark.sparkContext.parallelize([1,2,3,4,5,6,7,8,9])
# Collect - Shows output of all results from rdd. Use for small set of data.
print("***** collect ****")
print(rdd.collect())

# Count - returns number of elements
print("***** count ****")
print(rdd.count())

# take - returns first n number of elements
print("***** take ****")
print(rdd.take(7))

# first - returns first element
print("***** first ****")
print(rdd.first())

# foreach() - take every element and print in loop
print("***** foreach ****")
rdd.foreach(lambda x : print(x))

# reduce - group all elements and perform action (eg : Sum, Avg..etc)
print("***** reduce ****")
print(rdd.reduce(lambda x, y : x + y))

# save as - save at destination
print("***** save as ****")
rdd.saveAsTextFile("/Users/sg/Project/PySpark_Learning/PycharmProjects/save_as_eg.rtf")