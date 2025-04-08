#Types of arguments in Python
#1. Positional arguments
#It takes the order of arguments
#you should follow the same order of arguments how the function is defined

# # #The len of arguments should be same in function def and call
# def cal(a,b,op):
#     if op == '+':
#         print(a+b)
#     else:
#         print("Not supported")

# cal(1,2,'+')
# cal('+',1,2)

# #Keyword Arguments
# # cal(a=1, b=2, op='+')
# cal(op='+',a=1)

# #Default arguments
# def sum(a,b,op='+'):
#     if op == '+':
#         print(a+b)
#     else:
#         print("Not supported")

# sum(1,2,'-')
# sum(1,2)

#Variable length arguments
def sum(*a):
    sum = 0
    for i in a:
        sum = sum + i
    print(sum)

sum(1,2,3,4,5,7,0)
sum(1,2)
sum(2,6,8,9,10,26,34,9)


def sum(a):
    sum = 0
    for i in a:
        sum = sum + i
    print(sum) 

lis = [1,2,3,4,5,6,7,8,0]
sum(lis)
