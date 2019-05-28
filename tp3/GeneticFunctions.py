class GeneticFunctions(object):
    # def probability_crossover(self):
    #     r"""returns rate of occur crossover(0.0-1.0)"""
    #     return 1.0

    # def probability_mutation(self):
    #     r"""returns rate of occur mutation(0.0-1.0)"""
    #     return 0.0

    def initial(self):
        """returns list of initial population
        """
        return []

    def fitness(self, chromosome):
        """returns domain fitness value of chromosome
        """
        return len(chromosome)

    def check_stop(self, fits_populations):
        """stop run if returns True
        - fits_populations: list of (fitness_value, chromosome)
        """
        return False

    def selection(self, fits_populations):
        """generator of selected parents
        """
        gen = iter(sorted(fits_populations))
        while True:
            f1, ch1 = next(gen)
            f2, ch2 = next(gen)
            yield (ch1, ch2)
            pass
        return

    def crossover(self, parents):
        """breed children
        """
        return parents

    def mutation(self, chromosome):
        """mutate chromosome
        """
        return chromosome
    pass