class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def work(self):
        print("I can work")
    def display(self):
        print(f"I am {self.name} I'm {self.age} years old")
class Man(Human):
    def __init__(self,name,age,location):
        Human.__init__(self,name,age)
        self.location=location
    def eat(self):
        print("I can eat")
    def work(self):
        Human.work(self)
        print("I can swim")
class Women(Human):
    def __init__(self,name,age,can_dance):
        Human.__init__(self,name,age)
        self.can_dance=can_dance
    def sleep(self):
        print("I can sleep")
    def main_display(self):
        Human.display(self)
        print(f"know dance :{self.can_dance}")
man_1=Man("Teja",20,"Hyd")
man_1.work()

women_1=Women("Teja",20,True)
women_1.work()

women_1.main_display()