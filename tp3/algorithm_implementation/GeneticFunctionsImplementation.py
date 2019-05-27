from GeneticFunctions import GeneticFunctions
from algorithm_implementation.SelectionAlgorithms import SelectionAlgorithm
from algorithm_implementation.CrossoverAlgorithms import CrossoverAlgorithm
from Chromosome import Chromosome


class GeneticFunctionsImplementation(GeneticFunctions):

    CHROMOSOME_SIZE = 6

    def __init__(self, parameters):
        # prob_crossover=0.9, prob_mutation=0.2):
        self.counter = 0

        self.selection_algorithm = parameters.selection_algorithm
        self.crossover_algorithm = parameters.crossover_algorithm
        self.mutation_algorithm = parameters.mutation_algorithm

        self.generation_max = parameters.max_generation

        self.attack_multiplier = parameters.attack_multiplier
        self.defense_multiplier = parameters.defense_multiplier

        self.force_multiplier = parameters.force_multiplier
        self.agility_multiplier = parameters.agility_multiplier
        self.expertise_multiplier = parameters.expertise_multiplier
        self.resistance_multiplier = parameters.resistance_multiplier
        self.life_multiplier = parameters.life_multiplier

        self.weapons = parameters.weapons
        self.boots = parameters.boots
        self.helmets = parameters.helmets
        self.gloves = parameters.gloves
        self.shirts = parameters.shirts

        # self.limit = parameters.limit
        self.population_size = parameters.population_size

        self.is_tournament_probabilistic = False
        # self.prob_crossover = prob_crossover
        # self.prob_mutation = prob_mutation

    # GeneticFunctions interface impls
    # def probability_crossover(self):
    #     return self.prob_crossover
    #
    # def probability_mutation(self):
    #     return self.prob_mutation

    def initial(self):

        population = []

        for i in range(0, self.population_size):
            chromosome = Chromosome(items_size=len(self.weapons))
            population.append(chromosome)

        return population

    def fitness(self, chromosome):
        return chromosome.calculate_fitness(self.attack_multiplier, self.defense_multiplier, self.force_multiplier, self.agility_multiplier,
                                            self.expertise_multiplier, self.resistance_multiplier, self.life_multiplier,
                                            self.weapons, self.boots, self.helmets, self.gloves, self.shirts)

    def check_stop(self, fits_populations):
        self.counter += 1
        return self.counter > self.generation_max
        # if self.counter % 10 == 0:
        #     best_match = list(sorted(fits_populations))[-1][1]
        #     fits = [f for f, ch in fits_populations]
        #     best = max(fits)
        #     worst = min(fits)
        #     ave = sum(fits) / len(fits)
        #     print(
        #         "[G %3d] score=(%4d, %4d, %4d): %r" %
        #         (self.counter, best, ave, worst,
        #          self.chromo2text(best_match)))
        #     pass
        # return self.counter >= self.limit

    def selection(self, fits_populations):
        if self.selection_algorithm == 'elite':
            SelectionAlgorithm.elite()
        elif self.selection_algorithm == 'ruleta':
            SelectionAlgorithm.roulette(fits_populations)
        elif self.selection_algorithm == 'universal':
            SelectionAlgorithm.universal(fits_populations)
        elif self.selection_algorithm == 'boltzman':
            SelectionAlgorithm.boltzman(fits_populations)
        elif self.selection_algorithm == 'torneos':
            SelectionAlgorithm.tournament(fits_populations, self.is_tournament_probabilistic)
        elif self.selection_algorithm == 'ranking':
            SelectionAlgorithm.ranking(fits_populations)

    def crossover(self, parents):
        father, mother = parents
        array_len = len(father.genes)

        if self.crossover_algorithm == 'anular':
            r, l = CrossoverAlgorithm.setup_anular_parameters(array_len)
            return CrossoverAlgorithm.anular_crossover(father, mother, r, l)
        if self.crossover_algorithm == 'two_points':
            index1, index2 = CrossoverAlgorithm.setup_indexes(array_len)
            return CrossoverAlgorithm.two_point_crossover(father, mother, index1, index2)
        elif self.crossover_algorithm == 'uniform':
            return CrossoverAlgorithm.uniform_crossover(father, mother)

        index = CrossoverAlgorithm.setup_index(array_len)
        return CrossoverAlgorithm.one_point_crossover(father, mother, index)

    def mutation(self, chromosome):
        pass
        # index = random.randint(0, len(self.target) - 1)
        # vary = random.randint(-5, 5)
        # mutated = list(chromosome)
        # mutated[index] += vary
        # return mutated

    # internals
    # def tournament(self, fits_populations):
    #     alicef, alice = self.select_random(fits_populations)
    #     bobf, bob = self.select_random(fits_populations)
    #     return alice if alicef > bobf else bob
    #
    # def select_random(self, fits_populations):
    #     return fits_populations[random.randint(0, len(fits_populations) - 1)]



