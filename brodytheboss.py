from enemy import Enemy
class Brody(Enemy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.color = color
        self.health = 200
        self.attack_power = 25

    def attack(self):
        return super().attack() + 10