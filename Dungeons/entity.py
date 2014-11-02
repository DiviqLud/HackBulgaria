from weapon import Weapon

class Entity():
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = None

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def get_health(self):
        return self.health

    def take_damage(self, damage_points):
        if damage_points < self.health:
            self.health -= damage_points
            return self.get_health()
        else:
            self.health = 0
            return self.health

    def take_healing(self, healing_points):
        if not self.is_alive():
                return False
        if self.get_health() + healing_points > self.max_health:
            self.health = self.max_health
        else:
            self.health += self.max_health
        return True

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def has_weapon(self):
        if self.weapon != None:
            return True
        else:
            return False

    def attack(self):
        if self.has_weapon():
            if self.weapon.critical_hit():
                return self.weapon.damage*2
            else:
                return self.weapon.damage
        else:
            return 0
