from abc import ABC, abstractmethod

class product(ABC):
    @abstractmethod
    def show(self):
        pass

class IIT(product):
    def show(self):
        print("IIT is a type of College")

class car(IIT):
    def show(self):
        print("Car is a type of product")



obj = IIT()
obj.show()

obj = car()
obj.show()
