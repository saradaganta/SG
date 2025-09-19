from pyspark.sql import SparkSession


spark=SparkSession.builder.appName("DE_FAQs").getOrCreate()

# *********** Question 1 *****************
from pyspark.sql.functions import split, explode
"""
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

"""
# *********** Question 2 *****************
from pyspark.sql.functions import *
"""
# Get the first not null city from the 3 city columns
# Input data format.
data = [('Goa','','AP'),('', 'AP', None),(None,'','Bnglr')]
#Assign column names
columns=["city1","city2","city3"]
# Create and display as input table
df=spark.createDataFrame(data, columns)
df.show()
# Working with coalesce to get first not null value
#df1=df.withColumn('firstnotnull',coalesce(df.city1,df.city2,df.city3))
# Convert blanks to Nulls where coalesce can get available not null value.
df1=df.withColumn('firstnotnull',coalesce(
    when(df.city1=='',None).otherwise(df.city1),
    when(df.city2=='',None).otherwise(df.city2),
    when(df.city3=='',None).otherwise(df.city3)))
df1.show(truncate=False)

"""
# *********** Question 3 *****************
from pyspark.sql.functions import *
# Combine two tables student, student marks and calculate percentage to get result
data1=[(1,"Steve"),(2,"David"),(3,"John"),(4,"Shree"),(5,"Helen")]
data2=[(1,"SQL",90),(1,"PySpark",100),(2,"SQL",70),(2,"PySpark",60),(3,"SQL",30),(3,"PySpark",20),(4,"SQL",50),(4,"PySpark",50),(5,"SQL",45),(5,"PySpark",45)]
#Assign column names
schema1=["Id","Name"]
schema2=["Id","Subject","Mark"]
# Create and display as input table
df1=spark.createDataFrame(data1,schema1)
df2=spark.createDataFrame(data2,schema2)
df1.show()
df2.show()
# Join both data frames df1 & df2. We are dropping Id from second table not to display.
df_join=df1.join(df2,df1.Id==df2.Id).drop(df2.Id)
df_join.show(truncate=False)
# Calculate the percentage.
df_per=df_join.groupBy('Id','Name').agg(
    (sum('Mark')/count('*')).alias('Percentage')
)
df_per.show(truncate=False)
# Similar to Case statement for determine grades.
df_final=df_per.select('*', 
              when(df_per.Percentage>=70,'Distinction')
              .when((df_per.Percentage<70) & (df_per.Percentage>=60), "First Class")
              .when((df_per.Percentage<60) & (df_per.Percentage>=50), "Second Class")
              .when((df_per.Percentage<50) & (df_per.Percentage>=40), "Third Class")
              .when((df_per.Percentage <40), "Fail"
              )).alias('Result')
df_final.show(truncate=False)