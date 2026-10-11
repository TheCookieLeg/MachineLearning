import random
import math

def random_character():
    n = random.randint(32, 122)
    return chr(n)

class DNA:
    def __init__(self, length):
        self.genes = []
        self.fitness = 0
        for i in range(length):
            self.genes.append(random_character())

    def get_phrase(self):
        return "".join(self.genes)

    def calculate_fitness(self, target):
        score = 0
        for i in range(len(self.genes)):
            if self.genes[i] == target[i]:
                score += 1
        self.fitness = score / len(self.genes)

    def crossover(self, partner):
        child = DNA(len(self.genes))
        midpoint = math.floor(random.randint(0, len(self.genes) - 1))
        for i in range(len(self.genes)):
            if i < midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child

    def mutate(self):
        mutationRate = 0.01
        for i in range(len(self.genes)):
            if random.random() < mutationRate:
                self.genes[i] = random_character()
