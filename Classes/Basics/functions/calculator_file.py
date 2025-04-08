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

