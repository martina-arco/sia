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
        """list of tuples of parent's chrosomes
        """
        pass

    def crossover(self, father, mother):
        """breed children
        """
        pass

    def mutation(self, chromosome):
        """mutate chromosome
        """
        return chromosome

    def fitness_scaling(self, fits_population):
        """list of tuples of ftinesses and chrosomes
        """
        return fits_population
    pass
