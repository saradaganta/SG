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