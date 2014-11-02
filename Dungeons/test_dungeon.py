import unittest
import orc
import hero
from dungeon import Dungeon


class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.my_map = Dungeon("basic_dungeon.txt")

    #def test_map_dungeon(self):
     #   self.my_map.print_map()

    def test_spawn_hero(self):
        good_hero = hero.Hero("Sebastian", 100, "The great")
        self.assertTrue(self.my_map.spawn("The Great", good_hero))
    #    self.my_map.print_map()
        bad_orc = orc.Orc("Mudagog", 100, 1.4)
        self.assertTrue(self.my_map.spawn("The Badass", bad_orc))
    #    self.my_map.print_map()

    def test_move_hero(self):
        good_hero = hero.Hero("Sebastian", 100, "The great")
        self.assertTrue(self.my_map.spawn("The Great", good_hero))
    #    self.my_map.print_map()
        bad_orc = orc.Orc("Mudagog", 100, 1.4)
        self.assertTrue(self.my_map.spawn("The Badass", bad_orc))
    #    self.my_map.print_map()
        self.assertFalse(self.my_map.move("The Great", "up")) 
        self.assertFalse(self.my_map.move("The Great", "left")) 
        self.assertTrue(self.my_map.move("The Badass", "up")) 
        self.assertFalse(self.my_map.move("The Badass", "right")) 


        self.my_map.print_map()

if __name__ == '__main__':
    unittest.main()
