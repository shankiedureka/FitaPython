#Dynamic
#Getting input from user
a = input("Enter only int values")
b = input()

#Type conversion
#converting one datatype to another
# a = int(a)
# a = str(a)
# a = float(a)

#Only if the string is digit
#string --> int
#string --> float
#if it is not a digit, type conevrsion is not possible

#int --> string
#float --> string

#int --> float
#float --> int(not possible)
a = int(a)
b = int(b)
c = a + b
#Formatting the string
print("The addition value is " + str(c) + ",input 1 is" + str(a) + 'and input is ' + str(b))
print("The addition value is {0},input 1 is {1} and input is {2}  ".format(c,a,b))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
# 5 + 2
# "bhar" + "arath" --> 'bhararath'
