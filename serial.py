"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        '''This creates and inital value and saves the inital value to use for resetting'''
        
        self.start = start - 1
        self.reset_value = start
    
    def generate(self):
        '''Returns a updated serial incrimenting by 1'''

        self.start += 1
        return self.start
    
    def reset(self):
        '''Resets the initial value to the start + 1'''

        self.start = self.reset_value - 1
