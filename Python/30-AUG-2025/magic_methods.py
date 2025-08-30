# l1=[1,2,3]
# print(len(l1))
# print(l1)

class Auther:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} of {self.name}"
    def __call__(self, *args, **kwargs):
        print(f"{self.age}")
    def __del__(self):
        print("Calling before deleting")
a1=Auther("sai",20)
print(a1)
a1()
del a1
print(a1)