car = {'color': 'blue', 'points': 9}
print(car['color'])
print(car['points'])

car['x_position'] = 0
car['y_position'] = 25
print(car)

print(f"car color is {car['color']}")
car['color'] = 'ash'
print(f"The car color is now {car['color']}")

car['speed'] = 'fast'
print(f"Original positon: {car['x_position']}")

if car['speed'] == 'slow':
    x_increment = 1
elif car['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
car['x_position'] = car['x_position'] + x_increment
print(f"New Position: {car['x_position']}")

car = {'color': 'blue', 'points': 9}
print(car)
del car['points']
print(car)

print("------practise--------")
fav_lang = {'siva' : 'python', 'sarada' : 'java', 'praveen' : 'sql', 'ganta' : 'python'}
lang = fav_lang['ganta'].title()
print(f"Ganta's favourite language is {lang}")

print("------practise--------")
car = {'color': 'Orang', 'speed': 'Normal'}
#print(car['points'])
point_val = car.get('points', "No points assigned")
print(point_val)

print("------Exercise-6.1-------")
person = {'fname': 'siva', 'lname': 'gurram', 'age': '45', 'city': 'mckinney'}
print('fname :',person['fname'])
print('lname :',person['lname'])
print('age :',person['age'])
print('city :',person['city'])

print("------Exercise-6.2-------")
fav_num= {'siva' : 100, 'gurram' : 200, 'kumar' : 300 }
print('siva :',fav_num['siva'])
print('gurram :',fav_num['gurram'])
print('kumar :',fav_num['kumar'])

for name, number in fav_num.items():
    print(f"{name}'s number is {number}")

# num = {}
# for i in range(3):
#     name = input("Enter your name :")
#     number = input("Enter your number :")
#     num[name] = number
# print("\n Favourite numbers")
# for name, number in num.items():
#     print(f"{name}'s favourite number is {number}")

print("------Exercise-6.3-------")
prog = {
    'if' : 'applying condition/s',
    'for' : 'looping the values',
    'print' : 'print or display'
}
for program, desc in prog.items():
    print(f"{program.upper()} is used to {desc}")

print("------Exercise-6.4-------")
car = {
    'good' : 'acura',
    'normal' : 'nissan',
    'bad' : 'range rover'
}
for character, name in car.items():
    print(f"{character.upper()} car is {name}")

print("------Exercise-6.5-------")
rivers = {
    'ganga' : 'big',
    'krishna' : 'large',
    'godhavari' : 'huge'
}
for name, type in rivers.items():
    print(f"{name.title()} is a {type.title()} river")

print("------Exercise-6.6-------")
poll = {
    'telugu' : 'mother tongue',
    'english' : 'regular',
    'hindi' : 'occational'
    }
for lang, type in poll.items():
    print(f"{lang.title()} is my {type} language")

print("------Nesting-------")

toy_1 = {'color' : 'green', 'points' : 5}
toy_2 = {'color' : 'red', 'points' : 10}
toy_3 = {'color' : 'blue', 'points' : 15}

toys = [toy_1, toy_2, toy_3]
for toy in toys:
    print(toy)

# Make an empty list for storing toys”
toys = []
for toy_number in range(30):
    new_toy = {'color': 'green', 'points': 5, 'quality': 'good'}
    toys.append(new_toy)
# “Show the first 5 aliens.”
for toy in toys[:5]:
    print(toy)
print("...")

print(f"Total number of toys: {len(toys)}")

# Make an update for first 3 toys”
for toy in toys[:3]:
    if toy['color'] == 'green':
        toy['color'] = 'yellow'
        toy['quality'] = 'best'
        toy['points'] = 15
for toy in toys[:5]:
    print(toy)
print("...")

# Make a loop ”

for toy in toys[0:5]:
    if toy['color'] == 'yellow':
        toy['color'] = 'cyan'
        toy['quality'] = 'great'
        toy['points'] = '25'
    elif toy['color'] == 'green':
        toy['color'] = 'red'
        toy['quality'] = 'very good'
        toy['points'] = '30'
for toy in toys[:5]:
    print(toy)
print("...")