# *
# * *
# * * *
# * * * *

#1st - it should have n lines
#2nd - each line the start should increase by 1 and 1st line should be 1 star

# n = int(input("Enter the no. of stars - "))
n = 3
# For number of lines
for i in range(0,n):
    #for printing starts in each line(based of line print no. of stars)
    for j in range(0,i+1):
        print('*',end='')
    print('\n')


# '+' --> concats
# '*' --> 'a' * 2(prints the values with number of times)
for i in range(1,n+1):
    print('#'*i)
    print('\n')
    
