from entity import Entity
from hero import Hero
from orc import Orc
import fileinput

class Dungeon():
    def __init__(self, file_path):
        self.file_path = file_path
        self.source = open(self.file_path, 'r')
        self.content = self.source.readlines()
        self.hero_player = None
        self.orc_player = None


    def print_map(self):
        for line in self.content:
            print(line)
        self.source.close()

    def spawn(self, player_name, entity):
        for line in range(len(self.content)):
            for char in self.content[line]:
                if char == "S":
                    if isinstance(entity, Hero):
                        self.hero_player = player_name
                        self.content[line] = self.content[line].replace(char, "H", 1)
                        self.source.close()
                        return True
                    if isinstance(entity, Orc):
                        self.orc_player = player_name
                        self.content[line] = self.content[line].replace(char, "O", 1)
                        self.source.close()
                        return True
        return False

    def move(self, player_name, direction):
        size_line = len(self.content)
        size_cols = len(self.content[0])
        for line in range(len(self.content)):
            self.content[line] = list(self.content[line])
        for line in range(len(self.content)):
            for char in range(len(self.content[line])):
                if self.hero_player == player_name and self.content[line][char] in "H" or self.orc_player == player_name and self.content[line][char] in "O":
                    if direction == "right":
                        if char + 1 >= size_cols:
                            return False
                        elif self.content[line][char+1] == ".":
                            self.content[line][char], self.content[line][char+1] = self.content[line][char+1], self.content[line][char] 
                            return True
                        elif self.content[line][char+1] == "W":
                            pass
                        else:
                            return False
                    if direction == "up":
                        if line - 1 < 0:
                            return False
                        elif self.content[line-1][char] == ".":
                            self.content[line][char], self.content[line-1][char] = self.content[line-1][char], self.content[line][char] 
                            return True
                        else:
                            return False
                    if direction == "down":
                        if line + 1 >= size_line:
                            return False
                        elif self.content[line+1][char] == ".":
                            self.content[line][char], self.content[line+1][char] = self.content[line+1][char], self.content[line][char]
                            return True
                        else:
                            return False
                    if direction == "left":
                        if char - 1 < 0:
                            return False
                        elif self.content[line][char-1] == ".":
                            self.content[line][char], self.content[line][char-1] = self.content[line][char-1], self.content[line][char]
                            return True
                        else:
                            return False
                return False

    def end_of