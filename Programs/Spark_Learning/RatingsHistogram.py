"""
from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf=conf)

lines = sc.textFile("file:///Users/sg/Documents/Python_Learning/SG/Programs/Data Files/source/ml-100k/u.data")
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

sortResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortResults.items():
    print("%s %i" %(key, value))
"""