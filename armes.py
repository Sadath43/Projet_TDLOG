
class Weapons:
    def __init__(self,munition,range):
        self.munition=munition
        self.range=range

    def fire_at(self,x,y,z):
        if munition==0:
            print("NoAmunitionError")
        else munition-=1

class Lance_missiles_antisurface(Weapons):
    def __init__(self):
        super().__init__(self,munition,range):
    def fire_at(self,x,y,z):
        if z==0 || np.sprt(x**2+y**2+z**2)>30:
            print("OutOfRangeError")