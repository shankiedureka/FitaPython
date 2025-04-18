def square(x):
    return x**2

print(square(2))
print(square(3))

#lambda functions - anonymous function
# syntax
# lambda arguments : expression

#rule
#it takes multiple arguments
#but it performs only 1 expression
square_lambda = lambda x : x**2 
print(square_lambda(4))

sum_lambda = lambda a,b : a+b
print(sum_lambda(10,20))
