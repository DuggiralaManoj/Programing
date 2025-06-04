class Instructor:
    followers=0                   #class object variable
    def __init__(self,name,age):  #special method
        self.name = name          #attributes
        self.age = age
    #the hobie only accept the string not the attribute or a object
    def display(self,hobie):            #method
        print(f"Hey I am {self.name} and I do {hobie}")   #no need to use self. for method that is only for attributes

    def update_fallowers(self,follower_name):
        self.followers +=1

instructor = Instructor('teja',21)  #object
print(instructor.name)
instructor.display("dance")
instructor.update_fallowers("ravi")
instructor.update_fallowers("raju")
print(instructor.followers)

