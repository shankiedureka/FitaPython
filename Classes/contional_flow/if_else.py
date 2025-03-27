a = input()
b = input()

operator = input()

a = int(a)
b = int(b)

#Syntax
# if <condition>:
#     Logic
#     logics
# elif <condition>:
#     Logics
# elif <conditions>:
#     Logics
# else:
#     Logics



if operator == '+':
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    print(a/b)
else:
    print("Not supported")

print("Done")
