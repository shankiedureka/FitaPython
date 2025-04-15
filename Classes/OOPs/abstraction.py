#abstraction - hiding the implemntation details and showing only
#the essential features 

#module name is abc
from abc import ABC, abstractmethod

#We need abstract class
#we need concrete class
#Abstract class
#ABstract method

#Abstract class
#should inherit from ABC class
#It should not have any logics for its methods
#It should have the methods in abstractmethod form and use 
#@abstractmethod before the functions
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

#Concrete class
#Write implementation functions for all abstract mmethods
class car(Vehicle):
    def start_engine(self):
        print('Staring the car')
    def stop_engine(self):
        print('Stopping the car')

obj = car()
obj.start_engine()


# @check
# def calculator(a,b,op):
#     print(a+b)

# calculator(a,b,op)

# def check(a,b):
#     if type(a) == int:
#         return a
