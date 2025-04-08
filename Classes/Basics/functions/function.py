#function definition
#function call

#function definition
#def <functionname>(args):

#Dynamic
def calculator(val1, val2, op):
    if op == '+':
        print(val1+val2)
    elif op == '-':
        print(val1-val2)
    elif op == '*':
        print(val1*val2)
    elif op == '/':
        print(val1/val2)
    else:
        print("Not supported")

    print("Done")


a = 10
b = 20
operator = '+'
a = int(a)
b = int(b)
calculator(a,b,operator)

print("Square the value a")
print(a**2)

c = 5
d = 2
oper = '*'
c = int(c)
d = int(d)
calculator(c,d,oper)