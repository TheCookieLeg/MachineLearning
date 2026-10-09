import random
import GuessThePhrase as Phrase

def random_character():
    n = random.randint(32, 122)
    return chr(n)

class DNA:
    def __init__(self, length):
        self.genes = []
        self.fitness = 0
        for i in range(length):
            self.genes.append(random_character())

    def calculate_fitness(self, target):
        score = 0
        for i in range(self.genes.len()):
            if self.genes[i] == target[i]:
                score += 1
        self.fitness = score / self.genes.len()
            
