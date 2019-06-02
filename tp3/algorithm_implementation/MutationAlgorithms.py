import random
import utils

from Chromosome import Chromosome


def mutate_gene(index, items_size):
    if index == utils.HEIGHT:
        random_gene = random.uniform(1.3, 2.0)
    else:
        random_gene = random.randint(0, items_size-1)

    return random_gene


class Mutation(object):
    def __init__(self, initial_probability, rate, items_size):
        self.rate = rate
        self.mutation_probability = initial_probability
        self.items_size = items_size

    def update_parameters(self):
        pass

    def mutate(self, chromosome):
        pass


class GenMutation(Mutation):
    def __init__(self, initial_probability, rate, items_size):
        super().__init__(initial_probability, rate, items_size)

    def mutate(self, chromosome):
        mutate = random.uniform(0, 1) <= self.mutation_probability
        if mutate:
            index = utils.select_random_index()
            new_genes = chromosome.genes.copy()
            new_genes[index] = mutate_gene(index, self.items_size)
            return Chromosome(genes=new_genes)

        return chromosome


class MultiGenMutation(Mutation):
    def __init__(self, initial_probability, rate, items_size):
        super().__init__(initial_probability, rate, items_size)

    def mutate(self, chromosome):
        new_genes = chromosome.genes.copy()
        for index in range(0, utils.CHROMOSOME_SIZE):
            mutate = random.uniform(0, 1) < self.mutation_probability
            if mutate:
                new_genes[index] = mutate_gene(index, self.items_size)

        return Chromosome(genes=new_genes)


