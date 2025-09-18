# Data frame Transformations.
# Two types : Narrow Transformations, Wide Transformations
from http.cookiejar import FileCookieJar

# Narrow Transformations : Not require shuffling or distributing across cluster. Work independently without exchanging data with other transformations.
sortBy
union
filter/where
distinct ()

# Wide Transformations : Required shuffling.
groupBy()
join() - inner Join, LOJ, ROJ, FOJ
agg()
cross join
repartition()
pivot
sort()
