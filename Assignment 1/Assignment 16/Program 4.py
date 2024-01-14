

class parent:

    def __init__(self,attribute):
        self.attribute = attribute


    def display(self):
        print("In Parent attribute method",self.attribute)

class child(parent):

    def display(self):

        print("In Child attribute method",self.attribute)

ret1 = child("shubham")
ret1.display()

