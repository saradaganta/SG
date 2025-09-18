# wordcount programme
print("*** wordcount Programme ***")
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("wordcount").getOrCreate()
# read file
rdd = spark.sparkContext.textFile("/Users/sg/Project/PySpark_Learning/PycharmProjects/wordcount_input.rtf")
print(rdd.collect())
# split words
fm_rdd = rdd.flatMap(lambda x : x.split(" "))
print(fm_rdd.collect())
# assign 1 to each word
map_rdd = fm_rdd.map(lambda x : (x, 1))
print(map_rdd.collect())
# grouping same words using reducedByKey
grp_rdd = map_rdd.reduceByKey(lambda x, y : x + y)
print(grp_rdd.collect())

# Write all the above code in oneline
# flatmap, map, reducedByKey, collect
print("*** all the above code in one line ***")
new_rdd = rdd.flatMap(lambda x : x.split(" ")).map(lambda x : (x, 1)).reduceByKey(lambda x, y : x + y)
print(new_rdd.collect())

