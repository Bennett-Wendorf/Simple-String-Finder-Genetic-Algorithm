from answer import Answer
from population import Population
from chromosome import Chromosome
import random
import sys

def Score(chrom, answer):
    key = answer.GetValue()
    score = 0
    chromVal = chrom.GetValue()
    for i in range(len(chromVal)):
        if(chromVal[i] == key[i]):
            score += 1
    score /= len(key)
    return score

def GetMeanScore(population, answer):
    individuals = population.GetIndividuals()
    total = 0
    for element in individuals:
        total += Score(element, answer)
    return total/len(individuals)

def SortSecond(val):
    return val[1]

def Selection(population, answer, GRADED_RETAIN_PERCENT, NONGRADED_RETAIN_PERCENT):
    listToReturn = []
    chroms = []
    pickedChroms = []
    for chrom in population.GetIndividuals():
        chroms.append([chrom, Score(chrom, answer)])

    chroms.sort(key = SortSecond, reverse = True)
    fitNumToRetain = len(population.GetIndividuals())*GRADED_RETAIN_PERCENT
    fitNumToRetain = round(fitNumToRetain)
    randomRetain = len(population.GetIndividuals())*NONGRADED_RETAIN_PERCENT
    randomRetain = round(randomRetain)
    
    for i in range(fitNumToRetain):
        pickedChroms.append(chroms.pop(0))

    for i in range(randomRetain):
        index = random.randrange(len(chroms))
        pickedChroms.append(chroms.pop(index))

    for element in pickedChroms:
        listToReturn.append(element[0])

    newPopulation = Population(listToReturn)
    
    return newPopulation

def Crossover(parent1, parent2):
    halfParent1 = parent1.GetValue()[:int(len(parent1.GetValue())/2)]
    halfParent2 = parent2.GetValue()[int(len(parent2.GetValue())/2):]

    childString = halfParent1 + halfParent2

    child = Chromosome(childString)

    return child

def Mutation(chrom, alphabet, mutationAmount):
    for i in range(mutationAmount):
        charToReplace = random.choice(chrom.GetValue())
        newChar = random.choice(alphabet)

        chrom = Chromosome(chrom.GetValue().replace(charToReplace, newChar, 1))

    return chrom

def Generation(population, answer, mutationRate, GRADED_RETAIN_PERCENT, NONGRADED_RETAIN_PERCENT, mutationAmount):
    select = Selection(population, answer, GRADED_RETAIN_PERCENT, NONGRADED_RETAIN_PERCENT)

    children = []
    popIndividuals = population.GetIndividuals()
    
    while len(children) < len(popIndividuals)-len(select.GetIndividuals()):
        parent1 = random.choice(popIndividuals)
        parent2 = random.choice(popIndividuals)

        child = Crossover(parent1, parent2)

        if((random.randrange(100) + 1) <= mutationRate):
            child = Mutation(child, answer.alphabet, mutationAmount)
            #print("Mutated")
                             
        children.append(child)

    returnList = select.GetIndividuals() + children

    returnPop = Population(returnList)

    return returnPop

def Algorithm(pop_size, chrom_size, MUTATION_RATE=100, GRADED_RETAIN_PERCENT = .3, NONGRADED_RETAIN_PERCENT = .2, MUTATION_AMOUNT = 1):
    file = open("Output Data/StringGenAlg.txt", "a")
    answer = Answer(chrom_size)
    population = Population.genRandom(pop_size, chrom_size, answer.alphabet)
    answers = []
    count = 0

    while not answers:
               
        population = Generation(population, answer, MUTATION_RATE, GRADED_RETAIN_PERCENT, NONGRADED_RETAIN_PERCENT, MUTATION_AMOUNT)

        print("Mean score = ", GetMeanScore(population, answer), file=sys.stderr)
        print("Count = ", count)

        for chrom in population.GetIndividuals():
            if answer.IsAnswer(chrom.GetValue()):
                answers.append(chrom)
                
        count += 1

    print(answers[0].GetValue())
    file.write(str(count) + "   Parameters were: pop_size = " + str(pop_size) + ", chrom_size = " + str(chrom_size) + ", MUTATION_RATE = " + str(MUTATION_RATE) + ", GRADED_RETAIN_PERCENT = " + str(GRADED_RETAIN_PERCENT) + ", NONGRADED_RETAIN_PERCENT = " + str(NONGRADED_RETAIN_PERCENT) + ", MUTATION_AMOUNT = " + str(MUTATION_AMOUNT) + "\n")
    file.close()
    print("The algorithm took ", count, " generations to find the answer.")
    print("Parameters were: pop_size = ", pop_size, ", chrom_size = ", chrom_size, ", MUTATION_RATE = ", MUTATION_RATE, ", GRADED_RETAIN_PERCENT = ", GRADED_RETAIN_PERCENT, ", NONGRADED_RETAIN_PERCENT = ", NONGRADED_RETAIN_PERCENT, ", MUTATION_AMOUNT = ", MUTATION_AMOUNT)

def Run_Multiple(times, pop_size, chrom_size, MUTATION_RATE=100, GRADED_RETAIN_PERCENT = .3, NONGRADED_RETAIN_PERCENT = .2, MUTATION_AMOUNT = 1):
    for i in range(times):
        Algorithm(pop_size, chrom_size, MUTATION_RATE, GRADED_RETAIN_PERCENT, NONGRADED_RETAIN_PERCENT, MUTATION_AMOUNT)
