#procedural programming
#Functional programming

#Procedural
#Variables and datatypes
#if else
#loops

#Functional programming
#Functions
#Modules

#OOPs -  Object Oriented Programming
#class - Blueprint or Template
#Object - Instance of a class

#class have attributes and methods
#attributes - variables
#methods - functions

#class <name>:
    #<code>
class car:
    #attributes
    color = ''

    #methods
    def manuafacture(self):
        print("The car has manuafactured in color - ", self.color)
    def wow(self):
         if self.color == 'red':
              print('wow')

#object_name(any varaible) = class_name()
usr_1 = car()
usr_1.color = 'red'
usr_1.manuafacture()

usr_2 = car()
usr_2.color = 'Blue'
usr_2.manuafacture()


usr_1.wow()
usr_2.wow()





