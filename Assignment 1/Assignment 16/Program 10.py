
class Vehicle :

    def __init__(self,Brand,Model,Milage):
        self.Brand = Brand
        self.Model = Model
        self.Milage = Milage

    def DispData(self):
        print("Brand Of Bike : ",self.Brand)
        print("Model OF Bike : ",self.Model)
        print("Milage Of Bike :",self.Milage)

class Bike(Vehicle):

    pass

obj = Bike("Intercepter",650,30)
obj.DispData()
