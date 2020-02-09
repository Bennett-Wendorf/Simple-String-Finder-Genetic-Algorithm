import random
class Chromosome:
    def __init__(self, chrom_string):
        self.value = chrom_string

    @classmethod
    def Gen_Random(cls, length, alphabet):
        value = ""
        for i in range(length):
            value += random.choice(alphabet)
        chrom = cls(value)
        return chrom

    def Get_Value(self):
        return self.value
