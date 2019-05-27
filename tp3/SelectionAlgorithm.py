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

    # No lo entendi
    @staticmethod
    def roulette(populations):
        pass

    # No lo entendi
    @staticmethod
    def universal(populations):
        pass

    # No lo entendi
    @staticmethod
    def boltzman(population):
        pass

    @staticmethod
    def tournament(populations):
        # Esto del while true no lo entiendo, deberia estar usando un corte
        while True:
            father = SelectionAlgorithm.tournament_deployment(populations)
            mother = SelectionAlgorithm.tournament_deployment(populations)
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
            if random.randint(1, high=None) > 0.5:
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
        
        pop_size = inverted_population.size()
        prob_size = (pop_size+1)*(pop_size/2)
        selection_number = random.randint(0, high=prob_size)

        for x in range(1, pop_size):
            accumulation += x
            if x >= selection_number:
                return inverted_population.get(x)

        return inverted_population.get(x)
