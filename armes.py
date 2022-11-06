import numpy as np
import unittest
class Weapons:
    def __init__(self,munition: int, range :int):
        assert munition >= 0 and munition <= 10, "les munitions doivent etre des entiers compris entre 0 et 10 "
        assert range > 0
        self._munition=munition
        self._range = range

    def fire_at(self,x,y,z):
        assert self._munition > 0, "NoAmunitionError"
        self._munition -= 1

#implementation des armes:
arme=Weapons(5,89)


class LMantisurface (Weapons):
    def __init__(self, munition: int):
        super().__init__(munition, 30)

    def fire_at (self, x:int, y=int, z=int):
        assert self._munition > 0, "NoAmunitionError"
        assert z == 0 and np.sqrt(x**2 + y**2 + z**2) < 30, "OutOfRangeError"
        if z == 0 or np.sqrt(x**2+y**2+z**2) > 30:
            print("OutOfRangeError")
            self._munition -= 1
        else:
            self._munition -= 1


class Lancetorpilles (Weapons):
    def __init__(self, munition: int):
        super().__init__(munition, 20)

    def fire_at(self, x, y, z):
        assert self._munition > 0, "NoAmunitionError"
        assert z <= 0 and np.sqrt(x ** 2 + y ** 2 + z ** 2) < 20, "OutOfRangeError"
        if z > 0 or np.sqrt(x**2 + y**2 + z**2) > 20:
            print("OutOfRangeError")
            self._munition -= 1
        else:
            self._munition -= 1


class LMantiair(Weapons):
    def __init__(self, munition: int):
        super().__init__(munition, 40)

    def fire_at (self,x,y,z):
        assert self._munition > 0, "NoAmunitionError"
        assert z > 0 and np.sqrt(x ** 2 + y ** 2 + z ** 2) < 40, "OutOfRangeError"
        if z <= 0 or np.sqrt(x**2 + y**2 + z**2) > 40:
            print("OutOfRangeError")
            self._munition -=1
        else:
            self._munition -=1

if __name__ == '__main__':
    unittest.main()
