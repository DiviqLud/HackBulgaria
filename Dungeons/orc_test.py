import orc
import unittest
from weapon import Weapon

class TestOrc(unittest.TestCase):

    def setUp(self):
        self.bad_orc = orc.Orc("Mudagog", 100, 1.4)

    def test_orc_init(self):
        self.assertEqual(self.bad_orc.name, "Mudagog")
        self.assertEqual(self.bad_orc.health, 100)
        self.assertEqual(self.bad_orc.berserk_factor, 1.4)

    def test_orc_berserk_factor_out_of_bound_for_2(self):
        another_orc = orc.Orc("Garvin", 500, 4.5)
        self.assertEqual(another_orc.berserk_factor, 2)

    def test_orc_berserk_factor_out_of_bound_for_1(self):
        another_orc = orc.Orc("Garvin", 500, 0.4)
        self.assertEqual(another_orc.berserk_factor, 1)

    def test_atack(self):
        bow = Weapon("The slayer", 500, 0.9)
        self.bad_orc.equip_weapon(bow)
        self.assertEqual(self.bad_orc.atack(), 700)

if __name__ == '__main__':
       unittest.main()   