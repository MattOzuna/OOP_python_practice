"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    '''
    >>> wf = WordFinder("words.txt")
        3 words read

    >>> wf.random()
        'cat'

    >>> wf.random()
        'cat'

    >>> wf.random()
        'porcupine'

    >>> wf.random()
        'dog'
    '''
    
    def __init__(self, file):
        self.file = file
        self.word_list = []

    def word_choice(self):
        lines = open(self.file).read().splitlines()
        while len(self.word_list) < 3:
            line = choice(lines)
            if len(line) != 1:
                self.word_list.append(line)

    def random(self):
        if len(self.word_list) == 0:
            self.word_choice()
        
        return choice(self.word_list)

#solution used different methods

        

            
            
                

