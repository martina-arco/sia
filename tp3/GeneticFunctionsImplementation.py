from GeneticFunctions import GeneticFunctions
from CrossoverAlgorithm import CrossoverAlgorithm
from Chromosome import Chromosome
import random


class GeneticFunctionsImplementation(GeneticFunctions):

    CHROMOSOME_SIZE = 6

    def __init__(self, parameters):
        # prob_crossover=0.9, prob_mutation=0.2):
        self.counter = 0

        self.crossover_algorithm = parameters.crossover_algorithm

        self.generation_max = 10

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

        for i in self.population_size:
            chromosome = Chromosome(len(self.weapons))
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
        while True:
            father = self.tournament(fits_populations)
            mother = self.tournament(fits_populations)
            yield (father, mother)

    def crossover(self, parents):
        # if self.crossover_algorithm == 'anular':
        #     return CrossoverAlgorithm.anular_crossover(parents)
        if self.crossover_algorithm == 'two_points':
            return CrossoverAlgorithm.two_point_crossover(parents)
        elif self.crossover_algorithm == 'uniform':
            return CrossoverAlgorithm.uniform_crossover(parents)

        return CrossoverAlgorithm.one_point_crossover(parents)

    def mutation(self, chromosome):
        index = random.randint(0, len(self.target) - 1)
        vary = random.randint(-5, 5)
        mutated = list(chromosome)
        mutated[index] += vary
        return mutated

    # internals
    # def tournament(self, fits_populations):
    #     alicef, alice = self.select_random(fits_populations)
    #     bobf, bob = self.select_random(fits_populations)
    #     return alice if alicef > bobf else bob
    #
    # def select_random(self, fits_populations):
    #     return fits_populations[random.randint(0, len(fits_populations) - 1)]



