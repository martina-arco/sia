import random
import string

WEAPON = 0
BOOT = 1
HELMET = 2
GLOVE = 3
SHIRT = 4
HEIGHT = 5

CHROMOSOME_SIZE = 6

FITNESS = 0
CHROMOSOME = 1


def sort_by_fitness(fit):
    return fit[0]


def select_random_index():
    return random.randint(0, CHROMOSOME_SIZE - 1)


def select_two_random_indexes():
    index1 = random.randint(0, CHROMOSOME_SIZE - 2)
    index2 = random.randint(0, CHROMOSOME_SIZE - 2)

    if index1 > index2:
        index1, index2 = index2, index1

    return index1, index2


def generate_seed_for_population(population_size):
    seed = ""
    for i in range(population_size):
        seed += random.choice(string.ascii_letters)
    return seed

