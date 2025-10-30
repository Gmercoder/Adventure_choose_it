from random import randint

class Dice:
    def __init__(self, d4:int=0, d6:int = 0, d10:int = 0, d20:int = 0, mod=0):
        self.d4, self.d6, self.d10, self.d20, self.mod = d4, d6, d10, d20, mod

    def roll(self):
        #cumm_sum stands for cummulative sum
        cumm_sum = 0
        for _ in range(self.d4):
            cumm_sum += randint(1,4)
        for _ in range(self.d6):
            cumm_sum += randint(1, 6)
        for _ in range(self.d10):
            cumm_sum += randint(1,10)
        for _ in range(self.d20):
            cumm_sum += randint(1, 20)
        return cumm_sum + self.mod
