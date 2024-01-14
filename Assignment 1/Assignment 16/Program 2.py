
class parent_vehicle:
    
    def __init__(self,brand,model,year,speed):
        self.Brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self,accelerate):
        self.accelerate = accelerate
        print("In Parent:accelerate",self.accelerate)

    def brake(self,brake):
        self.brake = brake

    def honk(self,honk):
        self.honk = honk
        print("In honk Parent",self.honk)



class child_vehicle (parent_vehicle):

    def accelerate(self,accelerate):
        self.accelerate = accelerate
        print("In Child accelerate",self.accelerate)

    def honk(self,honk):
        self.honk = honk
        print("In honk Child", self.honk)


retObj1 = parent_vehicle("Fararri","01","2001",430)
retObj1.accelerate(500)
retObj1.honk("Turrrrrr   Turrrrrr")

ret = child_vehicle("Rolls_Royce",11,2024,501)
ret.accelerate(100)
ret.honk("Wrooooom    Wrooooom")
