from chromosome import Chromosome
class Population:
    def __init__(self, chromList):
        self.individuals = []
        self.individuals.extend(chromList)

    @classmethod
    def genRandom(cls, popSize, chromSize, alphabet):
        newList = []
        for i in range(popSize):
            newList.append(Chromosome.genRandom(chromSize, alphabet))
        newPop = cls(newList)
        return newPop
        
    def GetIndividuals(self):
        return self.individuals
