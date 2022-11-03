import armes
import numpy as np
import unittest
from armes import *
class Vessel:
    def __init__(self, coordinate: tuple, max_hits: int, weapon):
        self.coordinate = coordinate
        self.max_hits = max_hits
        self.weapon = weapon

    def go_to(self, x: float, y: float, z: float):
        print("move to{x, y}")

    def get_coordinate(self, x: float, y: float, z: float):
        self.coordinate = (x, y, z)

    def fire_at(self, x, y, z):
        assert self.max_hits !=0, "Destroyed Error"
        print("fire at (x, y ,z)")

class cruisier (Vessel):
    def __init__(self, coordinate, max_hits, antiair:Weapons):
        super().__init__(self, coordinate, 6,antiair)
    def get_coordinates(self, x ,y ,z):
        assert z==0, "out of surface"
        self.coordinate=tuple(x, y, z)
    def go_to(self, x, y, z):
        assert z==0, "cant move out the surface"
    def fire_at (self, x, y, z):
        assert self.max_hits!=0, "Destroyed Error"
        rayon=(self.coordinate [0]-x)**2+(self.coordinate[1]-y)**2+(self.coordinate[2]-z)**2
        assert rayon < self.weapon.range, "out of range Error"
        if rayon >self.weapon.range: self.weapon.munition-=1


class submarine(Vessel):
      def __init__(self, coordinate, max_hits, lance_torpille):
           super().__init__(self, coordinate, 2, lance_torpille)
      def get_coordinates(self, x, y, z):
           assert z == -1 or z==0, "out of surface"
           self.coordinates = tuple(x, y, z)
      def go_to(self, x, y, z):
           assert z == 0 or z==-1, "cant move out the surface"
           self.get_coordinates(x, y, z)
      def fire_at(self, x, y, z):
          assert self.max_hits != 0, "Destroyed Error"
          rayon = (self.coordinate[0] - x) ** 2 + (self.coordinate[1] - y) ** 2 + (self.coordinate[2] - z) ** 2
          assert rayon < self.weapon.range, "out of range Error"
          if rayon > self.weapon.range: self.weapon.munition-=1


class Fregate (Vessel):
    def __init__(self, coordinate, max_hits, lance_missile_antisurface):
        super().__init__(self, coordinate, 5, lance_missile_antisurface)
    def get_coordinates(self, x, y, z):
         assert z == 0, "out of surface"
         self.coordinates = tuple(x, y, z)
    def go_to(self, x, y, z):
        assert z == 0, "cant move out the surface"
        print("move to{x, y}")
    def fire_at(self, x, y, z):
         assert self.max_hits != 0, "Destroyed Error"
         rayon = (self.coordinate[0] - x) ** 2 + (self.coordinate[1] - y) ** 2 + (self.coordinate[2] - z) ** 2
         assert rayon < self.weapon.range, "out of range Error"
         if rayon >self.weapon.range: self.weapon.munition-=1


class Destroyer(Vessel):
    def __init__(self, coordinate, max_hits, lance_torpille: Lancetorpilles):
        super().__init__(self, coordinate, 4, lance-torpille)
    def get_coordinates(self, x, y, z):
        assert z == 0, "out of surface"
        self.coordinates = tuple(x, y, z)
    def go_to(self, x, y, z):
        assert z == 0, "cant move out the surface"
        print("move to{x, y}")

    def fire_at (self, x, y, z):
        assert self.max_hits != 0, "Destroyed Error"
        rayon = (self.coordinates[0] - x) ** 2 + (self.coordinate[1] - y) ** 2 + (self.coordinate[2] - z) ** 2
        assert rayon < self.weapon.range, "out of range Error"
        if rayon >self.weapon.range: self.weapon.munition-=1


    class Aircraft (Vessel):
        def __init__(self, coordinate, max_hits, lance_missile_antisurface):
            super().__init__(self, coordinate, 1, lance_missiles_antisurface)
        def get_coordinates(self, x, y, z):
            assert z == 1, "out of surface"
            self.coordinates = tuple(x, y, z)
        def go_to (self, x, y, z):
            assert z == 1, "cant move out the surface"
            print("move to{x, y}")
        def fire_at(self, x, y, z):
            assert self.max_hits != 0, "Destroyed Error"
            rayon = (self.coordinate[0] - x) ** 2 + (self.coordinate[1] - y) ** 2 + (self.coordinate[2] - z) ** 2
            assert r <self.weapon.range, "out of range Error"
            if rayon >self.weapon: self.weapon.munition-=1


class joueur_space:
    def __init__(self, liste_des_vaisseaux:list):
        self.liste_des_vaisseaux=liste_des_vaisseaux

    def add_vessel (vaisseau: Vessel):
        self.liste_des_vaisseaux.append(vaisseau)


if __name__=='__main__':
    unittest.main()

