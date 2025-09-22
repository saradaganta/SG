from user import *
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