class Person:
    def __init__(self,name,roll_no,age):
        self.name=name
        self.__roll_no=roll_no
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age >35:
           print("Error you should enter more than 35")
        else:
            self.__age=age
    def display(self):
        print(f"My self {self.name} with roll number {self.__roll_no}  age of {self.__age} ")

p1=Person("sai",9,20)
print(p1.get_age())
p1.set_age(34)
print(p1.get_age())
p1.display()

