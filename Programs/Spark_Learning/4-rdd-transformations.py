from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("transformations").getOrCreate()

# Transformations

my_list = ["Siva","Kumar","Gurram"]
my_list1 = [1,2,3,4,5,6,7,8]
my_list2 = ["hi siva", "how are you", "all is well"]
my_list3 = [(10, 50000), (20, 45000), (30, 80000), (10, 60000), (20, 35000)]

# Upper
rdd = spark.sparkContext.parallelize(my_list)
print(rdd.collect())
print("***** sting to upper case ****")
new_rdd = rdd.map(lambda x : x.upper())
print(new_rdd.collect())

# Math Operations
rdd1 = spark.sparkContext.parallelize(my_list1)
print("**** Multiply ****")
new_rdd1 = rdd1.map(lambda x : x * 2)
print(new_rdd1.collect())

# Filter
print("**** Filter ****")
filter_rdd = rdd1.filter(lambda x : x > 3)
print(filter_rdd.collect())

# FlatMap eg: [[1,2,3],[2,3,4]] = [1,2,2,3,3,4]
print("***** FlatMap *****")
# use "split" function to convert from string to list.

rdd2 = spark.sparkContext.parallelize(my_list2)
print(rdd2.collect())
# split(List of List) = [["hi siva"], ["how are you"], ["all is well"]]
# flatmap(List of String) = ["hi", "siva", "how, "are", "you", "all", "is", "well"]
fm_rdd = rdd2.flatMap(lambda x : x.split(" "))
print(fm_rdd.collect())

# Group by key
print("*** Group by key ****")
rdd3 = spark.sparkContext.parallelize(my_list3)
print(rdd3.collect())
group_rdd = rdd3.groupByKey()
print(group_rdd.collect())
# Group by and Aggregate
grp_agg_rdd = group_rdd.mapValues(lambda x : sum(x))
print(grp_agg_rdd.collect())

# reduced by key (Similar to group by key generally used in more frequently)
print("*** reduced by key ***")
print(rdd3.collect())
grp_red_rdd = rdd3.reduceByKey(lambda x,y : x + y)
print(grp_red_rdd.collect())

# Joins
print("*** joins ***")
rdd1 = spark.sparkContext.parallelize([(1, ('James', 29)), (2, ('Peter', 32)), (3, ('Larry')), (4, ('Greg' ,'50'))])
rdd2 = spark.sparkContext.parallelize([(1, ('New York', 'CEO')), (2, ('SFO', 'ACTOR')), (3, ('DALLAS', 'DOC')), (1, ('DC', 'POLITICIAN'))])
join_rdd = rdd1.leftOuterJoin(rdd2)
print(join_rdd.collect())

# Distinct
print("*** Distinct ***")
rdd = spark.sparkContext.parallelize([1,2,3,3,4,2,5])
dist_rdd = rdd.distinct()
print(dist_rdd.collect())

# sort by
print("*** sort by ***")
rdd = spark.sparkContext.parallelize([7,0,6,9,1,2,3,3,4,2,5])
srt_rdd = rdd.sortBy(lambda x : x, ascending = False)
print(srt_rdd.collect())
srt_rdd1 = rdd.sortBy(lambda x : x, ascending = True)
print(srt_rdd1.collect())

# Union
print("*** Union ***")
rdd1 = spark.sparkContext.parallelize([1,3,5])
rdd2 = spark.sparkContext.parallelize([2,4,6])
union_rdd = rdd1.union(rdd2)
print(union_rdd.collect())

# Cartesian
print("*** Cartesian ***")
rdd1 = spark.sparkContext.parallelize([1,3,5])
rdd2 = spark.sparkContext.parallelize(['a','b','c'])
cart_rdd = rdd1.cartesian(rdd2)
print(cart_rdd.collect())

# FAQ's
# what is difference between map & flatmap
    # map(): This function takes one element and produce one element.
    # flatmap() : This function take one element and will produce one or more element.
# what is the difference between coalesce and repartition
    # Performance technique
    # To decrease partitions we use coalesce. Increase or decrease we use repartition.
# what is difference between groupByKey and reduceByKey
    # groupByKey() - Data will go to one node first and then apply grouping.
        # eg: 5 machines(nodes) = 5gb each node has 1 gb data. With groupByKey() all 5gb data will go to only one node and apply grouping.
    # reduceByKey() - It applies grouping in each node and it will go to one node.
# Write wordcount program
    # Look for wordcount.py