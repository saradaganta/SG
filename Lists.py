
cars = ['bmw', 'audi', 'porsche', 'merc']
print(cars)
print(cars[0])
print(cars[0].title())
print(cars[1])
print('#', cars[3])
print(cars[-1])
print(cars[-2]) 

print("#-----Exercise--------#")
print("**** Exer: 3-1 ****")

names=['abc', 'DEF', 'ghi', 'jkl']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print("**** Exer: 3-2 ****")

greet = "Happy Friendship Day"
print(greet, (names[0].upper()))
print(greet, names[1].lower())
print(greet, names[2].title())
print(greet, names[3])

print("**** Exer: 3-3 ****")
message = f"My favourite car is {cars[0].title()}."
print(message)

# ------ Changing elements in list -----------
print(cars)

print("*** After changing first element from BMW TO Toyota ***")
cars[0] = 'toyota'
print(cars)

print("*** Appending new element Honda to list ***")
cars.append('honda')
print(cars)

print("*** Inserting new element Acura to list ***")
cars.insert(3, 'acura'.title())
print(cars)

print("*** Remove/Delete element honda & toyota from list ***")
cars.remove('honda')
del cars[0]
print(cars)

print("*** pop the element from list ***")
pop_cars = cars.pop()
print(cars)
print(pop_cars)
previously_owned = pop_cars
print(f"The car I owned once was a {previously_owned.title()}.")

pop_cars = cars.pop(2)
print(cars)
print(pop_cars)
previously_owned = pop_cars
print(f"\n The car I owned now is {previously_owned.title()}.")

bikes=['honda','ducati','kawasaki','yamaha']
print(f"Print Bikes:", bikes)
bikes.sort()
print(f"print sorted Bikes:", bikes)
bikes.sort(reverse=True)
print(f"Print reverse sorted Bikes:", bikes)
len(bikes)
#print(bikes[-5])
print(bikes[-3])

famous=['ntr','cbn', 'modi','kalam']
for fam in famous:
    if fam == 'ntr':
        print(fam.upper())
    else:
     print(fam)

print("------- Exercise --------------")


pizza = ['chicken', 'cheese','chkncheese']
print(pizza)
for piz in pizza:
   if piz == 'chicken':
       print(f"I love {piz} pizza, I really love Pizza")
   elif piz == 'cheese':
        print(f"I can have {piz} Pizza, I like this pizza")
   else:
       print(f"I really love {piz} pizza, I love it")

print("------- Exercise --------------")

pets = ['dog', 'cat', 'rabbit']
print(pets)
for pt in pets:
    if pt == 'dog':
        print(f"{pt} is a trusted pet")
    elif pt == 'cat':
        print(f"{pt} is a funny pet")
    else:
        print(f"{pt} is cute pet")

print("------- Range() Function --------------")
# First numbers
for val in range(1,6):
    print(val)

print("print numbers as list")
numbers = list(range(1, 6))
print(numbers)

# even_numbers
even_numbers = list(range(2,12,2))
print(even_numbers)
# Odd_numbers
odd_numbers = list(range(1,15,3))
print(odd_numbers)
# Square_numbers
squares = []
for value in range(1, 100):
    square = value ** 2
    squares.append(square)
print(squares)

# simple_Stats
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

print("-------EXercises-----------")
for count in range(1, 21):
    print(count)
print("-------EXercises-----------")
num = [1,2,3,4,5,6,7,8,9,10]
for nbr in num:
    print(nbr)
print("-------EXercises-----------")
a = min(num)
b = max(num)
c = sum(num)
print(f"{a},{b},{c}")    
print("-------EXercises-----------")
odd = list(range(1, 20, 3))
print(odd)
print("-------EXercises-----------")

for lst3 in range(3, 30, 3):
    print(lst3)
print("-------EXercises-----------")
cubes = []
for value in range(1, 10):
    cube = value ** 3
    cubes.append(cube)
print(cubes)
print("-------EXercises-----------")
players = ['ganguly', 'virat', 'sachin', 'shewag', 'dhoni']
print(players[1:3])
print(players[:3])
print(players[2:])
print(players[-2:])
print("-------Exercises-----------")
for player in players[:2]:
    print(player.title())
print("-------Practise-----------")
my_food = ['chicken', 'lamb', 'fish', 'shrimp', 'crab', 'lobster']
friend_food = my_food[2:4]

print(f"My favourite foods are {my_food}")
print(f"My friends favourite foods are {friend_food}")
my_food.append('ice_cream')
friend_food.append('cake')
print(my_food)
print(friend_food)

friend_food = my_food
print(my_food)
print(friend_food)

print("-------Exercises-----------")
