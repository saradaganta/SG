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