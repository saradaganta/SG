from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode

spark=SparkSession.builder.appName("CreateTable").getOrCreate()

# Make the below input data into multiple rows
# Input data format
data = [('Alice','Badminton,Tennis'),('Bob','Tennis,Cricket'),('Julie','Cricket,Carroms')]
#Assign column names
columns = ["Name","Hobbies"]
# Create and display as input table
df = spark.createDataFrame(data, columns)
df.show()
# Convert input data into array using Split & show as multiple rows using explode.
#df.select(df.Name, split(df.Hobbies, ',')).show(truncate=False)
df.select(df.Name, explode(split(df.Hobbies, ',')).alias('Hobbies')).show(truncate=False)