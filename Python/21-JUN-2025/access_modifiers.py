class Person:
    def __init__(self,name,roll_no):
        self.name=name
        self.__roll_no=roll_no
    def display(self):
        print(f"My self {self.name} ")
class Human(Person):
    pass

human=Human("Sai",9)
print(human.name)
human.display()
print(human._Person__roll_no)

# print(person_1.name)
# person_1=Person("Shiva")
# person_1.display()
