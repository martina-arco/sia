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
    def universal(self, populations):
        return 0

    # Hago el calculo de boltzman y lo uso como limite para trigger de fitness
    @staticmethod
    def boltzman(self, population):
        return 0

    @staticmethod
    def tournament(self, populations):
        # Esto del while true no lo entiendo, deberia estar usando un corte
        while True:
            father = self.tournament_deployment(populations)
            mother = self.tournament_deployment(populations)
            yield (father, mother)

    @staticmethod
    def ranking(self, populations):
        sorted_population = sorted(populations, reverse=True)
        while True:
            father = self.select_by_inverted_ranking_probability(sorted_population)
            mother = self.select_by_inverted_ranking_probability(sorted_population)
            yield (father, mother)

    @staticmethod
    def tournament_deployment(self, fits_populations):
        mini_tournament = set()
        mini_tournament.add(self.select_random(fits_populations))
        mini_tournament.add(self.select_random(fits_populations))
        mini_tournament.add(self.select_random(fits_populations))

        # No se como tomar este parametro desde genetics
        # if True:
        if self.tournament_probabilistic:
            if random.randint(1, high=None) > 0.5:
                return max(mini_tournament)
            else:
                return min(mini_tournament)
        else:
            return max(mini_tournament)

    @staticmethod
    def select_random(self, fits_populations):
        return fits_populations[random.randint(0, len(fits_populations) - 1)]

    @staticmethod
    def select_by_inverted_ranking_probability(self, inverted_population):
        accumulation = 0
        pop_size = inverted_population.size()
        prob_size = (pop_size+1)*(pop_size/2)
        selection_number = random.randint(1, high=prob_size)
        for x in range(1, pop_size):
            accumulation += x
            if accumulation >= selection_number:
                return inverted_population.get(x)

        # Deberia retornar un error
        return 0

    @staticmethod
    def select_by_probability(self, sorted_population):
        accumulation = 0
        prob_size = 0
        pop_size = sorted_population.size()
        for i in range(1, pop_size):
            prob_size += sorted_population.get(i).fitness

        selection_number = random.randint(1, high=prob_size)

        for x in range(1, pop_size):
            accumulation += sorted_population.get(x).fitness
            if accumulation >= selection_number:
                return sorted_population.get(x)

        # Deberia retornar un error
        return 0
