import numpy as np
class Weapons:
    def __init__(self,munition,range):
        self._munition=munition
        self._range=range

    def fire_at(self,x,y,z):
        if _munition==0:
            print("NoAmunitionError")
        else:
             _munition=_minition-1

#implementation des armes:
Lance_missiles_antisurface=Weapons(40,30)

"""
class Lance_missiles_antisurface(Weapons):
    def __init__(self):
        super().__init__(self,munition,range):
    def fire_at(self,x,y,z):
        if z==0 or np.sprt(x**2+y**2+z**2)>30:
            print("OutOfRangeError")
"""


