import random

from Chromosome import Chromosome


class CrossoverAlgorithm(object):

    @staticmethod
    def one_point_crossover(parents):
        father, mother = parents

        index = random.randint(1, len(father.array) - 2)
        child1 = Chromosome(genes=father.array[:index] + mother.array[index:])
        child2 = Chromosome(genes=mother.array[:index] + father.array[index:])
        return child1, child2

    @staticmethod
    def two_point_crossover(parents):
        father, mother = parents

        index1 = random.randint(1, len(father.array) - 2)
        index2 = random.randint(1, len(father.array) - 2)

        if index1 > index2:
            index1, index2 = index2, index1

        child1 = Chromosome(genes=father.array[:index1] + mother.array[index1:index2] + father.array[index2:])
        child2 = Chromosome(genes=mother.array[:index1] + father.array[index1:index2] + mother.array[index2:])
        return child1, child2

    @staticmethod
    def uniform_crossover(parents):
        father, mother = parents

        child1_array = []
        child2_array = []

        for gene in father.array:
            if random.uniform(0, 1) < 0.5:
                child1_array[gene] = father.array[gene]
                child2_array[gene] = mother.array[gene]
            else:
                child1_array[gene] = mother.array[gene]
                child2_array[gene] = father.array[gene]

        child1 = Chromosome(genes=child1_array)
        child2 = Chromosome(genes=child2_array)
        return child1, child2

    @staticmethod
    def anular_crossover(parents, r, l):
        father, mother = parents

        child1_array = []
        child2_array = []

        for gene in father.array:
            if gene >= r-1 or gene < r+l-1 % len(father.array):
                child1_array[gene] = mother.array[gene]
                child2_array[gene] = father.array[gene]
            else:
                child1_array[gene] = father.array[gene]
                child2_array[gene] = mother.array[gene]

        child1 = Chromosome(genes=child1_array)
        child2 = Chromosome(genes=child2_array)

        return child1, child2
