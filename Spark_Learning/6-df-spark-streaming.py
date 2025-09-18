from hmac import digest

from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
import random
import string

# Spark Session initialize
spark = SparkSession.builder.appName("Spark_Streaming").getOrCreate()

###########*************************************################
# Data Velocity (Speed) :

# Batch :
# Periodic :
# Near Real Time (Interval): Spark Streaming will support.
#################*********************************##############

# Spark streaming initialize
ssc = StreamingContext(spark.sparkContext, 3)
rddQueue = []

for i in range(3) :
    data = ["Hello", "MY", "Beautiful", "World"]
    # data = list(map(lambda x : x+random.choice(string.ascii_letters + string.digits, string.punctuation), data))
    rddQueue  += [spark.sparkContext.parallelize(data)]

# 3 rdds created.
dstream = ssc.queueStream(rddQueue)

# split each line into words and count their occurrences
wordsCount = dstream.flatMap(lambda line : line.split(" "))\
                    .map(lambda word : (word, 1))\
                    .reduceByKey(lambda x, y : x+y)
wordsCount.pprint()

ssc.start()
ssc.awaitTermination()
ssc.stop()