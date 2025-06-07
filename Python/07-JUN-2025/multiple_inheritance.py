class Human:
    def __init__(self,hearts):
        self.num_eyes=2
        self.num_nose=1
        self.hearts=hearts
    def work(self):
        print("I can work")
class Man:
    def __init__(self,name):
        self.name=name
    @staticmethod     #by using the static method we can call the method without creating an object
    def flirt():
        print("I can flirt")
    def work(self):
        print("I can dance")
class Boy(Human,Man):
    def __init__(self,name,hearts,language):
        self.language=language
        Man.__init__(self,name)
        Human.__init__(self,hearts)
    @staticmethod
    def eat():
        print("I can eat")
    def work(self):
        print("I can sing")
    def display(self):
        print(f"I am {self.name}, I can teach {self.language}")
boy_1=Boy("Indra",1,"Python")
boy_1.flirt()
Human.work(boy_1)
Boy.eat()
print(boy_1.num_nose)
boy_1.display()