from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,n):
        self.number_of_tyres=n
    @abstractmethod
    def start(self):
        pass

    def display(self):
        print("Hi I am calling from vehicle class")
