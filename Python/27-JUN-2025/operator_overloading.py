# class ComplexNumber:       #to print the complex number from the parenthesis values like (a,b)
#     def __init__(self,r,i):
#         self.real=r
#         self.imaginary=i
#     def __add__(self, other):
#         return f"{self.real+other.real} + {self.imaginary+other.imaginary}i"
#
# c1=ComplexNumber(5,6)
# c2=ComplexNumber(6,7)
# print(c1+c2)


#testing the grater than operator
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self, other):
        if self.age>other.age:
            return True
        else:
            return False

p1=Person("Sai",20)
p2=Person("Nikhil",18)
if p1>p2:
    print(f"{p1.name} is older than {p2.name}")
else:
    print(f"{p2.name} is older than {p1.name}")