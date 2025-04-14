#Encapsulation ---> prevents direct access to some variables and functions
class BankAccount:
    #constructor
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
    
   
    def __change_balance(self,amount):
        self.__balance = self.__balance + amount
    
    #getter function
    def get_balance(self,pin):
        if pin == '1234':
            return self.__balance
        else:
            return None

    #setter function
    def deposit(self, amount):
         #setter function
        self.__change_balance(amount)

    #setter function
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__change_balance(-amount)

user_1 = BankAccount('Kumar',1000)
user_1.deposit(2000)
#this function can't be called directly from object
user_1.__change_balance(3000)
#this balance variable is also not accessible
print(user_1.__balance)
bal = user_1.get_balance(2341)
print(bal)


#I have a private function
#Getter function and setter function
#Getter function - used to get the values from private variable or function
#Setter function - used to access the private variable or function

