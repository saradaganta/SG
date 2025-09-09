# greet:
def greet_user():
    "Display a simple greeting."
    print("Hello")
greet_user()

# Passing information to function:
def greet_user(username):
    print(f"\nHello, {username}!")
greet_user("Siva Gurram")

print("***** Exercise 8.1 ******")
def display_message():
    "Display messsage"
    print("\nI learn how to use function, Call funtion and use to dispaly message correctly")
display_message()

print("***** Exercise 8.2 ******")
def fav_book(title):
    print(f"\nOne of my favourite book is {title}!")
fav_book('Alice in WonderLand')

# Passing Arguments:
def desc_pet(type, name):
    print(f"\nI have a {type}.")
    print(f"\nMy {type}'s name is {name.title()}.")
desc_pet('cat', 'kitten')
# Multiple fuction calls:
