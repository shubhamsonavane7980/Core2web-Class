

class parent:

    def __init__(self,apple):
        self.apple = apple
        print(self.apple)

    @classmethod
    def name(self,name):
         self.name = name
         print("Name is : ",self.name)


    @staticmethod
    def age(age):
         parent.age = age
         print("Age Is :", parent.age)


class child(parent):
    pass

obj1 = child("laptop brand")
obj1.name("Shubham")
obj1.age(22)