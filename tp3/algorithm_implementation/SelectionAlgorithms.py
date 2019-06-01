import random
import utils


class SelectionAlgorithm(object):
    def selection(self, arg1, arg2):
        pass


# se ordenan por aptitud y devuelve el top
class EliteSelection(SelectionAlgorithm):
    def selection(self, fits_population, k):
        sorted_population = sorted(fits_population, key=utils.sort_by_fitness, reverse=True)
        chromosomes = [ch for f, ch in sorted_population]
        return chromosomes[0:k]


class RouletteSelection(SelectionAlgorithm):
    def selection(self, fits_population, k):
        sorted_population = sorted(fits_population, key=utils.sort_by_fitness, reverse=True)
        parents = []

        for i in range(0, k):
            parent = select_by_probability(sorted_population)
            parents.append(parent)

        return parents


class UniversalSelection(SelectionAlgorithm):
    def selection(self, fits_population, k):
        sorted_population = sorted(fits_population, key=utils.sort_by_fitness, reverse=True)
        universal_array = universal_array_builder(sorted_population, k)
        i = 0
        parents = []

        while i < len(sorted_population) - 1:
            father = universal_array[i][1]
            mother = universal_array[i+1][1]
            parents.append((mother, father))

        return parents


class BoltzmanSelection(SelectionAlgorithm):
    # Hago el calculo de boltzman y lo uso como limite para trigger de fitness
    def selection(self, arg1, arg2):
        pass


class TournamentSelection(SelectionAlgorithm):
    def __init__(self, is_tournament_probabilistic):
        self.is_tournament_probabilistic = is_tournament_probabilistic

    def selection(self, populations, k):
        i = 0
        parents = []

        while i < len(populations) - 1:
            father = tournament_deployment(populations, self.is_tournament_probabilistic)
            mother = tournament_deployment(populations, self.is_tournament_probabilistic)
            parents.append((father, mother))

        return parents


class RankingSelection(SelectionAlgorithm):
    def selection(self, fits_population, k):
        sorted_population = sorted(fits_population, key=utils.sort_by_fitness, reverse=True)
        i = 0
        parents = []

        while i < len(sorted_population) - 1:
            father = select_by_inverted_probability(sorted_population)
            mother = select_by_inverted_probability(sorted_population)
            parents.append((father, mother))

        return parents


# internals
def universal_array_builder(sorted_population, k):
    result = []
    value_rand_r = random.randint(0, high=1)
    r = []
    for i in range(0, k - 1):
        r[i] = (value_rand_r + i - 1) / k

    accumulation = 0
    prob_size = 0
    pop_size = len(sorted_population)

    for i in range(1, pop_size):
        prob_size += sorted_population[i].fitness

    i = 0
    for x in range(1, pop_size):
        accumulation += sorted_population[x].fitness
        if accumulation >= r[i]:
            result.append(sorted_population[x])
            for t in range(i + 1, k):
                if accumulation >= r[t]:
                    result.append(sorted_population[x])
                else:
                    i = t
                    break

    # lleno los espacios restantes con el ultimo que supero
    if len(result) != k:
        for r in range(i, k):
            result[r] = result[i - 1]
        return result


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
    selection_number = random.randint(1, high=prob_size)

    for x in range(1, pop_size):
        accumulation += x
        if x >= selection_number:
            return inverted_population[x]

    # Por ahi tiene que retornar un error, no estoy seguro
    return inverted_population[x]


def select_by_probability(sorted_population):
    accumulation = 0
    fitness_sum = 0
    pop_size = len(sorted_population)

    for i in range(0, pop_size):
        fitness_sum += sorted_population[i][0]

    selection_number = random.uniform(0, fitness_sum)

    for x in range(0, pop_size):
        accumulation += sorted_population[x][0]
        if accumulation >= selection_number:
            chromosome_result = sorted_population[x][1]
            del sorted_population[x]
            return chromosome_result
