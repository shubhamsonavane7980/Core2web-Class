
class Demo:

    def __init__(self,Num):
        self.Num = Num

    def __del__(self):
        print("In Destructor")


obj1 = Demo(11)
obj2 = Demo(22)
obj3 = Demo(33)
obj4 = Demo(44)

obj1 = obj3

del obj2


