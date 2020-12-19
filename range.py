import random

class Range:
    def __init__(self, minium, maxium, denominator):
        self.minium = minium
        self.maxium = maxium
        self.denominator = denominator

    def randomValue(self):
        return random.randint(self.minium, self.maxium)