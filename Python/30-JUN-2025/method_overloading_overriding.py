# class Demo:
#     def add(self,a,b,c=0):
#         return a+b+c
# d1=Demo()
# print(d1.add(1,2))
# print(d1.add(2,3,4))

# class Demo:
#     def add(self,*args):
#         total=0
#         for i in args:
#             total +=i
#         return total
# d1=Demo()
# print(d1.add(1,2))
# print(d1.add(2,3,4,5))

class Father:
    def sleep(self):
        print("Sleeps at 10 pm")
    def eat(self):
        print("Eat")
class Sun(Father):
    def sleep(self):
        print("Sleeps at 2 am")
        super().sleep()
raju=Sun()
raju.sleep()



