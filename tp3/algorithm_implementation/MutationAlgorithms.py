import random
import utils

from Chromosome import Chromosome


def mutate_gene(index, items_size):
    if index == utils.HEIGHT:
        random_gene = random.uniform(1.3, 2.0)
    else:
        random_gene = random.randint(0, items_size)

    return random_gene


class Mutation(object):

    def mutate(self, chromosome, items_size, prob_mutation):
        pass


class GenMutation(Mutation):
    def mutate(self, chromosome, items_size, prob_mutation):
        mutate = random.uniform(0, 1) < prob_mutation
        if mutate:
            index = utils.select_random_index()
            new_genes = chromosome.genes
            new_genes[index] = mutate_gene(index, items_size)
            return Chromosome(genes=new_genes)

        return chromosome


class MultiGenMutation(Mutation):
    def mutate(self, chromosome, items_size, prob_mutation):
        new_genes = chromosome.genes
        for index in range(0, utils.CHROMOSOME_SIZE):
            mutate = random.uniform(0, 1) < prob_mutation
            if mutate:
                new_genes[index] = mutate_gene(index, items_size)

        return Chromosome(genes=new_genes)


