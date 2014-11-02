import weapon
import unittest

class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.char_weapon = weapon.Weapon("Bow", 500, 0.2)

    def test_init_constructor(self):
        self.assertEqual(self.char_weapon.type, "Bow")
        self.assertEqual(self.char_weapon.damage, 500)
        self.assertEqual(self.char_weapon.critical_strike_percent, 0.2)

    def test_critical_hit(self):
        results = []
        for i in range(100):
            results.append(self.char_weapon.critical_hit())
        self.assertTrue(True in results and False in results)

if __name__ == '__main__':
    unittest.main()