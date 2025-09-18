from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("sql Operations").getOrCreate()
from pyspark.sql.functions import lit, concat

df1 = spark.read.option("header", True).option("delimiter", ",").csv("/Users/sg/Project/PySpark_Learning/PycharmProjects/userdata1.csv")
df2 = spark.read.option("header", True).option("delimiter", ",").csv("/Users/sg/Project/PySpark_Learning/PycharmProjects/userdata1.csv")

df1.printSchema()

df1.show(5, True)
df2.show(5, True)
"""
# ***************************** Distinct ***********************************************************************
# Distinct - union to get dups first to show distinct
union_df = df1.union(df2)
union_df.orderBy("id").show(10, False)

# Distinct
dist_df = union_df.distinct()
dist_df.orderBy("id").show(10, False)

# Drop Duplicates
dd_df = union_df.drop_duplicates()
dd_df.orderBy("id").show(10, False)
"""
# ******************** NULL handing ****************************************************************************
"""
# On whole table
null_df = df1.na.fill("")
null_df.show(50, False)

# On few columns
null_df = df1.na.fill("",["gender"])
null_df.show(50, False)

# integer column fill 0
# String column fill ""
"""
# ********************** create new column *********************************************************************
# Hardcoded value to new column
"""
new_df = df1.withColumn("UnK", lit("Don't know"))
new_df.show(5, False)

# Customize new column value with logic. for eg: concat()
new_df1 = df1.withColumn("fullname", concat(df1["first_name"],df1["last_name"]))
new_df1.show(5, False)

"""
# ********************** Drop existing column in DF ************************************************************
"""
new_df = df1.drop("gender","cc")
new_df.show(5, False)
"""
# ********************** Rename Column *************************************************************************
"""
new_df = df1.withColumnRenamed("gender", "genders")
new_df.show(5, False)
"""
# ************** How to read source files(csv, parquet, json, orc)/rdbms/rdd/list[dist])
"""
spark.read.csv()
spark.read.parquet()
spark.read.json()
spark.read.orc()
spark.read.table() -- Hive
spark.read.jdbc(url= localhost, properties= cred, tablename= "table_name") -- RDBMS
creds = {
    "username" : "root"
    "password" : "cloud"
    "driver" : ".com.mysql.jdbc.Driver"
    }
"""
# *********************** how to load/write data from DF **************************************************************
# df --> csv
# df.write.csv("output_path")

# df --> parquet
# df.write.parquet("output_path")

# df --> json
# df.write.json("output_path")

# df --> orc
# df.write.orc("output_path")

# df --> rdd
# df.rdd

# df --> hive
# df.write.insertInto(table_Name=)

# df --> RDBMS
# df.write.jdbc(properties, url, table_name)
