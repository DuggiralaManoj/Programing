class Human:
    def __init__(self,heart):
        self.num_nose=1
        self.num_eye=2
        self.heart=heart
    def work(self):
        print("I can work")
class Man(Human):
    def __init__(self,heart,name):
        Human.__init__(self,heart)
        self.name=name
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can fight")
class Boy(Man):
    def __init__(self,heart,name,can_dance):
        Human.__init__(self,heart)
        Man.__init__(self,heart,name)
        self.can_dance=can_dance
    def flirt(self):
        print("I can flirt")
    def work(self):
        Human.work(self)
        Man.work(self)
        print("I can sing")
boy_1=Boy(1,"sai",True)
boy_1.work()
boy_1.flirt()
print(boy_1.name)
print(boy_1.can_dance)
