dimensions = (150, 75)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250
print("\nOriginal Dimensions:")
for dim in dimensions:
    print(dim)
# Wiriting over a tuple
dimensions = (250, 125)
print("\nModified Dimensions:")
for dim in dimensions:
    print(dim)
print("------Exercise--4.13----")
buffet = ('salad', 'steak', 'pasta', 'pizza', 'desert')
for buf in buffet:
    print(buf)
print("\n New menu:")
buffet = ('bread', 'soup', 'pasta', 'pizza', 'desert')
for buf in buffet:
    print(buf)