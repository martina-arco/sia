import random


class SelectionAlgorithm(object):

    # se ordenan por aptitud y devuelve el top
    @staticmethod
    def elite(populations):
        sorted_population = sorted(populations)
        while True:
            father = next(sorted_population)
            mother = next(sorted_population)
            yield (father, mother)

    @staticmethod
    def roulette(self, populations):
        sorted_population = sorted(populations)
        while True:
            father = self.select_by_probability(sorted_population)
            mother = self.select_by_probability(sorted_population)
            yield (father, mother)

    # No lo entendi
    @staticmethod
    def universal(populations):
        pass

    # Hago el calculo de boltzman y lo uso como limite para trigger de fitness
    @staticmethod
    def boltzman(population):
        pass

    @staticmethod
    def tournament(populations, is_tournament_probabilistic):
        # Esto del while true no lo entiendo, deberia estar usando un corte
        while True:
            father = SelectionAlgorithm.tournament_deployment(populations, is_tournament_probabilistic)
            mother = SelectionAlgorithm.tournament_deployment(populations, is_tournament_probabilistic)
            yield (father, mother)

    @staticmethod
    def ranking(populations):
        sorted_population = sorted(populations, reverse=True)
        while True:
            father = SelectionAlgorithm.select_by_inverted_probability(sorted_population)
            mother = SelectionAlgorithm.select_by_inverted_probability(sorted_population)
            yield (father, mother)

    @staticmethod
    def tournament_deployment(fits_populations, is_tournament_probabilistic):
        mini_tournament = set()
        mini_tournament.add(SelectionAlgorithm.select_random(fits_populations))
        mini_tournament.add(SelectionAlgorithm.select_random(fits_populations))
        mini_tournament.add(SelectionAlgorithm.select_random(fits_populations))

        if is_tournament_probabilistic:
            if random.random(0, 1) > 0.5:
                return max(mini_tournament)
            else:
                return min(mini_tournament)
        else:
            return max(mini_tournament)

    @staticmethod
    def select_random(fits_populations):
        return fits_populations[random.randint(0, len(fits_populations) - 1)]

    @staticmethod
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

    @staticmethod
    def select_by_probability(self, sorted_population):
        accumulation = 0
        prob_size = 0
        pop_size = sorted_population.size()
        for i in range(1, pop_size):
            prob_size += sorted_population.get(i).fitness

        selection_number = random.randint(1, high=prob_size)

        for x in range(1, pop_size):
            accumulation += sorted_population[x].fitness
            if accumulation >= selection_number:
                return sorted_population[x]

        # Creo que tiene que retornar un error
        pass
