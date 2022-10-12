
from armes import Weapons
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
        print("fire at")


