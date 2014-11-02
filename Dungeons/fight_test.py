import unittest
import hero
import orc
import weapon
import fight

class TestFight(unittest.TestCase):

    def setUp(self):
        bad_orc = orc.Orc("Emil", 150, 0.6)
        good_hero = hero.Hero("Naso", 160, "The Slayer")
        self.arena = fight.Fight(bad_orc, good_hero)

    def test_flip_coin (self):
        results = []
        for i in range(10):
            results.append(self.arena.flip_coin())
        self.assertTrue(self.arena.fight_orc in results and self.arena.fight_hero in results)

    def test_simulate_fight_with_weapons(self):
        axe = weapon.Weapon("The axe", 20, 0.6)
        dagger = weapon.Weapon("Daggerious", 21, 0.9)
        self.arena.fight_hero.weapon = axe
        self.arena.fight_orc.weapon = dagger
        self.arena.simulate_fight()
        self.assertTrue(self.arena.fight_hero.is_alive() or self.arena.fight_orc.is_alive())

    def test_simulate_fight_when_one_is_without_weapons(self):
        axe = weapon.Weapon("The axe", 20, 0.6)
        self.arena.fight_hero.weapon = axe
        self.arena.simulate_fight()
        self.assertTrue(not self.arena.fight_orc.is_alive())

    def test_simulate_fight_when_both_dont_have_weapons(self):
        self.arena.simulate_fight()
        self.assertTrue(self.arena.fight_hero.is_alive() and self.arena.fight_orc.is_alive())

if __name__ == '__main__':
    unittest.main()