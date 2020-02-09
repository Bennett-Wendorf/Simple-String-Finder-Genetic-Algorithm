from chromosome import Chromosome
class Population:
    def __init__(self, chrom_list):
        self.individuals = []
        self.individuals.extend(chrom_list)

    @classmethod
    def Gen_Random(cls, pop_size, chrom_size, alphabet):
        new_list = []
        for i in range(pop_size):
            new_list.append(Chromosome.Gen_Random(chrom_size, alphabet))
        new_pop = cls(new_list)
        return new_pop
        
    def Get_Individuals(self):
        return self.individuals
