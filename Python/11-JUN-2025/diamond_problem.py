class A:
    def work(self):
        print("I can work")
class B(A):
    def work(self):
        print("I can dance")
class C(A):
    def work(self):
        print("I can sing")
class D(B,C):
    def work(self):
        print("I can do")

d1=D()
d1.work()
print(D.mro())



