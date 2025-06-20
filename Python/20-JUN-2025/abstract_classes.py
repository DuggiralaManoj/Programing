from abstraction import Vehicle

class Bike(Vehicle):
    def __init__(self,n,colour):
        super().__init__(n)
        self.colour=colour
    def start(self):
        print("Start with kick")
class Scooty(Vehicle):
    def start(self):
        print("Start with self")
class Car(Vehicle):
    def start(self):
        print("Start with key")
