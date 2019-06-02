import random
import utils


class SelectionAlgorithm(object):
    def selection(self, arg1, arg2):
        pass


# se ordenan por aptitud y devuelve el top
class EliteSelection(SelectionAlgorithm):
    def selection(self, fits_population, k):
        sorted_population = sorted(fits_population, key=utils.sort_by_fitness, reverse=True)
        # chromosomes = [ch for f, ch in sorted_population]
        return sorted_population[0:k]


class RouletteSelection(SelectionAlgorithm):
    def selection(self, fits_population, k):
        fitness_accumulation = accumulative_fitness(fits_population)
        chromosomes = []

        for i in range(0, k):
            chromosome = select_by_probability(fitness_accumulation, fits_population, random.uniform(0, 1))
            chromosomes.append(chromosome)

        return chromosomes


class UniversalSelection(SelectionAlgorithm):
    def selection(self, fits_population, k):
        fitness_accumulation = accumulative_fitness(fits_population)
        chromosomes = []

        for i in range(1, k+1):
            r = (random.uniform(0, 1) + i - 1) / k
            chromosome = select_by_probability(fitness_accumulation, fits_population, r)
            chromosomes.append(chromosome)

        return chromosomes


class TournamentSelection(SelectionAlgorithm):
    def __init__(self, is_tournament_probabilistic):
        self.is_tournament_probabilistic = is_tournament_probabilistic

    def selection(self, populations, k):
        chromosomes = []

        for i in range(0, k):
            chromosome = tournament_deployment(populations, self.is_tournament_probabilistic)
            chromosomes.append(chromosome)

        return chromosomes


class RankingSelection(SelectionAlgorithm):
    def selection(self, fits_population, k):
        sorted_population = sorted(fits_population, key=utils.sort_by_fitness, reverse=True)
        i = 0
        chromosomes = []

        while i < len(sorted_population) - 1:
            chromosome = select_by_inverted_probability(sorted_population)
            chromosomes.append(chromosome)

        return chromosomes


def accumulative_fitness(population):
    accumulated_fitness = []
    fitness_sum = 0
    population_size = len(population)

    for i in range(0, population_size):
        fitness_sum += population[i][0]

    accumulated_fitness.append(population[0][0] / fitness_sum)

    for i in range(1, population_size):
        relative = population[i][0] / fitness_sum
        accumulated_fitness.append(accumulated_fitness[i-1] + relative)

    return accumulated_fitness


def select_by_probability(accumulated_fitness, population, r):
    for x in range(0, len(population)):
        if accumulated_fitness[x] >= r:
            return population[x]
    # si no agarre ninguno es porque es el ultimo
    return population[len(population)-1]


def tournament_deployment(fits_populations, is_tournament_probabilistic):
    mini_tournament = set()
    mini_tournament.add(select_random(fits_populations))
    mini_tournament.add(select_random(fits_populations))
    mini_tournament.add(select_random(fits_populations))

    if is_tournament_probabilistic:
        if random.random(0, 1) > 0.5:
            return max(mini_tournament)
        else:
            return min(mini_tournament)
    else:
        return max(mini_tournament)


def select_random(fits_populations):
    return fits_populations[random.randint(0, len(fits_populations) - 1)]


def select_by_inverted_probability(inverted_population):
    accumulation = 0
    x = 0

    pop_size = len(inverted_population)
    prob_size = (pop_size+1) * (pop_size/2)
    selection_number = random.randint(1, prob_size)

    for x in range(1, pop_size):
        accumulation += x
        if x >= selection_number:
            return inverted_population[x]

    # Por ahi tiene que retornar un error, no estoy seguro
    return inverted_population[x]
