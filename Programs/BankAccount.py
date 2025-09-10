class BankAccount:
    def __init__(self,name,account_no,ifsc_code,balance=0):
        self.name=name
        self.account_no=account_no
        self.ifsc_code=ifsc_code
        self.balance=balance
        
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New Balance:${self.balance}"
        else:
            return "Invalid amount deposited."
    
    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            return f"Withdraw ${amount}. New Balance:${self.balance}"
        else:
            return "Insufficient Funds or Invalid Withdraw amount"
    
    def balance_enquiry(self):
        return f"Account Holder: {self.name}\nAccount No:{self.account_no}\nIFSC CODE: {self.ifsc_code}\nBalance: {self.balance}"
        
bank = BankAccount("SG","495349573","000579",10000000)
print(bank.balance_enquiry())
print(bank.deposit(5000000))
print(bank.withdraw(500000))
print(bank.balance_enquiry())