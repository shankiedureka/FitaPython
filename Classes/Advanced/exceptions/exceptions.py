
#Specific exception for Zerodivision
try:
    a = 10
    b = 0
    c = a/b
    print("Done")
except ZeroDivisionError:
    print("Division by zero is not")
except FileNotFoundError:
    print("File not found")

    
print("Done")

#Generic exception handling
#try:
    #<Logics>
#except Exception as <variable_name>:
    #<Logics>
try:
    a = 10
    b = 10
    c = a/b
    d = 'bharath'
    d = int(d)
    print("Done")
except Exception as e:
    print(e)

print('Done')


#Finally - will execute always, no matter what the issue is
try:
    a = 10
    b = 0
    c = a/b
    # d = 'bharath'
    # d = int(d)
    print("Done")
except Exception as e:
    print(e)
finally:
    print('Done')

#else - it executes if no exeption has hit
try:
    a = 10
    b = 0
    c = a/b
    #results
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print('Done')

#Order
#try - mandatory
#except - mandatory
#else 
#finally

# try:
#     connect to db
#     get results
# except Exception as e:
#     print(e)
#     return None
# else:
#     return results