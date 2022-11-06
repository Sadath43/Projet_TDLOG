from armes import *
from unittest import TestCase
from vaisseau import *
import numpy

class test_weapons_fire_at (TestCase) :
    def test_fire_at_LMantisurface(self):
        lmantisurface = LMantisurface()
        lmantisurface.fire_at(1, 2, 0)
        self.assertEqual(21, lmantisurface._munition, "lmantisurface didn't fire")


    def test_fire_at_LMantiair(self):
        lmantiair = LMantiair()
        lmantiair.fire_at(1, 2, 3)
        self.assertEqual(21, lmantiair._munition, "lmantiair didn't fire")

    def test_fire_at_Lancetorpilles(self):
        lancetorpilles = Lancetorpilles()
        lancetorpilles.fire_at(1, 2, -3)
        self.assertEqual(21, lancetorpilles._munition, "lancetorpille didn't fire")



class test_vessel_go_to (TestCase) :
    def test_Cruisier_go_to (self):
        cruisier= Cruisier(1,2,0)
        cruisier.go_to(0,0,0)
        self.assertEqual((0,0,0), cruisier.coordinates, " Cruisier don't move-")
    def test_Submarine_go_to (self):
        submarine= Submarine(1,2,0)
        submarine.go_to(2,3,0)
        self.assertEqual((2,3,0), submarine.coordinates, " Submarine don't move-")
    def test_Fregate_go_to (self):
        fregate = Fregate(1,2,0)
        fregate.go_to(2,3,0)
        self.assertEqual((2, 3, 0), fregate.coordinates , " fregate don't move-")
    def test_Destroyer_go_to(self):
        destroyer = Destroyer(1,2,0)
        destroyer.go_to(4,4,0)
        self.assertEqual((4, 4, 0), destroyer.coordinates, " destroyer don't move-")


    def test_Aircraft_go_to(self):
        aircraft= Aircraft(1,2,1)
        aircraft.go_to(1,5,1)
        self.assertEqual((1, 5, 1), aircraft.coordinates, " aircraft don't move-")
class test_vessel_fire_at(TestCase):
    def test_Cruisier_fire_at(self):
        cruisier = Cruisier(1, 2, 0)
        cruisier.fire_at(4,2,0)
        self.assertEqual(21, cruisier.weapon._munition, " fregate don't fire-")
    def test_Submarine_fire_at(self):
        submarine = Submarine(1, 2, -1)
        submarine.fire_at(0,2,-1)
        self.assertEqual(21, submarine.weapon._munition, " submarine don't fire-")
    def test_Fregate_fire_at(self):
        fregate = Fregate(1, 2, 3)
        fregate.fire_at(2, 2, 3)
        self.assertEqual(21, fregate.weapon._munition, " fregate don't fire-")
    def test_Destroyer_fire_at(self):
        destroyer = Destroyer(1, 2, 0)
        destroyer.fire_at(1, 2, 0)
        self.assertEqual(21, destroyer.weapon._munition, " destroyer don't fire-")
    def test_Aircraft_fire_at(self):
        aircraft = Aircraft (1, 2, 3)
        aircraft.fire_at(6, 2, 3)
        self.assertEqual(21, aircraft.weapon._munition, " aircraft don't fire-")

if __name__=='__main__':
    unittest.main()