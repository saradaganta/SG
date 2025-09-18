from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("sql Operations").getOrCreate()
from pyspark.sql.functions import lit, concat

df1 = spark.read.option("header", True).option("delimiter", ",").csv("/Users/sg/Project/PySpark_Learning/PycharmProjects/userdata1.csv")

df1.show(5, True)

# df to CSV
# df1.coalesce(1).write.mode("append").option("header", True).option("delimiter", "|").csv("/Users/sg/Project/PySpark_Learning/PycharmProjects/targets/")
# df1.coalesce(1).write.mode("overwrite").csv("/Users/sg/Project/PySpark_Learning/PycharmProjects/targets/")

# Header = True (default = false) (only for CSV)
# delimiter = ("|", "   ", etc..) default = "," (only for CSV)
# Control files creation.
# no of partitions  = no of files

# overwrite existing file
# default behaviour = throws error(files already exist exception)
# mode("append") = add records to existing data
# mode("overwrite") = delete existing file and re-write new file

# df to parquet
df1.coalesce(1).write.mode("append").parquet("/Users/sg/Project/PySpark_Learning/PycharmProjects/targets/")

# df to ORC
df1.coalesce(1).write.mode("append").orc("/Users/sg/Project/PySpark_Learning/PycharmProjects/targets/")

# df to json
df1.coalesce(1).write.mode("append").json("/Users/sg/Project/PySpark_Learning/PycharmProjects/targets/")
