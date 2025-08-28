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

print("-----Exercise--5.1-----")
car = ['acura','lexus','infinity','suburu','honda','toyota','nissan']
car = 'suburu'
if car == 'suburu':
    print(True)
else:
    print(False)
print(car)

car = 'audi'
if car == 'suburu':
    print(True)
else:
    print(False)
print(car)

car = 'acura'
if car == 'acura':
    print(True)
else:
    print(False)
print(car)

print("-----Exercise--5.2-----")

x = 10
if x > 5 :
    print(True)
else:
    print(False)

y = ['a','s','d']
b = 'a'
if 'a' in y:
    print(f"user {b.upper()} exist")
else:
    print(f"user {b.upper()} not exist")