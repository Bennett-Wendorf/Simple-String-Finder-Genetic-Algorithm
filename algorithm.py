from answer import Answer
from population import Population
from chromosome import Chromosome
import random
import sys

def Score(chrom, answer):
    key = answer.Get_Value()
    score = 0
    chrom_val = chrom.Get_Value()
    for i in range(len(chrom_val)):
        if(chrom_val[i] == key[i]):
            score += 1
    score /= len(key)
    return score

def Get_Mean_Score(population, answer):
    individuals = population.Get_Individuals()
    total = 0
    for element in individuals:
        total += Score(element, answer)
    return total/len(individuals)

def Sort_Second(val):
    return val[1]

def Selection(population, answer, graded_retain_percent, nongraded_retain_percent):
    list_to_return = []
    chroms = []
    picked_chroms = []
    for chrom in population.Get_Individuals():
        chroms.append([chrom, Score(chrom, answer)])

    chroms.sort(key = Sort_Second, reverse = True)
    fit_num_to_retain = len(population.Get_Individuals())*graded_retain_percent
    fit_num_to_retain = round(fit_num_to_retain)
    random_retain = len(population.Get_Individuals())*nongraded_retain_percent
    random_retain = round(random_retain)
    
    for i in range(fit_num_to_retain):
        picked_chroms.append(chroms.pop(0))

    for i in range(random_retain):
        index = random.randrange(len(chroms))
        picked_chroms.append(chroms.pop(index))

    for element in picked_chroms:
        list_to_return.append(element[0])

    new_population = Population(list_to_return)
    
    return new_population

def Crossover(parent_1, parent_2):
    half_parent_1 = parent_1.Get_Value()[:int(len(parent_1.Get_Value())/2)]
    half_parent_2 = parent_2.Get_Value()[int(len(parent_2.Get_Value())/2):]

    child_string = half_parent_1 + half_parent_2

    child = Chromosome(child_string)

    return child

def Mutation(chrom, alphabet, mutation_amount):
    for i in range(mutation_amount):
        char_to_replace = random.choice(chrom.Get_Value())
        new_char = random.choice(alphabet)

        chrom = Chromosome(chrom.Get_Value().replace(char_to_replace, new_char, 1))

    return chrom

def Generation(population, answer, mutation_rate, graded_retain_percent, nongraded_retain_percent, mutation_amount):
    select = Selection(population, answer, graded_retain_percent, nongraded_retain_percent)

    children = []
    pop_individuals = population.Get_Individuals()
    
    while len(children) < len(pop_individuals)-len(select.Get_Individuals()):
        parent_1 = random.choice(pop_individuals)
        parent_2 = random.choice(pop_individuals)

        child = Crossover(parent_1, parent_2)

        if((random.randrange(100) + 1) <= mutation_rate):
            child = Mutation(child, answer.alphabet, mutation_amount)
            #print("Mutated")
                             
        children.append(child)

    return_list = select.Get_Individuals() + children

    return_pop = Population(return_list)

    return return_pop

def Algorithm(pop_size, chrom_size, mutation_rate=75, graded_retain_percent = .3, nongraded_retain_percent = .2, mutation_amount = 1):
    file = open("Output Data/StringGenAlg.txt", "a")
    answer = Answer(chrom_size)
    population = Population.Gen_Random(pop_size, chrom_size, answer.alphabet)
    answers = []
    count = 0

    while not answers:
               
        population = Generation(population, answer, mutation_rate, graded_retain_percent, nongraded_retain_percent, mutation_amount)

        print("Mean score = ", Get_Mean_Score(population, answer), file=sys.stderr)
        print("Count = ", count)

        for chrom in population.Get_Individuals():
            if answer.Is_Answer(chrom.Get_Value()):
                answers.append(chrom)
                
        count += 1

    print(answers[0].Get_Value())
    file.write(str(count) + "   Parameters were: pop_size = " + str(pop_size) + ", chrom_size = " + str(chrom_size) + ", mutation_rate = " + str(mutation_rate) + ", graded_retain_percent = " + str(graded_retain_percent) + ", nongraded_retain_percent = " + str(nongraded_retain_percent) + ", mutation_amount = " + str(mutation_amount) + "\n")
    file.close()
    print("The algorithm took ", count, " generations to find the answer.")
    print("Parameters were: pop_size = ", pop_size, ", chrom_size = ", chrom_size, ", mutation_rate = ", mutation_rate, ", graded_retain_percent = ", graded_retain_percent, ", nongraded_retain_percent = ", nongraded_retain_percent, ", mutation_amount = ", mutation_amount)

def Run_Multiple(times, pop_size, chrom_size, mutation_rate=100, graded_retain_percent = .3, nongraded_retain_percent = .2, mutation_amount = 1):
    for i in range(times):
        Algorithm(pop_size, chrom_size, mutation_rate, graded_retain_percent, nongraded_retain_percent, mutation_amount)

if __name__ == "__main__":
    print(str(sys.argv))
    Algorithm(int(sys.argv[1]), int(sys.argv[2]))
