import random
import string
class Answer:
    alphabet = string.ascii_letters + "!"
    def __init__(self, length):
        self.value = ""
        for i in range(length):
            self.value += random.choice(self.alphabet)
    def Is_Answer(self, comparison):
        return comparison == self.value
    def Get_Value(self):
        return self.value
    
