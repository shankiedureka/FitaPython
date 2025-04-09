class BankAccount:
    #constructor
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        bharath.balance
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance


# Create an account
bharath = BankAccount("Bharath", 1000)

print(bharath.deposit(500))  

Shamil = BankAccount('Shamil',1000)

print(Shamil.deposit(500))  



#Class groups data and functions together
#You don't need to manage the data and logic seperately
#Scalability
#OOPs will be used mostly for large scale applications(banking)

#Self
#self refers to current instance of class