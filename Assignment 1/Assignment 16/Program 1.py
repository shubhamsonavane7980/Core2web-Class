

class Human:
    def __init__(self,name,age):
        print("In Demo Constructor")
        self.name = name
        self.age = age
    def informaction(self):
        print("Name Is : ",self.name)
        print("Age is :",self.age)

name = input("Enter Name :")
age = int(input("Enter Age :"))

if __name__ == "__main__" :
    obj1 = Human(name,age)
    obj1.informaction()