from pyspark.sql.types import IntegerType

from pyspark.sql import SparkSession
# String Functions imports
from pyspark.sql.functions import count, desc, col, upper, concat, lit, substr, concat_ws, round
# Arithmatic Functions imports
#from pyspark.sql.functions import min, max, avg, sum, count

spark = SparkSession.builder.appName("sql with parquet").getOrCreate()

df = spark.read.parquet("/Users/sg/Project/PySpark_Learning/PycharmProjects/house-price.parquet")
# convert "area" & "bedrooms" into integer.
df = df.withColumn("area",col("area").cast(IntegerType())) \
       .withColumn("bedrooms", col("bedrooms").cast(IntegerType()))

df.show(10, False)
df.printSchema()

df.createOrReplaceTempView("house_price")
"""
# ****************** Clauses ******************************************************************************
# Select & where using sql & df
spark.sql("""
#Select * from house_price where 1 = 1 and bedrooms >= 4 and bathrooms >= 3 and stories = 2 and area > 4000 ;
""").show()
# df Select
df.select("*").show(10, False)
# df where
df.where("1=1 and bedrooms >= 4 and bathrooms >= 3 and stories = 2 and area > 4000").show(5, False)
# df group by
df.groupBy("bedrooms").agg(count("*")).show(5, False)
#df order by
df.groupBy("bedrooms").agg(count("*")).orderBy("bedrooms").show(5,False)
# for desc order
df.groupBy("bedrooms").agg(count("*")).orderBy(desc("bedrooms")).show(5,False)
# for having
df.groupBy("bedrooms").agg(count("*")).where(count("*") > 100).orderBy(desc("bedrooms")).show(5, False)
"""
# ******************* String Functions ****************************************************************************
"""
# df String - Upper(), Lower(), substr(), concat()
# withColumn() is used to create new column
df.withColumn('prefarea_upper',upper(col("prefarea"))).select("prefarea", "prefarea_upper").show(5, False)

# df concat ()
df.withColumn('fullstat', concat(df["prefarea"], lit(" "), df["furnishingstatus"])).show(5, False)

df.withColumn('furnish', concat_ws(' ',df["prefarea"], df["furnishingstatus"])).show(5, False)

# df substr()

df.withColumn('furnish', col("furnishingstatus").substr(1,3)).select("furnishingstatus", "furnish").show(5, False)

"""
# ******************* Arithmetic Functions ****************************************************************
"""
# df +, -, *, /, %, round(), ceil(), floor()
# sum
df.withColumn('add_col', col("area") + col("bedrooms")).select("area", "bedrooms", "add_col").show(5, False)

# Minus
df.withColumn('substract_col', col("area") - col("bedrooms")).select("area", "bedrooms", "substract_col").show(5, False)

# Multiply
df.withColumn('multiply_col', col("area") * col("bedrooms")).select("area", "bedrooms", "multiply_col").show(5, False)

# Divide
df.withColumn('divide_col', col("area") / col("bedrooms")).select("area", "bedrooms", "divide_col").show(5, False)

# Mod
df.withColumn('mod_col', col("area") % col("bedrooms")).select("area", "bedrooms", "mod_col").show(5, False)

# Mod
df.withColumn('round_col', round(col("area"))).select("area", round_col").show(5, False)
"""
# ***************** Aggregate Functions *******************************************************************
"""
# Min, Max, Avg, Sum, Count
df.agg(min("area"), max("area"), avg("area"), sum("area"), count("area")).show(5, False)
"""
# **************** Joins **********************************************************************************
"""
# Inner join, LOT, ROT, FOT, CROSS JOIN
df_p = spark.read.parquet("/Users/sg/Project/PySpark_Learning/PycharmProjects/userdata1.parquet").select ("id", "first_name", "last_name")
df_c = spark.read.option("header", True).option("delimiter", ",").csv("/Users/sg/Project/PySpark_Learning/PycharmProjects/userdata1.csv")

df_p.show(5, False)
df_c.show(5, False)

# Inner Join
new_df = df_p.join(df_c, df_p['id'] == df_c['id'], "inner")
new_df.show(5, False)

# LOT
new_df = df_p.join(df_c, df_p['id'] == df_c['id'], "left")
new_df.show(5,False)

# ROT
new_df = df_p.join(df_c, df_p['id'] == df_c['id'], "right")
new_df.show(5,False)

# FOT
new_df = df_p.join(df_c, df_p['id'] == df_c['id'], "full")
new_df.show(5, False)

# CROSS
new_df = df_p.crossJoin(df_c)
new_df.show(5, False)
"""
# UNION
"""
new_df = df_p.union(df_c)
new_df.show(10, False)

# UNION ALL

new_df = df_p.unionAll(df_c)
new_df.show(10, False)
"""