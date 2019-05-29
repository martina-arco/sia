import random
import utils

from Chromosome import Chromosome


def gen(genes, index, items_size):
    genes[index] = mutate_gene(index, items_size)
    return Chromosome(genes=genes)


def multi_gen(genes, items_size, prob_mutation):
    for index in range(0, len(genes)):
        mutate = random.random() < prob_mutation
        if mutate:
            genes[index] = mutate_gene(index, items_size)

    return Chromosome(genes=genes)


def mutate_gene(index, items_size):
    if index == utils.HEIGHT:
        random_gene = random.uniform(1.3, 2.0)
    else:
        random_gene = random.randint(0, items_size)

    return random_gene
