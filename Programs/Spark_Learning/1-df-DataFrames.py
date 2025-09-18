from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.appName("CSV_PARQUET_JSON TO DF").getOrCreate()
# Schema Enforcement - Enforces schema on data. Data type for each column will be defined.
# Better Performance - Columnar storage format and optimization techniques
# Higher - Level API - Provides higher level API for data manipulation, Easy to write complex data processing pipelines
# Integration with SQL - DF Can be easily converted into SQL tables and integrate with SQL based tools/DB.

"""
input_file_schema = StructType([
    StructField("name", StringType(), True),
    StructField("alpha-2", StringType(), True),
    StructField("alpha-3", StringType(), True),
    StructField("country_code", IntegerType(), True)
])

input_df = spark.read\
    .option("header", True)\
    .option("delimiter", ",")\
    .option("header", True)\
    .option("inferSchema", True)\
    .schema(input_file_schema)\
    .csv('/Users/sg/Project/PySpark_Learning/PycharmProjects/country_full.csv')

input_df.show(10)
input_df.printSchema()
"""
# Ways to create DF's :
# FILE BASED - S3, HDFS, Local file system (Linux/Windows)
    # CSV, PARQUET, ORC, JSON ..etc
# TABLE BASED - RDBMS, NOSQL DB, Hive
    # Table --> DF

# RDD - rdd --> DF
rdd = spark.sparkContext.parallelize([(1, "Siva, 40"), (2, "Sarada", 32), (3, "Vikku", 7)])
df = rdd.toDF(["emp_id", "emp_name", "emp_age"])
df.show()

# Array -> DF

data = [{"id": 1, "name": "Siva", "age": 40},
        {"id": 2, "name": "Sarada", "age": 32},
        {"id": 3, "name": "Vikranth", "age": 7},
        ]
df = spark.createDataFrame(data)
df.show()

# File -- DF CSV
# input_df = spark.read.option("header", True).options("inferSchema", True).csv("/Users/sg/Project/PySpark_Learning/PycharmProjects/country_full.csv")
# input_df.show(5)

# common features - Header, delimiter ("," default)
# print("*** Schema ***")
# input_df.printSchema()

# Read from parquet/orc:
"""
input_df = spark.read.parquet("/Users/sg/Project/PySpark_Learning/PycharmProjects/house-price.parquet")
input_df.show(10)
input_df.printSchema()
"""
# Read from json:
"""
input_df = spark.read.json("/Users/sg/Project/PySpark_Learning/PycharmProjects/weather.json")
#input_df = spark.read.option("multiline", True).json("/Users/sg/Project/PySpark_Learning/PycharmProjects/weather.json")
input_df.show(10)
input_df.printSchema()
"""
# Read Nested Json :
"""
#input_df = spark.read.json("/Users/sg/Project/PySpark_Learning/PycharmProjects/nested_json.json")
input_df = spark.read.option("multiline", True).json("/Users/sg/Project/PySpark_Learning/PycharmProjects/nested_json.json")
#input_df.show(10)
input_df.printSchema()
"""
# ************************************************************************************************************************************************
# connect to Hive table:
# reading from tale.
# import spark session
spark = SparkSession.builder.appName("Connect to Hive").enableHiveSupport().getOrCreate()
hive_df = spark.read.table("Select * from db.table")
hive_df.show()

# reading same data from file location:
hive_df1 = spark.read.parquet("/User/hive/warehouse/db/table/")
hive_df1.show()

# Connect to RDBMS :
# Read from mysql.
#import spark session
spark = spark.builder.appName("Read data from MYSQL").getOrCreate()

jdbc_url = "jdbc.mysql://<hostname>:<portname>/db_name"
# if connecting to local then use below :
# --jdbc_curl = "jdbc.mysql://localhost:22/retail_db"

creds = (
    "username" : "admin",
    "passowrd" : "Pass"
    "driver" : "com.mysql.jdbc.Driver"
)

df = spark.read.jdbc(url=jdbc_url,properties=creds,table="table_nm")
df.show()