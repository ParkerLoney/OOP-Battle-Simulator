import random
from enemy import Enemy
class Goblin(Enemy):
    def _init__(self, name, color):
        super().__init__(name)
        self.color = color