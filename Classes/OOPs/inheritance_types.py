#Multiple Inheritance - inheriting from multiple parent classes
class vehicle:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print("starting ", self.brand)

class Stop_Vehicle:
    def stop(self):
        print('Stopping the vehicle')

#class class_name(parent_class_name)
class car(vehicle,Stop_Vehicle):
    def honk(self):
        #super will be able to access only the 1st inheritanted class
        super().start()
        self.start()
        print("car is honking")
        self.stop()

kia = car('kia')
kia.honk()

#Multi level inheritance
class grandfather:
    def weight_1(self):
        print('He is 70 kg')
    
class parent(grandfather):
    def weight_2(self):
        print('he is 60kg')
        self.weight_1()

class child(parent):
    def weight_3(self):
        print('He is 50 kg')
        self.weight_1()
        self.weight_2()

c = child()
c.weight_3()


# #Hierchial
class parent:
    def speak_1(self):
        print('he speaks Tamil')

class child_1(parent):
    def speak_2(self):
        print('he speaks tamil and english')

class child_2(parent):
    def speak_3(self):
        print('he speaks tamil, english and kannada')

#Hybrid - combination of two or more inheritance types


class A:
    def show(self):
        print('A')
    def p(self):
        print('Hi')
    

class B(A):
    def show(self):
        print('B')
        super().show()

class C(A):
    def show(self):
        print('C')
        super().show()
        super().p()


obj = B()
obj.show()
