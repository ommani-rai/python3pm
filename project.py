"""
parent class: User
    -> user details

child class: Bank
    -> deposit
    -> withdraw
    -> view balance
"""
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def view_details(self):
        print("User Details:")
        print("name: ", self.name)
        print("age: ", self.age)
        print("gender: ", self.gender)

# user = User("shyam", 23, "male")
# user.view_details()


class Bank(User):
    
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def deposit(self, amout):
        self.balance = 0
        self.amount = amout
        self.balance = self.balance + self.amount

        print("Your account is updated. Rs.", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.balance > self.amount:
            self.balance = self.balance - self.amount

            print("You Withdraw Rs.", self.amount)
            print("Your account is reduced by Rs.", self.amount)
            print("Your remaining balace is: ", self.balance)

        else:
            print("Insufficient funds", self.balance)
    
    def view_balance(self):
        self.view_details()
        print("Your Balance: Rs.", self.balance)
        

bank = Bank("ram", 12, "male")
bank.deposit(1000)
bank.withdraw(400)
bank.view_balance()