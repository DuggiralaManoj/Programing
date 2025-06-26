class Duck:
    def quack(self):
        print("I can quack")
class Human:
    def quack(self):
        print("I can quack like a duck")
class Dog:
    def bark(self):
        print("I can bark")

class Obj:
    def display(self,obj):
        obj.quack()

# def display(obj):
#     obj.quack()

d=Duck()
h=Human()
dog=Dog()
# display(dog)

o=Obj()          #these were used when class is created without class these don not work
o.display(d)
o.display(h)
o.display(dog)