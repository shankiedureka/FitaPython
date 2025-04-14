
#inheritance - inheriting properties and methods from parent to child
class vehicle:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print("starting ", self.brand)

#class class_name(parent_class_name)
class car(vehicle):
    def honk(self):
        #super --> used to access the functions or varaibles
        # in parent class
        print(self.brand)
        super().start()
        print("car is honking")

kia = car('kia')
kia.start()
kia.honk()


#Employee details(name,age,bloodgroup,address)
#Employee working(department,working hours)
# class employee:
#     name = name
#     age = age
#     def get_blood_group():
#         print("blood group is b+ve")
# class working(employee):
#     department = department
#     hours = hours


#single
#multiple
#multi level
#hybrid
#hierchial
