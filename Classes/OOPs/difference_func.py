def create_account(owner, balance=0):
    return {"owner": owner, "balance": balance}

def deposit(account, amount):
    account["balance"] += amount
    return account
def deposit(account, amount):
    account["balance"] += amount
    return account
def withdraw(account, amount):
    if amount > account["balance"]:
        return "Insufficient funds"
    account["balance"] -= amount
    return account



# Use the functions
account = create_account("Bharath", 1000)

account = deposit(account, 500)  
print(account["balance"])      

account = withdraw(account, 300)
print(account["balance"])      

result = withdraw(account, 2000)
print(result)

#Functional programming over OOPS
#If you don't need to manage state/data 
#if you want clean code