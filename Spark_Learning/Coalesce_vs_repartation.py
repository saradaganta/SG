import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import rand

spark = (SparkSession.builder
         .appName("RepartitionVsCoalesceDemo")
         .getOrCreate())

# Create a DataFrame with 10 million rows
df = spark.range(0, 10_000_000).withColumn("rand_col", rand())

print("Initial partitions:", df.rdd.getNumPartitions())

# Measure repartition timing
start = time.time()
df_repart = df.repartition(200)
df_repart.count()   # force execution
print("Repartition partitions:", df_repart.rdd.getNumPartitions(),
      " Time:", round(time.time() - start, 2), "seconds")

# Measure coalesce timing
start = time.time()
df_coalesce = df.coalesce(10)
df_coalesce.count()  # force execution
print("Coalesce partitions:", df_coalesce.rdd.getNumPartitions(),
      " Time:", round(time.time() - start, 2), "seconds")