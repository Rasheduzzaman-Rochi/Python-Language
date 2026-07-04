class ATM:
    def __init__(self, balance):
        self._balance = balance
    
    def check_balance(self):
        print(self._balance)
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        self._balance -= amount

atm1 = ATM(200)
atm1.check_balance()
atm1.deposit(50)
atm1.check_balance()
atm1.withdraw(30)
atm1.check_balance()