#polymorphism means it has many form. It allows methods to perform different
#task based on object

#method overriding
class Bird:
    def sound(self):
        print('Some generic sounds')

class Parrot(Bird):
    def sound(self):
        print('Parrot says : Hello')

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chips")

p = Parrot()
p.sound()

s = Sparrow()
s.sound()

b = Bird()
b.sound()


