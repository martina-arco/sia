import random
import utils

from Chromosome import Chromosome


class Crossover(object):

    def crossover(self, father, mother):
        pass


class OnePointCrossover(Crossover):

    def crossover(self, father, mother):
        index = utils.select_random_index()
        child1 = Chromosome(genes=father.genes[:index] + mother.genes[index:])
        child2 = Chromosome(genes=mother.genes[:index] + father.genes[index:])
        return child1, child2


class TwoPointCrossover(Crossover):

    def crossover(self, father, mother):
        index1, index2 = utils.select_two_random_indexes()
        child1 = Chromosome(genes=father.genes[:index1] + mother.genes[index1:index2+1] + father.genes[index2+1:])
        child2 = Chromosome(genes=mother.genes[:index1] + father.genes[index1:index2+1] + mother.genes[index2+1:])
        return child1, child2


class UniformCrossover(Crossover):
    def crossover(self, father, mother):
        child1_genes = []
        child2_genes = []

        for i in range(0, len(father.genes)):
            if random.uniform(0, 1) < 0.5:
                child1_genes.append(father.genes[i])
                child2_genes.append(mother.genes[i])
            else:
                child1_genes.append(mother.genes[i])
                child2_genes.append(father.genes[i])

        child1 = Chromosome(genes=child1_genes)
        child2 = Chromosome(genes=child2_genes)
        return child1, child2


class AnularCrossover(Crossover):
    def crossover(self, father, mother):
        r, l = self.setup_anular_parameters(len(father.genes))
        child1_genes = []
        child2_genes = []

        for i in range(0, len(father.genes)):
            if r <= i < r+l:
                child1_genes.append(mother.genes[i])
                child2_genes.append(father.genes[i])
            elif r+l > len(father.genes) and i < (r+l) % len(father.genes):
                child1_genes.append(mother.genes[i])
                child2_genes.append(father.genes[i])
            else:
                child1_genes.append(father.genes[i])
                child2_genes.append(mother.genes[i])

        child1 = Chromosome(genes=child1_genes)
        child2 = Chromosome(genes=child2_genes)

        return child1, child2

    def setup_anular_parameters(self, array_len):
        l = random.randint(0, array_len / 2)
        r = random.randint(0, array_len - 1)
        return r, l
