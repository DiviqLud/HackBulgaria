import entity
import unittest
from weapon import Weapon

class TestEntity(unittest.TestCase):
    def setUp(self):
        self.character = entity.Entity("Bron", 100)

    def test_entity_init(self):
        self.assertEqual(self.character.name, "Bron")
        self.assertEqual(self.character.health, 100)

    def test_is_alive(self):
        self.assertTrue(self.character.is_alive())

    def test_is_dead(self):
        self.character.health = 0
        self.assertFalse(self.character.is_alive())

    def test_get_health(self):
        self.character.health = 55
        self.assertEqual(self.character.health, 55)

    def test_take_damage(self):
        self.assertEqual(self.character.take_damage(45.45), 54.55)

    def test_take_damage_more_than_health(self):
        self.assertEqual(self.character.take_damage(110), 0)

    def test_healing_when_its_too_late(self):
        self.character.health = 0
        self.assertFalse(self.character.take_healing(50))

    def test_healing_over_given_health(self):
        self.character.health = 50
        self.assertTrue(self.character.take_healing(60))

    def test_healing_for_success(self):
        self.character.health = 40
        self.assertTrue(self.character.take_healing(50))

    def test_has_weapon(self):
        self.assertFalse(self.character.has_weapon())

    def test_equip_weapon(self):
        bow = Weapon("The slayer", 500, 0.9)
        self.character.equip_weapon(bow)
        self.assertEqual(self.character.weapon, bow)

    def test_attack_with_weapon(self):
        bow = Weapon("The slayer", 500, 0.3)
        self.character.equip_weapon(bow)
        self.assertEqual(self.character.attack(), 500)

    def test_attack_without_weapon(self):
        self.assertEqual(self.character.attack(), 0)

    def test_attack_with_critical_strike(self):
        bow = Weapon("The slayer", 500, 1)
        self.character.equip_weapon(bow)
        self.assertEqual(self.character.attack(), 1000)

if __name__ == '__main__':
    unittest.main()