

class parent:

    def __init__(self,Teamname,captain,c_jercyno,age):
        self.Teamname = Teamname
        self.captain = captain
        self.c_jercyno = c_jercyno
        self.age = age
        print("India")


class Child(parent):

    def dispdata(self):
        print("Name Of Team :",self.Teamname)
        print("Captain of Team :",self.captain)
        print("jercey no of Captain :",self.c_jercyno)
        print("Age Of Captain",self.age)

obj1 = Child("India","Viratkolhi",18,33)
obj1.dispdata()