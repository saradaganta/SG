"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_desc_name(self):
        longname = f"{self.year} {self.make} {self.model}"
        return longname.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print(f"You cannnot roll back odometer from {self.odometer_reading} miles")
    def increment_odometer(self, miliage):
        self.odometer_reading += miliage
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on full charge.")
    
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    
        self.battery_size = 65

    def desc_battery(self):
        print(f"This car has a {self.battery_size} --kwh battery.")
    
    def fill_gas_tank(self):
        print("This car dosen't have gas tank!")
    
tesla = ElectricCar('Tesla', 'X', 2025)
print(tesla.get_desc_name())
tesla.desc_battery()
tesla.get_range()
"""
print("***** Exercise 9.6 *******")
"""
class Resturant():
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def get_desc(self):
        print(f"{self.name} is an {self.type} resturant")      

class IceCreamStand(Resturant):
    def __init__(self, name, type, icecream='vanilla'):
        super().__init__(name, type)
        self.icecream = icecream
    def desc_icecream(self):
        print(f"This resturant has {self.icecream} flavour icecream")

resturant1 = Resturant('swagath', 'indian')
print(resturant1.get_desc())

ice_stand = IceCreamStand('sweet treats', 'Dessart', icecream="coconut")
print(ice_stand.get_desc())
ice_stand.desc_icecream()
"""
print("***** Exercise 9.7 *******")
"""
class USERS:
    def __init__(self, first_name, last_name, login_attempts, age=None, loc=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.loc = loc
        self.login_attempts = login_attempts
    
    def desc_user(self):
        print(f"\n********** User Profile ******** ")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        if self.age:
            print(f"Age: {self.age}")
        if self.loc:
            print(f"loc: {self.loc}")
    def greet_user(self):
        print(f"\nHello {self.first_name.title()}, welcome back !")
class ADMIN(USERS):
    def __init__(self, first_name, last_name, login_attempts, age=None, loc=None):
        super().__init__(first_name, last_name, login_attempts, age, loc)
        self.privileges = [
        "can add a post",
        "can delete a post",
        "can ban user"]
    def show_privileges(self):
        print(f"\nAdministrator privileges for {self.first_name.title()}:")
        for privileges in self.privileges:
            print(f"-- {privileges}")

admin1 = ADMIN("siva", "gurram", 45, "dallas")
admin1.desc_user()
admin1.greet_user()
admin1.show_privileges()
"""
print("***** Exercise 9.8 *******")
class USERS:
    def __init__(self, first_name, last_name, login_attempts, age=None, loc=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.loc = loc
        self.login_attempts = login_attempts
    
    def desc_user(self):
        print(f"\n********** User Profile ******** ")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        if self.age:
            print(f"Age: {self.age}")
        if self.loc:
            print(f"loc: {self.loc}")
    def greet_user(self):
        print(f"\nHello {self.first_name.title()}, welcome back !")

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges= [
        "can add a post",
        "can delete a post",
        "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print(f"\nAdministrator privileges:")
        for privileges in self.privileges:
            print(f"-- {privileges}")      
class ADMIN(USERS):
    def __init__(self, first_name, last_name, login_attempts, privileges, age=None, loc=None):
        super().__init__(first_name, last_name, login_attempts, age, loc)
        self.privileges = Privileges()

admin1 = ADMIN("siva", "gurram", 45, "dallas")
admin1.desc_user()
admin1.greet_user()
admin1.privileges.show_privileges()