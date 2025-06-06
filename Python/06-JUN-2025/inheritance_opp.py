class Human:
    def __init__(self,num_hearts):
        self.num_eyes=1
        self.num_nose=2
        self.num_hearts =num_hearts
    def eat(self):
        print("I can Eat")
    def work(self):
        print("I can Work")
class Man(Human):
    def __init__(self,name,hearts):
        super().__init__(hearts)
        self.name=name
    def work(self):
        super().work()
        print("I can Dance")

male_1 = Man("Shiva",1)
male_1.eat()
male_1.work()
print(F"Name is {male_1.name}")
print(F"Number of eye is {male_1.num_eyes}")
print(F"Number of hearts{male_1.num_hearts}")