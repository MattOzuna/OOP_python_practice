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
        for num in range(3):
            line = choice(lines)
            self.word_list.append(line)

    def random(self):
        if len(self.word_list) == 0:
            self.word_choice()
        
        return choice(self.word_list)

        

            
            
                

