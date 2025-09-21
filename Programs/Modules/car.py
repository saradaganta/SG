class Car:
    def __init__(self,make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_desc_name(self):
        longname = f"{self.year} {self.make} {self.model}"
        return longname.title()
    
    def read_odometer(self):
        print(f"This cas has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, miliage):
        if miliage >= self.odometer_reading:
            self.odometer_reading = miliage
        else:
            print("You can't roll back odometer reading..!")
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    def desc_battery(self):
        print(f"This car has a {self.battery_size} -- Kwh battery")
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 270
        print(f"This car can go about {range} miles on full charge")
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery=Battery()
