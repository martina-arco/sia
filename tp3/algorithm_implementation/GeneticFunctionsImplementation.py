import random
import utils

import algorithm_implementation.StopConditions as StopConditions
import algorithm_implementation.SelectionAlgorithms as SelectionAlgorithms
import algorithm_implementation.CrossoverAlgorithms as CrossoverAlgorithms
import algorithm_implementation.MutationAlgorithms as MutationAlgorithms

from GeneticFunctions import GeneticFunctions
from Chromosome import Chromosome


def select_random_index():
    return random.randint(0, utils.CHROMOSOME_SIZE - 1)


def select_two_random_indexes():
    index1 = random.randint(0, utils.CHROMOSOME_SIZE - 2)
    index2 = random.randint(0, utils.CHROMOSOME_SIZE - 2)

    if index1 > index2:
        index1, index2 = index2, index1

    return index1, index2


class GeneticFunctionsImplementation(GeneticFunctions):

    def __init__(self, parameters):
        self.generations = 0

        self.population_size = parameters.population_size
        self.prob_crossover = parameters.prob_crossover
        self.prob_mutation = parameters.prob_mutation

        self.stop_condition = parameters.stop_condition
        self.selection_algorithm = parameters.selection_algorithm
        self.crossover_algorithm = parameters.crossover_algorithm
        self.mutation_algorithm = parameters.mutation_algorithm
        self.is_tournament_probabilistic = False

        self.generation_max = parameters.max_generation
        # ToDo: hay que agregar esto a los parametos y acordarse de verificar que sea par
        self.generation_k = 1

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
        # supongo que el counter es el numero de generacion
        self.population_temp = 100-self.counter
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
        return chromosome.calculate_fitness(self.attack_multiplier, self.defense_multiplier, self.force_multiplier,
                                            self.agility_multiplier,self.expertise_multiplier, self.resistance_multiplier,
                                            self.life_multiplier, self.weapons, self.boots, self.helmets, self.gloves,
                                            self.shirts)

    def check_stop(self, fits_populations):
        self.generations += 1

        if self.stop_condition == 'generation_number':
            return StopConditions.is_max_generation(self.generations, self.generation_max)
        elif self.stop_condition == 'structure':
            return StopConditions.structure()
        elif self.stop_condition == 'content':
            return StopConditions.content()

        return StopConditions.optimal()

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
        sorted_populations = sorted(fits_populations)
        if self.selection_algorithm == 'elite':
            return SelectionAlgorithms.elite(sorted_populations)

        elif self.selection_algorithm == 'roulette':
            return SelectionAlgorithms.roulette(sorted_populations)

        elif self.selection_algorithm == 'universal':
            return SelectionAlgorithms.universal(sorted_populations)

        elif self.selection_algorithm == 'boltzman':
            return SelectionAlgorithms.boltzman(fits_populations)

        elif self.selection_algorithm == 'tournament':
            return SelectionAlgorithms.tournament(fits_populations, self.is_tournament_probabilistic)

        elif self.selection_algorithm == 'ranking':
            return SelectionAlgorithms.ranking(fits_populations)

    def crossover(self, parents):
        father, mother = parents
        array_len = len(father.genes)

        if self.crossover_algorithm == 'anular':
            r, l = CrossoverAlgorithms.setup_anular_parameters(array_len)
            return CrossoverAlgorithms.anular_crossover(father, mother, r, l)

        elif self.crossover_algorithm == 'two_points':
            index1, index2 = select_two_random_indexes()
            return CrossoverAlgorithms.two_point_crossover(father, mother, index1, index2)

        elif self.crossover_algorithm == 'uniform':
            return CrossoverAlgorithms.uniform_crossover(father, mother)

        index = select_random_index()
        return CrossoverAlgorithms.one_point_crossover(father, mother, index)

    # falta que cambie si es no uniforme
    def probability_mutation(self):
        return self.prob_mutation

    def mutation(self, chromosome):
        items_size = len(self.weapons)

        if 'multi_gen' in self.mutation_algorithm:
            return MutationAlgorithms.multi_gen(chromosome.genes, items_size, self.prob_mutation)

        index = select_random_index()
        return MutationAlgorithms.gen(chromosome.genes, index, items_size)
