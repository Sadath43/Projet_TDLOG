import armes
import numpy as np
import unittest
from armes import *
class Vessel:
    def __init__(self, coordinate: tuple, max_hits: int, weapon: Weapons):
        self.coordinates = coordinate
        self.max_hits = max_hits
        self.weapon = weapon

    def go_to(self, x: float, y: float, z: float):
        pass

    def get_coordinate(self, x: float, y: float, z: float):
        self.coordinates = (x, y, z)

    def fire_at(self, x, y, z):
        assert self.max_hits != 0, "Destroyed Error"
        print("fire at (x, y ,z)")

class Cruisier (Vessel):
    def __init__(self,x,y,z):
        c= (x,y,z)
        super().__init__(c, 6, LMantiair())
    def get_coordinates (self, x ,y ,z):
        assert z == 0, "out of surface"
        self.coordinates = (x, y, z)
    def go_to (self, x, y, z):
        assert z == 0, "cant move out the surface"
        self.coordinates = (x, y, z)
    def fire_at (self, x, y, z):
        assert self.max_hits != 0, "Destroyed Error"
        rayon = (self.coordinates[0]-x)**2+(self.coordinates[1]-y)**2+(self.coordinates[2]-z)**2
        assert rayon < self.weapon._range, "out of range Error"
        self.weapon._munition -= 1



class Submarine(Vessel):
      def __init__(self,x,y,z):
           super().__init__((x,y,z) , 2, Lancetorpilles())
      def get_coordinates(self, x, y, z):
           assert z == -1 or z==0, "out of surface"
           self.coordinates = (x, y, z)
      def go_to(self, x, y, z):
           assert z == 0 or z==-1, "cant move out the surface"
           self.get_coordinates(x, y, z)
      def fire_at(self, x, y, z):
          assert self.max_hits != 0, "Destroyed Error"
          rayon = (self.coordinates[0] - x) ** 2 + (self.coordinates[1] - y) ** 2 + (self.coordinates[2] - z) ** 2
          assert rayon < self.weapon._range, "out of range Error"
          self.weapon._munition-=1



class Fregate (Vessel):
    def __init__(self, x,y,z):
        super().__init__((x,y,z), 5, LMantisurface())
    def get_coordinates (self, x, y, z):
         assert z == 0, "out of surface"
         self.coordinates = (x, y, z)
    def go_to(self, x, y, z):
        assert z == 0, "cant move out the surface"
        self.get_coordinates(x,y,z)
    def fire_at(self, x, y, z):
         assert self.max_hits != 0, "Destroyed Error"
         rayon = (self.coordinates[0] - x) ** 2 + (self.coordinates[1] - y) ** 2 + (self.coordinates[2] - z) ** 2
         assert rayon < self.weapon._range, "out of range Error"
         self.weapon._munition-=1


class Destroyer(Vessel):
    def __init__(self,x,y,z):
        lancetorpilles = Lancetorpilles()
        super().__init__((x,y,z), 4, lancetorpilles )
    def get_coordinates(self, x, y, z):
        assert z == 0, "out of surface"
        self.coordinates = (x, y, z)
    def go_to(self, x, y, z):
        assert z == 0, "cant move out the surface"
        self.get_coordinates(x,y,z)

    def fire_at (self, x, y, z):
        assert self.max_hits != 0, "Destroyed Error"
        rayon = (self.coordinates[0] - x) ** 2 + (self.coordinates[1] - y) ** 2 + (self.coordinates[2] - z) ** 2
        assert rayon < self.weapon._range, "out of range Error"
        self.weapon._munition-=1


class Aircraft (Vessel):
    def __init__(self, x,y,z):
        super().__init__((x,y,z), 1, LMantisurface())
    def get_coordinates(self, x, y, z):
        assert z == 1, "out of surface"
        self.coordinates = (x, y, z)
    def go_to (self, x, y, z):
        assert z == 1, "cant move out the surface"
        self.coordinates = (x, y, z)
    def fire_at(self, x, y, z):
        assert self.max_hits != 0, "Destroyed Error"
        rayon = (self.coordinates[0] - x) ** 2 + (self.coordinates[1] - y) ** 2 + (self.coordinates[2] - z) ** 2
        assert rayon <self.weapon._range, "out of range Error"
        self.weapon._munition-=1


class Joueur_space:
    def __init__(self, liste_des_vaisseaux=[]):
        self.liste_des_vaisseaux=liste_des_vaisseaux

    def add_vessel (self, vaisseaux: Vessel):
        self.liste_des_vaisseaux.append(vaisseaux)

    def recevoir_coup (self, x,y,z):
        assert x>=0 and x<=100 and y>=0 and y<=100 and (z==1 or z==-1), "Out of Joueur_space"
        for vessel in self.liste_des_vaisseaux:
            if vessel.coordinates == (x, y, z):
                return 0

        return 1

if __name__=='__main__':
    unittest.main()

