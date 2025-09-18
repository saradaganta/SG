"""
class Dog:
    def __init__(self, name, age, height=2):
        "initialize name and age attributes"
        self.name = name
        self.age = age
        self.height = height

    def sit(self):
        "dog sitting stimulate in response to command"
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        "dog rollover stimulate in response to command"
        print(f"{self.name} rolled over!")

my_dog = Dog('ginger', 5, 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age} Yrs old.")
print(f"My dog's height is {my_dog.height} feet")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Honey', 3)

print(f"Your dog name is {your_dog.name}")
print(f"Your dog age is {your_dog.age}")
"""
"""
print("**** Exercise 9.1 *****")
class Resturant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe(self):
        print(f"This restaurant '{self.restaurant_name}' is family friendly.")

    def open(self):
        print(f"The {self.cuisine_type} restaurant '{self.restaurant_name}' is open from 10:00 am to 9:00 pm.")
    
cusine = Resturant('Wood Lands', 'Indian')
cusine1 = Resturant('Olive Garden', 'Italian')

print(f"This '{cusine.restaurant_name}' resturant food is tasty")
print(f"The '{cusine1.restaurant_name}' resturant is {cusine1.cuisine_type}")

cusine.describe()
cusine1.open()
"""
"""
print("**** Exercise 9.2 *****")
class RESTURANTS3:
    def __init__(self, name, describe):
        self.name = name
        self.describe = describe
    
    def desc(self):
        print(f"This resturant '{self.name}' is '{self.describe}' resturant")
rest1 = RESTURANTS3('Indian Garden', 'Vegeterian')
rest2 = RESTURANTS3('Mexican Grill', 'Non Vegeterian')
rest3 = RESTURANTS3('Salad Bar', 'Vegan')

rest1.desc()
rest2.desc()
rest3.desc()
"""
"""
print("**** Exercise 9.3 *****")
class USERS:
    def __init__(self, first_name, last_name, age=None, loc=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.loc = loc
    
    def desc_user(self):
        print(f"\n********** User Profile ******** ")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        if self.age:
            print(f"Age: {self.age}")
        if self.loc:
            print(f"loc: {self.loc}")
    def greet_user(self):
        print(f"\nHello {self.first_name.title()}, welcome back !")
user1 = USERS('Bala', 'Nanda', age=68, loc='Hyd')
user2 = USERS('ntr', 'jr', age=42, loc='Mumb')
user3 = USERS('mah', 'gatt', age=54, loc='Hyd')

user1.desc_user()
user1.greet_user()

user2.desc_user()
user2.greet_user()

user3.desc_user()
user3.greet_user()
"""

# Adding attribute to class:
"""
class CAR:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 2000

    def get_descriptive_name(self):
      #  print(f"{self.year} {self.make} {self.model}")
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()   
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles")
    
my_new_car = CAR('bmw', 'm3', 2012)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
"""
# Update odometer reading.
"""
class CAR:
    def __init__(self, make, model, year):
          self.make = make
          self.model = model
          self.year = year
          self.odometer_reading = 2000

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
         print(f"This car has {self.odometer_reading} miles")
    
    def update_odometer(self, miliage):
        self.odometer_reading = miliage
my_new_car = CAR('acura', 'mdx', '2019')
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(21000)
my_new_car.read_odometer()

"""
# prevent odometer tampering
class CAR:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading = 2500
    
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles")
    def update_odometer(self,miligae):
        if miligae >= self.odometer_reading:
            self.odometer_reading = miligae
        else:
            print("You cannot rollback the odometer miligae")
my_car = CAR('audi', 'rs4', '2025')
print(my_car.get_descriptive_name()) 

my_car.update_odometer(150)
my_car.read_odometer()

    