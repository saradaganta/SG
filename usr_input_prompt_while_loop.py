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
"""
# using Flag
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
# using Break