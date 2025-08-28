cars = ['bmw', 'audi', 'merc', 'porsche', 'lambo', 'lucid']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("-----Practise-------")
topping = 'olives'
req_topping = topping
if req_topping != 'mushrooms':
    print("Hold the olives!")

print("-----Practise-------")
age = 21
if age < 21:
    print(True)
else:
    print(False)
print("-----Practise-------")
banned_usrs = ['abc', 'def', 'ghi']
usr = 'jkl'
if usr not in banned_usrs:
    print(f"{usr.title()}, is clear")
else:
    print(f"{usr.title()}, is banned")

print("-----Exercise-------")