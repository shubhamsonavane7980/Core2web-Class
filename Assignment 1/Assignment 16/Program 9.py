
class animal:

    def __init__(self,alien):
        self.alien = alien
        print("Name Of The Alien : ",self.alien)
    @classmethod
    def wild_Animals(self,Tiger):
        self.Tiger = Tiger
        print("Wild Animal Are : ",self.Tiger)
    @staticmethod
    def pet_Animals(Cat):
        animal.Cat = Cat
        print("Pet Animals Are : ",animal.Cat)

obj1 = animal("Apes")
obj1.wild_Animals("Tigris")
obj1.pet_Animals("Selam")






