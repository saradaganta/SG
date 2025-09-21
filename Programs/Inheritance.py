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
#print(ice_stand.get_desc())
ice_stand.desc_icecream()