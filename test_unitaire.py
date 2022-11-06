from armes import *
from unittest import TestCase
import numpy

class test_fire_at (TestCase) :
    def test_fire_at_LMantisurface(self):
        lmantisurface = LMantisurface(1)
        lmantisurface.fire_at(1, 2, 0)
        self.assertEqual(0, lmantisurface._munition, "lmantisurface didn't fire")


    def test_fire_at_LMantiair(self):
        lmantiair = LMantiair(2)
        lmantiair.fire_at(1, 2, 3)
        self.assertEqual(1, lmantiair._munition, "lmantiair didn't fire")

    def test_fire_at_Lancetorpilles(self):
        lancetorpilles = Lancetorpilles(3)
        lancetorpilles.fire_at(1, 2, -3)
        self.assertEqual(2, lancetorpilles._munition, "lancetorpille didn't fire")





if __name__=='__main__':
    unittest.main()