#4 default data structures
#Linked list , queue, stack
#list tuple set dictionary
#data Structure - How we store the data in memory,
#we can retrive and use them in optimal time and optimal memory

#List - similar to arrays
a = []
a = [1,2,3,4,5,6]
a = [12.5,23.8]
a = ['bha','kk']
a = [1,23.5,'bha']

#List is mutable(make alterations)
#insert
a = [1,2,3,4,5]
a.append(6)
print(a)

#delete
#deletes based on value in list
a.remove(2)
print(a)
#this removes based on index
a.pop(4)
print(a)


#List is ordered
a = ['bha','kum','s','ygyg']
print(a[1])

#it supports duplicates
a = [1,1,1,1,1,1]
print(a)

for i in a:
    print(i)



