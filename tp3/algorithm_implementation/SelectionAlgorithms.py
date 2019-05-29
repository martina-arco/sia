import random


# se ordenan por aptitud y devuelve el top
def elite(populations):
    sorted_population = sorted(populations)
    while True:
        father = next(sorted_population)
        mother = next(sorted_population)
        yield (father, mother)


def roulette(self, populations):
    sorted_population = sorted(populations)
    while True:
        father = self.select_by_probability(sorted_population)
        mother = self.select_by_probability(sorted_population)
        yield (father, mother)


def universal(populations, k):
    result = set()
    sorted_population = sorted(populations)
    value_rand_r = random.randint(0, high=1)
    r = []
    for i in range(0, k - 1):
        r[i] = (r + i - 1) / k

    accumulation = 0
    prob_size = 0
    pop_size = len(sorted_population)
    for i in range(1, pop_size):
        prob_size += sorted_population[i].fitness

    i = 0
    for x in range(1, pop_size):
        accumulation += sorted_population[x].fitness
        if accumulation >= r[i]:
            result.add(sorted_population[x])
            for t in range(i + 1, k):
                if accumulation >= r[t]:
                    result.add(sorted_population[x])
                else:
                    i = t
                    break

    # lleno los espacios restantes con el ultimo que supero
    if len(result) != k:
        for r in range(i, k):
            result[r] = result[i - 1]


# Hago el calculo de boltzman y lo uso como limite para trigger de fitness
def boltzman(population):
    pass


def tournament(populations, is_tournament_probabilistic):
    # Esto del while true no lo entiendo, deberia estar usando un corte
    while True:
        father = tournament_deployment(populations, is_tournament_probabilistic)
        mother = tournament_deployment(populations, is_tournament_probabilistic)
        yield (father, mother)


def ranking(populations):
    sorted_population = sorted(populations, reverse=True)
    while True:
        father = select_by_inverted_probability(sorted_population)
        mother = select_by_inverted_probability(sorted_population)
        yield (father, mother)


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
    prob_size = 0
    pop_size = sorted_population.size()
    for i in range(1, pop_size):
        prob_size += sorted_population[i].fitness

    selection_number = random.randint(1, high=prob_size)

    for x in range(1, pop_size):
        accumulation += sorted_population[x].fitness
        if accumulation >= selection_number:
            return sorted_population[x]
