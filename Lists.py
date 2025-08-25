
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