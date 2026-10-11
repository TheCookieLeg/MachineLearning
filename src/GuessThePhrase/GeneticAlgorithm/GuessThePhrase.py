import DNA
import math
import random

populationSize = 150
population = []
matingPool = []
target = "Machine learning is pretty damn cool, I must say"
parentA: DNA.DNA = None
parentB: DNA.DNA = None
phraseFound = False
generation = 0

# setup
for i in range(populationSize):
    population.append(DNA.DNA(len(target)))

# Functions
def calc_fitness_for_entire_population():
    for phrase in population:
        phrase.calculate_fitness(target)

def make_mating_pool():
    matingPool.clear()
    for phrase in population:
        n = math.floor(phrase.fitness * 100)
        for x in range(n):
            matingPool.append(phrase)

def choose_parents():
    global parentA, parentB
    parentA = random.choice(matingPool)
    parentB = random.choice(matingPool)
    while parentA is parentB:
        parentB = random.choice(matingPool)

def find_biggest_fitness():
    biggest = population[0]
    for phrase in population:
        if phrase.fitness > biggest.fitness:
            biggest = phrase
    return biggest

# Loop
while not phraseFound:
    generation += 1
    calc_fitness_for_entire_population()
    make_mating_pool()
    biggestFitness = find_biggest_fitness()

    print(generation, " ", biggestFitness.get_phrase())

    if biggestFitness.get_phrase() == target:
        phraseFound = True
        print("The phrase was found!")

    # Make children
    for i in range(populationSize):
        choose_parents()
        child = parentA.crossover(parentB)
        child.mutate() # May mutate
        population[i] = child


