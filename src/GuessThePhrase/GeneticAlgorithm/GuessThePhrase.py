import DNA
import math
import random


population = []
matingPool = []
target = "to be or not to be"
parentA: DNA.DNA
parentB: DNA.DNA

for i in range(100):
    population.append(DNA.DNA(target.len()))

def draw():
    for phrase in population:
        phrase.calculate_fitness(target)

def make_mating_pool():
    for phrase in population:
        n = math.floor(phrase.fitness * 100)
        for x in range(n):
            matingPool.append(phrase)

def choose_parents():
    global parentA, parentB
    parentA = random.choice(matingPool)
    parentB = random.choice(matingPool)
    while parentA == parentB:
        parentB = random.choice(matingPool)