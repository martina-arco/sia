import random
import utils
import math

from algorithm_implementation.StopConditions import MaxGenerationStopCondition
from algorithm_implementation.StopConditions import StructureStopCondition
from algorithm_implementation.StopConditions import ContentStopCondition
from algorithm_implementation.StopConditions import OptimalStopCondition

from algorithm_implementation.SelectionAlgorithms import EliteSelection
from algorithm_implementation.SelectionAlgorithms import RouletteSelection
from algorithm_implementation.SelectionAlgorithms import UniversalSelection
from algorithm_implementation.SelectionAlgorithms import BoltzmanSelection
from algorithm_implementation.SelectionAlgorithms import TournamentSelection
from algorithm_implementation.SelectionAlgorithms import RankingSelection

from algorithm_implementation.CrossoverAlgorithms import OnePointCrossover
from algorithm_implementation.CrossoverAlgorithms import TwoPointCrossover
from algorithm_implementation.CrossoverAlgorithms import UniformCrossover
from algorithm_implementation.CrossoverAlgorithms import AnularCrossover

from algorithm_implementation.MutationAlgorithms import GenMutation
from algorithm_implementation.MutationAlgorithms import MultiGenMutation


from GeneticFunctions import GeneticFunctions
from Chromosome import Chromosome


class GeneticFunctionsImplementation(GeneticFunctions):

    def __init__(self, parameters):
        self.generation = 0

        self.population_size = parameters.population_size
        self.prob_crossover = parameters.prob_crossover
        self.prob_mutation = parameters.prob_mutation

        self.stop_condition = parameters.stop_condition
        self.selection_algorithm = parameters.selection_algorithm
        self.crossover_algorithm = parameters.crossover_algorithm
        self.mutation_algorithm = parameters.mutation_algorithm
        self.is_tournament_probabilistic = False

        if self.stop_condition == 'generation_number':
            self.stop_condition_implementation = MaxGenerationStopCondition()
        elif self.stop_condition == 'structure':
            self.stop_condition_implementation = StructureStopCondition()
        elif self.stop_condition == 'content':
            self.stop_condition_implementation = ContentStopCondition()
        else:
            self.stop_condition_implementation = OptimalStopCondition()

        self.generation_max = parameters.max_generation
        self.fitness_min = parameters.fitness_min
        self.generation_percentage_to_say_equals = parameters.generation_percentage_to_say_equals
        self.best_fits = []
        self.previous_generation = []
        self.count_of_equal_generations = 0
        self.generation_number_to_say_equals = parameters.generation_number_to_say_equals
        self.is_tournament_probabilistic = False

        if self.selection_algorithm == 'elite':
            self.selection_algorithm_implementation_1 = EliteSelection()
        elif self.selection_algorithm == 'roulette':
            self.selection_algorithm_implementation_1 = RouletteSelection()
        elif self.selection_algorithm == 'universal':
            self.selection_algorithm_implementation_1 = UniversalSelection()
        elif self.selection_algorithm == 'boltzman':
            self.selection_algorithm_implementation_1 = BoltzmanSelection()
        elif self.selection_algorithm == 'tournament':
            self.selection_algorithm_implementation_1 = TournamentSelection(self.is_tournament_probabilistic)
        elif self.selection_algorithm == 'ranking':
            self.selection_algorithm_implementation_1 = RankingSelection()
        
        if self.selection_algorithm == 'elite':
            self.selection_algorithm_implementation_2 = EliteSelection()
        elif self.selection_algorithm == 'roulette':
            self.selection_algorithm_implementation_2 = RouletteSelection()
        elif self.selection_algorithm == 'universal':
            self.selection_algorithm_implementation_2 = UniversalSelection()
        elif self.selection_algorithm == 'boltzman':
            self.selection_algorithm_implementation_2 = BoltzmanSelection()
        elif self.selection_algorithm == 'tournament':
            self.selection_algorithm_implementation_2 = TournamentSelection(self.is_tournament_probabilistic)
        elif self.selection_algorithm == 'ranking':
            self.selection_algorithm_implementation_2 = RankingSelection()

        if self.crossover_algorithm == 'anular':
            self.crossover_algorithm_implementation = AnularCrossover()
        elif self.crossover_algorithm == 'two_points':
            self.crossover_algorithm_implementation = TwoPointCrossover()
        elif self.crossover_algorithm == 'uniform':
            self.crossover_algorithm_implementation = UniformCrossover()
        else:
            self.crossover_algorithm_implementation = OnePointCrossover()

        if 'multi_gen' in self.mutation_algorithm:
            self.mutation_algorithm_implementation = MultiGenMutation()
        else:
            self.mutation_algorithm_implementation = GenMutation()

        # ToDo: hay que agregar esto a los parametos y acordarse de verificar que sea par
        self.k = 1

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
        self.population_temp = 100 - self.generation

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
        self.generation += 1

        if self.stop_condition == 'generation_number':
            return self.stop_condition_implementation.check_stop(self.generation, self.generation_max)

        elif self.stop_condition == 'structure':
            fits_populations.sort(key=utils.sort_by_fitness, reverse=True)
            finished = self.stop_condition_implementation.check_stop(fits_populations, self.previous_generation)

            population_size_to_analyze = math.floor(len(fits_populations) * self.generation_percentage_to_say_equals)
            self.previous_generation = fits_populations.copy()[0:population_size_to_analyze]

            if finished:
                self.count_of_equal_generations += 1
            else:
                self.count_of_equal_generations = 0

            return self.count_of_equal_generations >= self.generation_number_to_say_equals

        elif self.stop_condition == 'content':
            fits = [f for f, ch in fits_populations]
            best_fit = max(fits)
            self.best_fits.append(best_fit)
            if self.generation % self.generation_number_to_say_equals == 0:
                return self.stop_condition_implementation.check_stop(self.best_fits, None)
            return False

        else:
            return self.stop_condition_implementation.check_stop(fits_populations, self.fitness_min)

    def selection(self, fits_populations):
        return self.selection_algorithm_implementation_1.selection(fits_populations, self.k)

    def crossover(self, father, mother):
        return self.crossover_algorithm_implementation.crossover(father, mother)

    # cambiar probabilidad si es no uniforme
    def mutation(self, chromosome):
        items_size = len(self.weapons)
        return self.mutation_algorithm_implementation.mutate(chromosome, items_size, self.prob_mutation)
