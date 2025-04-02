#two types of variables
#Global - Creating the variables outside a function
#Local - creating a variables inside a function


def calculator(val1, val2, op):
    
    if op == '+':
        c = val1 + val2
        print(val1+val2)
    elif op == '-':
        c = val1 - val2
        print(val1-val2)
    elif op == '*':
        c = val1 * val2
        print(val1*val2)
    elif op == '/':
        c = val1 / val2
        print(val1/val2)
    else:
        print("Not supported")

    return c
    print("Done")


a = 10
b = 20
operator = '+'
a = int(a)
b = int(b)
#variable_to store return value
result = calculator(a,b,operator)

print("Square the value a")
print(result**2)

c = 5
d = 2
oper = '*'
c = int(c)
d = int(d)
calculator(c,d,oper)