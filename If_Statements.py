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

print("-----Exercise--5.3-----")
alien_color = 'Yellow'
if alien_color == 'green':
    print("The player earned 5 points")

print("-----Exercise--5.4-----")
if alien_color == 'green':
    print("The player earned just 5 points")
elif alien_color != 'green':
    print("The player earned 10 points")

print("-----Exercise--5.5-----")
if alien_color == 'green':
    print("The player earned just 5 points")
elif alien_color == 'Yellow':
    print("The player earned 10 points")
else:
    print("The player earned 15 points")

print("-----Exercise--5.6-----")
person = 7
if person < 2:
    print("Baby")
elif person >= 2 and person <4:
    print("toddler")
elif person >= 4 and person < 13:
    print("Kid")
elif person >= 13 and person < 20:
    print("teenager")
elif person >= 20 and person < 65:
    print("adult")
else:
    print("Older") 

print("-----Exercise--5.7-----")
fav_fruits = ['mango','banana','guava']
if 'orange' in fav_fruits:
    print("Not a fan of orange")
elif 'kiwi' in fav_fruits:
    print("good for digstion")
elif 'mango' in fav_fruits:
    print("I love mangoes")
elif 'banana' in fav_fruits:
    print("good for gut health")
elif 'guava' in fav_fruits:
    print("High vitamin C")
else:
    print("not my favourite fruit")

print("-----Exercise--5.8-----")
usernames = ['vikku','praveen','sarada','siva','gurram','admin']
for usr in usernames:
    if 'admin' in usr:
        print(f"Hello {usr}, Would you like to see the status report")
    else:
        print(f"Hello {usr}, thank you for logging in again")

print("-----Exercise--5.9-----")
#usernames = ['siva','gurram']
usernames = []
if usernames:
    for usr in usernames:
        print(f"Our user {usr}")
    print("\n finished adding users !")
else:
    print("We need to find some users")

print("-----Exercise--5.10-----")
current_users = ['vikku','praveen','sarada','siva','admin']
new_users = ['gurram','gnrao','gvl','admin']
for usr in new_users:
    if usr not in current_users:
        print(f"Adding new {usr}")
    else:
        print(f"Sorry this username {usr} exist")
print("please change the username")

print("-----Exercise--5.11-----")
ordinal_num = [1,2,3,4,5,6,7,8,9]
for ord_num in ordinal_num:
    if ord_num == 1:
        print("1st")
    elif ord_num == 2:
        print("2nd")
    elif ord_num == 3:
        print("3rd")
    else:
        print(f"{ord_num}th")