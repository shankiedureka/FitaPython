#Loops - do the repetetive tasks
#while and for
#while - infinite times
#while starting a program, i doesn't know how many iterations i need 
#to perform


#1 to 10
#syntax
#while <condition>(boolean):
    #Logic

#Should have condition at which it fails
# a = 10
# count = 0
# while count < a:
#     print(count)
#     count = count + 1
# print('Done')

#using break conditions
# a = 10
# count = 0
# while True:
#     if count == 10:
#         break
#     print(count)
#     count = count + 1
    
# print('Done')


while True:
    a = input("Enter value 1 - ")
    b = input("Enter value 2 - ")
    print('Enter "stop" to exit the calculator application')
    print("Operators supported is + , - , * , /")
    operator = input("Enter Operator - ")

    a = int(a)
    b = int(b)
   
    if operator == '+':
        print(a+b)
    elif operator == '-':
        print(a-b)
    elif operator == '*':
        print(a*b)
    elif operator == '/':
        print(a/b)
    elif operator == 'stop':
        break
    else:
        print("Not supported")

print("Done")
