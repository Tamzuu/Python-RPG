class Enemy:
    def __init__(self, app, name, level,  health, weapon, damage):
        self.app = app
    
        self.name = name
        self.level = level
        self.health = health
        self.weapon = weapon
        self.damage = damage


    def take_damage(self):
        self.health -= self.app.player.damage

    
    def attack(self):
        self.app.player.health -= self.damage
        

class Orc(Enemy):
    def __init__(self, app: object, name: str = "Unknown", health: int = 100, weapon: str = "fists", damage: int = 3, level: int = 1):
        super().__init__(app, name, level, health, weapon, damage)
        self.health = 100
        self.damage = 10
        self.race = __class__.__name__
