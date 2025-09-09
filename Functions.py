"""
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
    print(f"My {type}'s name is {name.title()}.")
desc_pet('cat', 'kitten')
# Multiple fuction calls:
desc_pet('dog', 'ginger')
# Default value:
def desc_vehicle(name, type = 'car'):
    print(f"\nI have a {type}.")
    print(f"My {type}'s name is {name.title()}.")
desc_vehicle('acura','suv')
desc_vehicle('subaru')
desc_vehicle('nissan','')
"""
print("******* Exercise 8.3 *******")
def make_shirt(size, desc):
    print(f"\nSize of the Shirt is : {size}")
    print(f"Its theme is : {desc.upper()}")
make_shirt('Medium', 'Just Do It')
make_shirt('Small', 'for successful living')

print("******* Exercise 8.4 *******")
def make_shirt(size, desc='I love Python'):
    print(f"\nSize of the Shirt is : {size}")
    print(f"Its theme is : {desc.upper()}")
make_shirt('Medium')
make_shirt('Large')
make_shirt('Small', 'for successful living')

print("******* Exercise 8.5 *******")
def city_desc(city, country = 'India'):
    print(f"\n{city} is in {country.title()}")

city_desc('ongole')
city_desc('amaravathi')
city_desc('dallas', 'usa')

# Return Values:
def formatted_name(fname, lname):
    fullname = f"{fname} {lname}"
    return fullname.title()

artist = formatted_name('tarak', 'nandamuri')
print(artist)

# optional argument:
def name(fname, lname, mname = ''):
    if mname:
        fullname = f"{fname} {mname} {lname}"
    else:
        fullname = f"{fname} {lname}"
    return fullname.title()
artist = name('siva', 'kumar','gurram')
print(artist)
artist = name('vikranth','gurram')
print(artist)
