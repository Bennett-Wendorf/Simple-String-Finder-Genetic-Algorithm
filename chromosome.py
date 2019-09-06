import random
class Chromosome:
    def __init__(self, chromString):
        self.value = chromString

    @classmethod
    def genRandom(cls, length, alphabet):
        value = ""
        for i in range(length):
            value += random.choice(alphabet)
        chrom = cls(value)
        return chrom

    def GetValue(self):
        return self.value
