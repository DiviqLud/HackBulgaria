import random


class Fight():
    def __init__(self, fight_hero, fight_orc):
        self.fight_orc = fight_orc
        self.fight_hero = fight_hero

    def flip_coin(self):
        if random.random() < 0.5:
            return self.fight_hero
        else:
            return self.fight_orc

    def simulate_fight(self):
        if not self.fight_hero.has_weapon() and not self.fight_hero.has_weapon():
            return "Go get weapons"
        if self.flip_coin() == self.fight_hero:
            while self.fight_orc.is_alive() and self.fight_hero.is_alive():
                self.fight_orc.take_damage(self.fight_hero.attack())
                print("{} take {} from {}".format(self.fight_orc.name, self.fight_hero.attack(), self.fight_hero.name))
                if not self.fight_orc.is_alive():
                    break
                self.fight_hero.take_damage(self.fight_orc.attack())
                print("{} take {} from {}".format(self.fight_hero.name, self.fight_orc.attack(), self.fight_orc.name))

        else:
            while self.fight_orc.is_alive() and self.fight_hero.is_alive():
                self.fight_hero.take_damage(self.fight_orc.attack())
                print("{} take {} from {}".format(self.fight_hero.name, self.fight_orc.attack(), self.fight_orc.name))
                if not self.fight_hero.is_alive():
                    break
                self.fight_orc.take_damage(self.fight_hero.attack())
                print("{} take {} from {}".format(self.fight_orc.name, self.fight_hero.attack(), self.fight_hero.name))

        if not self.fight_orc.is_alive():
            print("The winner is {}".format(self.fight_hero.name))
        elif not self.fight_hero.is_alive():
            print("The winner is {}".format(self.fight_orc.name))
