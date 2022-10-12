
class Weapons:
    def __int__(self,munition,range):
        self.munition=munition
        self.range=range

    def fire_at(self,x,y,z):
        if munition==0:
            print("NoAmunitionError")
        else munition-=1

