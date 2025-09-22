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

# Returning a Dictonary:
def person(fname, lname):
    person = {'f':fname, 'l':lname}
    return person
artist = person('siva', 'gurram')
print(artist)

def person(fname, lname, age=None):
    person = {'f':fname, 'l': lname}
    if age:
        person['age'] = age
    return person
artist = person('siva','gurram', age=45)
print(artist)
# Using a function with a while loop
def formatted_name(fname, lname):
    fullname = f"{fname} {lname}"
    return fullname.title()

while True:
    print("\nPlease tell your me your name:")
    print("(enter 'q' at any time to quit)")

    fname = input("First Name: ")
    if fname == 'q':
        break
    lname = input("Last Name :")
    if lname == 'q':
        break
    format_name = formatted_name(fname, lname)
    print(f"\nHello, {format_name}!")
"""
"""
print("***** Exercise 8.6 *****")
def city_country(city, country):
        print(f"\n{city} is in {country}")
city_country('dallas', 'USA')
city_country('brisbane', 'Australia')
city_country('cary', 'USA')

print("***** Exercise 8.7 *****")
def make_album(title, artist, songs=None):
        make_album = {'name' : title, 'author' : artist}
        return make_album
album = make_album('siva', 'great warriors', 10)
print(album)
album = make_album('gurram', 'super heros', 6)
print(album)
album = make_album('vik', 'good vibes')
print(album)
"""
"""
print("***** Exercise 8.8 *****")
def make_album(title, artist, songs=None):
        make_album = {'name' : title, 'author' : artist, 'songs':songs}
        return make_album
while True:
        print(f"\nPlease enter the album details")
        print("(enter 'q' at any time to quit)")

        title = input("Enter Name of album :")
        if title == 'q':
            break
        artist = input("Enter Name of the Artist :")
        if artist == 'q':
            break
        songs = input("Enter Number of songs :")
        if songs == 'q':
            break
        album = make_album(title, artist, songs)
        print(f"\nThe book '{title.title()}' is written by '{artist.title()}' with {songs} songs..!")

# Passing a List:
# greet users
def greet_usr(names):
      for name in names:
            msg = f"Hellow, {name.title()}..!"
            print(msg)
usernames = ['Siva', 'Gurram', 'Kumar']
greet_usr(usernames)

# Modify list in a function:
# Prinitng models:
unprint_designs = ['flower pot', 'window blinds', 'wall art']
completed_models = []

while unprint_designs:
      current_design = unprint_designs.pop()
      print(f"\nPrinting Model: {current_design}")
      completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
      print(completed_model)

# structuring funcctions:
def print_models(unprint_designs, completed_models):
      while unprint_designs:
            current_design = unprint_designs.pop()
            print(f"Printing Model: {current_design}")
            completed_models.append(current_design)
def show_completed_models(completed_models):
      for completed_model in completed_models:
            print(completed_model)
        
unprint_designs = ['dome light', 'flower bulb', 'led chandler']
completed_models = []

print_models(unprint_designs, completed_models)
show_completed_models(completed_models)

# Preventing a function from modifying: copy
def make_pizza(*toppings):
      print(toppings)
    
make_pizza('Cheese')
make_pizza('mushrooms','olives','hot peppers')

def make_pizza(*toppings):
      for topping in toppings:
            print(f"- {topping}")
make_pizza()

make_pizza('Cheese')
make_pizza('mushrooms','olives','hot peppers')

def make_pizza(size, *toppings):
      print(f"\nMaking a {size}-inch pizza with the toppings :")
      for topping in toppings:
            print(f"- {topping}")
make_pizza(14, 'cheese')
make_pizza(18, 'mushrooms','olives','hot peppers')

# using arbitary keyword arguments:
def profile(first, last, **usr_info):
    usr_info['fname'] = first
    usr_info['lname'] = last
    return usr_info
usr_profile = profile('Siva', 'Gurram', location = 'McKinney', field = 'Information Technology')
print(usr_profile)
"""
"""
print("****** Exercise 8.12 ******")
def subway(size, *items):
    print(f"\nMake {size} inch subway with items: {items} ")
    for item in items:
        print(f"-{item}")
subway(6, 'multigrain', 'onions', 'olives', 'peppers')
subway(12, 'wheat', 'chicken', 'hot peppers', 'avacado')
subway(6, 'Herbs', 'tuna', 'cucumbers', 'tomato')
"""
"""
print("****** Exercise 8.13 ******")
def usr_prof(fname, lname, **info):
    info['firstname'] = fname
    info['lastname'] = lname
    return info
prof = usr_prof('vik', 'gur', loc = 'US', grade = '2nd', sport = 'soccer')
print(prof)
"""
"""
print("****** Exercise 8.14 ******")
def make_car(manfacturer, model, price=None, **info):
    info['company'] = manfacturer
    info['name'] = model

    if price is not None:
        info[price] = price
    return info
car = make_car('nissan', 'rogue', color= 'white', type = 'suv', drive='awd')
car1 = make_car('honda','acura', color = 'white', type = 'suv', drive = 'shawd')
car2 = make_car('subaru', 'forester', color = 'blue', type = 'suv', price = '$35000', drive = 'symmetrical awd')
print(f"{car}, \n{car1}, \n{car2}")
"""
"""
# Storing your functions in modules:
# importing module:
from Modules import pizza

pizza.make_pizza(16, 'cheese')
pizza.make_pizza(14, 'chicken', 'pipeapple', 'hot peppers', 'olives')

# importing only function from module
from Modules.pizza import make_pizza as mp

mp(16, 'chicken')
mp(12, 'onions', 'mushrooms', 'green peppers')
"""
print("**** Exercise 8.15 ****")
from Modules.printing_func import print_models as pm, show_completed_models as scm
unprinted_designs = ['car toy', 'key chain', 'stylus pen']
completed_models = []

pm(unprinted_designs, completed_models)
scm(completed_models)


