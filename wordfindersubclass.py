from wordfinder import WordFinder
from random import choice

class SpecialWordFinder(WordFinder):

    def __init__(self, file):
        super().__init__(file)

    def word_choice(self):
        lines = open(self.file).read().splitlines()
        while len(self.word_list) < 3:
            line = choice(lines)
            if len(line) != 1 and line[0:1] != '#':
                self.word_list.append(line)
