

class Player:
    def __init__(self, name:str = "Unknown", health:int = 100, damage:int = 10, weapon:str = "fists", level:int = 1, xp:int = 0):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.level = level
        self.xp = xp
        self.max_health = health