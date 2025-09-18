"""
message = input("Tell me something, and i will repeat :")
print(message)

name = input("Please enter your name :")
print(name)

age = input("how old are you :")
print(age)

height = input("How tall are you, in feet ?")
height = float(height)

if height >= 5.9:
    print("\n You are tall enough to ride bike !")
else:
    print("\nYou will be able to ride when you are little taller.")

# even or odd :
num = input("Enter number to tell if it's even or odd number:")
num = int(num)

if num % 2 == 0:
    print(f"\nThe number {num} is even.")
else:
    print(f"\nThe number {num} is odd.")
"""
"""
print("------- Exercise 7.1 -------")
rentcar = input("What kind of rental car you are looking for :")
print(f"\nLet me see if i can find {rentcar}")

print("------- Exercise 7.2 -------")
seating = input("How many people are there in dinner group :")
seating = int(seating)

if seating > 8 :
    print(f"\nYou have to wait for a table.")
else:
    print(f"\nYour table is ready.")

print("------- Exercise 7.3 -------")
Multof10 = input("Please enter number :")
Multof10 = int(Multof10)

if Multof10 % 10 == 0:
    print(f"\n{Multof10} is multiple of 10.")
else:
    print(f"\n{Multof10} is not multiple of 10.")
"""

# While Loop
#counting
"""
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 
"""

prompt = "\nTell me something, I will repeat"
prompt += "\nEnter 'quit' to end the program: "

# message = ""
"""
while message != 'quit':
    message = input(prompt)
    print(message)
"""
# using IF
"""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
# using Flag
active = True
while active:
message = input(prompt)

if message == 'quit':
active = False
else:
print(message)
"""
# using Break
"""
prompt = "\nPlease enter the city you want to visit:"
prompt += "\n(Enter 'quit' when you are finished:)"

while True:
city = input(prompt)
if city == 'quit':
break
elif city == 'dallas':
print(f"\nI live in {city}")
else:
print(f"\nI would love to visit {city}")
"""
# using continue
"""
current_number = 0
while current_number < 9:
current_number +=1
if current_number % 2 == 0:
continue
print(current_number)
"""
print("****** Exercise 7.4 ***********")
"""
prompt = "\nPlease enter pizza topping/s : "
prompt += "\n(Enter 'quit' when finished:)" 

while True:
topping = input(prompt)
if topping == 'quit':
break
else:
print(f"\nTopping/s {topping} added to your pizza..!")
"""
print("****** Exercise 7.5/7.6 ***********")
"""
prompt = "\nEnter your age:"
while True:
age = input(prompt)
age = int(age)
if age < 3:
print("\nNo ticket needed under 3 Yrs old")
elif age >=3 and age <= 12:
print("\nTicket price is $10.")
else:
print("\nTicket price is $15.")

# Done
# While loop with lists and dictonaries:
#confirmed_users:
ucu = ['peter','junior','keate','robert','mike','greg']
cu = []

while ucu:
    current_user = ucu.pop()

    print(f"Verifying User : {current_user.title()}")
    cu.append(current_user)
print("\nThe following users have been confirmed:")
for c_u in cu:
    print(c_u.title())

# Removing all instances of specific value from list:
print("****** Remove pets from list ********")
pets = ['cat', 'dog', 'rabbit', 'dog','parrot','rabbit']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling a dictonary with user input:
print("****** filling dictornary with user input ********")
responses = {}
poll_active = True

while poll_active:
    name = input("\nWhat is your name :")
    response = input("What car you want to drive ?")

    responses[name] = response

    repeat = input("Would you like to let another person drive? (yes/no)")
    if repeat == 'no':
        poll_active = False

print("\n-----poll results ------")
for name,response in responses.items():
    print(f"{name} would like to drive car {response}")
"""
"""
print("******* Exercise 7.8 ********")
sandwich_orders = ['subway','potbelly','mcd']
finished_sandwich = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"\nI made your {sandwich} sandwich")
    finished_sandwich.append(sandwich)

print(f"\nThe below sandwich are completed:")
for sw in finished_sandwich:
    print(sw)   
"""
print("******* Exercise 7.9 ********")
sandwich_orders = ['pastrami','subway','pastrami','potbelly','mcd','pastrami']
finished_sandwich = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(f"\nDeli has run out of 'pastarami'")
print(sandwich_orders)
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nI made you {sandwich} sandwich")
    finished_sandwich.append(sandwich)
print(f"\nThe below sandwich are completed :")
for sw in finished_sandwich:
        print(sw)

print("******* Exercise 7.10 ********")
vacation = {}
poll = True

while poll:
     name = input("\nWhat is your name:")
     response = input("\nWhich place you would like to visit :")

     vacation[name] = response

     repeat = input("Would you like others to respond ? (yes/no)")
     if repeat == 'no':
          poll = False
print("\n----- results -----")
for name,response in vacation.items():
     print(f"\n{name} like to visit {response}")
