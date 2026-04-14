class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance =balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
    def show_balance(self):
        print(f"{self.owner} has {self.balance}")
acc = BankAccount ("John",1000)
acc.deposit(500)
acc.withdraw(200)
acc.show_balance()