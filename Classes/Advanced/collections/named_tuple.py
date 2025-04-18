#Collection is python module which provide extra powerful data structures beyond
#built in types like list or tuple 

#Named tuple
#combination of both tuple and dictionary
#I can send data in dictionary format but it is not mutable
#tuple - immutable(1,2,3,4)

from collections import namedtuple

#define a named tuple
#tuple_name = namedtuple(<tuple_name>,[<key>,<key>])
Person = namedtuple("Person",['name','age','city'])

#create an instance
p1 = Person(name = "Bharath", age = 25, city = 'Chennai')
p2 = Person(name = "Kumar", age = 25, city = 'Kochin')

# print(p1)
# print(p2)
# print(type(p1))
print(p1.name)
print(p1.age)
print(p1.city)
