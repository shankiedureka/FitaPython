a = [1,2,3,4,5,6,7]

output = []
for i in a:
    if i < 5:
        i = i**2
        output.append(i)
print(output)

#The output will be always a list
#Efficient because i don't wanna create new list variable
#output_list = [expression for i in <list,tuple,set,dict>]
# a = [i**2 for i in a]
# print(a)

#adding conditional checks
#output_list = [expression for i in <list,tuple,set,dict> if i<5]
a = [i**2 for i in a if i<5]
print(a)