import utils
import math
import matplotlib.pyplot as plt

from algorithm_implementation.StopConditions import MaxGenerationStopCondition
from algorithm_implementation.StopConditions import StructureStopCondition
from algorithm_implementation.StopConditions import ContentStopCondition
from algorithm_implementation.StopConditions import OptimalStopCondition

from algorithm_implementation.SelectionAlgorithms import EliteSelection
from algorithm_implementation.SelectionAlgorithms import RouletteSelection
from algorithm_implementation.SelectionAlgorithms import UniversalSelection
from algorithm_implementation.SelectionAlgorithms import TournamentSelection
from algorithm_implementation.SelectionAlgorithms import RankingSelection

from algorithm_implementation.CrossoverAlgorithms import OnePointCrossover
from algorithm_implementation.CrossoverAlgorithms import TwoPointCrossover
from algorithm_implementation.CrossoverAlgorithms import UniformCrossover
from algorithm_implementation.CrossoverAlgorithms import AnularCrossover

from algorithm_implementation.MutationAlgorithms import GenMutation
from algorithm_implementation.MutationAlgorithms import MultiGenMutation

from algorithm_implementation.ScalingAlgorithms import NoScaling
from algorithm_implementation.ScalingAlgorithms import BoltzmannSelection
from algorithm_implementation.ScalingAlgorithms import RelativeScaling

from algorithm_implementation.ReplacementMethods import ReplacementOne
from algorithm_implementation.ReplacementMethods import ReplacementTwo
from algorithm_implementation.ReplacementMethods import ReplacementThree

from GeneticFunctions import GeneticFunctions
from Chromosome import Chromosome
from RealtimePlot import RealtimePlot


class GeneticFunctionsImplementation(GeneticFunctions):

    def __init__(self, parameters):
        self.generation = 0

        self.population_size = parameters.population_size
        self.seed = parameters.seed
        self.export_path = parameters.export_path

        self.stop_condition = parameters.stop_condition
        self.crossover_algorithm = parameters.crossover_algorithm
        self.mutation_algorithm = parameters.mutation_algorithm
        self.scaling_algorithm = parameters.scaling_algorithm
        self.replacement_method = parameters.replacement_method
        self.is_tournament_probabilistic = False

        self.selection_algorithm_1 = parameters.selection_algorithm_1
        self.selection_algorithm_2 = parameters.selection_algorithm_2
        self.selection_algorithm_3 = parameters.selection_algorithm_3
        self.selection_algorithm_4 = parameters.selection_algorithm_4

        self.percentage_for_selection = parameters.percentage_for_selection
        self.percentage_for_replacement = parameters.percentage_for_replacement

        if self.stop_condition == 'generation_number':
            self.stop_condition_implementation = MaxGenerationStopCondition()
        elif self.stop_condition == 'structure':
            self.stop_condition_implementation = StructureStopCondition()
        elif self.stop_condition == 'content':
            self.stop_condition_implementation = ContentStopCondition()
        else:
            self.stop_condition_implementation = OptimalStopCondition()

        self.generation_max = parameters.max_generation
        self.fitness_max = parameters.fitness_max
        self.population_percentage_to_say_equals = parameters.population_percentage_to_say_equals
        self.best_fits = []
        self.previous_generation = []
        self.count_of_equal_generations = 0
        self.generation_number_to_say_equals = parameters.generation_number_to_say_equals
        self.prob_mutation = parameters.prob_mutation
        self.rate_mutation = parameters.rate_mutation
        self.percentage_for_selection = parameters.percentage_for_selection

        if self.selection_algorithm_1 == 'elite':
            self.selection_algorithm_implementation_1 = EliteSelection()
        elif self.selection_algorithm_1 == 'roulette':
            self.selection_algorithm_implementation_1 = RouletteSelection()
        elif self.selection_algorithm_1 == 'universal':
            self.selection_algorithm_implementation_1 = UniversalSelection()
        elif 'tournament' in self.selection_algorithm_1:
            self.selection_algorithm_implementation_1 = TournamentSelection(
                'probabilistic' in self.selection_algorithm_1)
        elif self.selection_algorithm_1 == 'ranking':
            self.selection_algorithm_implementation_1 = RankingSelection()

        if self.selection_algorithm_2 == 'elite':
            self.selection_algorithm_implementation_2 = EliteSelection()
        elif self.selection_algorithm_2 == 'roulette':
            self.selection_algorithm_implementation_2 = RouletteSelection()
        elif self.selection_algorithm_2 == 'universal':
            self.selection_algorithm_implementation_2 = UniversalSelection()
        elif 'tournament' in self.selection_algorithm_2:
            self.selection_algorithm_implementation_2 = TournamentSelection(
                'probabilistic' in self.selection_algorithm_2)
        elif self.selection_algorithm_2 == 'ranking':
            self.selection_algorithm_implementation_2 = RankingSelection()

        if self.selection_algorithm_3 == 'elite':
            self.selection_algorithm_implementation_3 = EliteSelection()
        elif self.selection_algorithm_3 == 'roulette':
            self.selection_algorithm_implementation_3 = RouletteSelection()
        elif self.selection_algorithm_3 == 'universal':
            self.selection_algorithm_implementation_3 = UniversalSelection()
        elif 'tournament' in self.selection_algorithm_3:
            self.selection_algorithm_implementation_3 = TournamentSelection(
                'probabilistic' in self.selection_algorithm_3)
        elif self.selection_algorithm_3 == 'ranking':
            self.selection_algorithm_implementation_3 = RankingSelection()

        if self.selection_algorithm_4 == 'elite':
            self.selection_algorithm_implementation_4 = EliteSelection()
        elif self.selection_algorithm_4 == 'roulette':
            self.selection_algorithm_implementation_4 = RouletteSelection()
        elif self.selection_algorithm_4 == 'universal':
            self.selection_algorithm_implementation_4 = UniversalSelection()
        elif 'tournament' in self.selection_algorithm_4:
            self.selection_algorithm_implementation_4 = TournamentSelection(
                'probabilistic' in self.selection_algorithm_4)
        elif self.selection_algorithm_4 == 'ranking':
            self.selection_algorithm_implementation_4 = RankingSelection()

        if parameters.parent_selection_algorithm == 'elite':
            self.parent_selection_algorithm = EliteSelection()
        elif parameters.parent_selection_algorithm == 'roulette':
            self.parent_selection_algorithm = RouletteSelection()
        elif parameters.parent_selection_algorithm == 'universal':
            self.parent_selection_algorithm = UniversalSelection()
        elif 'tournament' in parameters.parent_selection_algorithm:
            self.parent_selection_algorithm = TournamentSelection(
                'probabilistic' in parameters.parent_selection_algorithm)
        elif parameters.parent_selection_algorithm == 'ranking':
            self.parent_selection_algorithm = RankingSelection()

        if self.scaling_algorithm == 'boltzmann':
            self.scaling_algorithm_implementation = BoltzmannSelection(parameters.initial_temperature,
                                                                       parameters.temperature_step)
        if self.scaling_algorithm == 'relative':
            self.scaling_algorithm_implementation = RelativeScaling()
        else:
            self.scaling_algorithm_implementation = NoScaling()

        if self.crossover_algorithm == 'anular':
            self.crossover_algorithm_implementation = AnularCrossover()
        elif self.crossover_algorithm == 'two_points':
            self.crossover_algorithm_implementation = TwoPointCrossover()
        elif self.crossover_algorithm == 'uniform':
            self.crossover_algorithm_implementation = UniformCrossover()
        else:
            self.crossover_algorithm_implementation = OnePointCrossover()

        if self.replacement_method == 1:
            self.replacement_method_implementation = ReplacementOne(parameters.population_size)
        elif self.replacement_method == 2:
            self.replacement_method_implementation = ReplacementTwo(parameters.population_size,
                                                                    self.selection_algorithm_implementation_3,
                                                                    parameters.percentage_for_replacement,
                                                                    self.selection_algorithm_implementation_4)
        elif self.replacement_method == 3:
            self.replacement_method_implementation = ReplacementThree(parameters.population_size,
                                                                      self.selection_algorithm_implementation_3,
                                                                      parameters.percentage_for_replacement,
                                                                      self.selection_algorithm_implementation_4)

        # ToDo: Acordarse de verificar que sea par
        self.k = parameters.k

        # ToDo: Verificar que esto esta bien cortado
        self.best_chromosome = (0, Chromosome(1))

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

        if 'multi_gen' in self.mutation_algorithm:
            self.mutation_algorithm_implementation = MultiGenMutation(self.prob_mutation, self.rate_mutation,
                                                                      len(self.weapons))
        else:
            self.mutation_algorithm_implementation = GenMutation(self.prob_mutation, self.rate_mutation,
                                                                 len(self.weapons))
        # Plotting
        self.plot_freq = 1
        self.max_fitness_plot = RealtimePlot(x_label='Generation', y_label='Max Fitness')
        self.average_fitness_plot = RealtimePlot(x_label='Generation', y_label='Average Fitness')
        self.chromosome_diversity_plot = RealtimePlot(x_label='Generation', y_label='Amount of different chromosomes')

    def initial(self):
        population = []

        for i in range(0, self.population_size):
            if self.seed is not None:
                chromosome = Chromosome(items_size=len(self.weapons), seed=self.seed[i])
            else:
                chromosome = Chromosome(items_size=len(self.weapons))
            population.append(chromosome)

        return population

    def fitness(self, chromosome):
        return chromosome.calculate_fitness(self.attack_multiplier, self.defense_multiplier, self.force_multiplier,
                                            self.agility_multiplier, self.expertise_multiplier,
                                            self.resistance_multiplier,
                                            self.life_multiplier, self.weapons, self.boots, self.helmets, self.gloves,
                                            self.shirts)

    def check_stop(self, fits_populations):
        self.generation += 1
        fits_populations.sort(key=utils.sort_by_fitness, reverse=True)
        best_fit = fits_populations[0][utils.FITNESS]
        if best_fit > self.best_chromosome[utils.FITNESS]:
            self.best_chromosome = fits_populations[0]

        if self.stop_condition == 'generation_number':
            return self.stop_condition_implementation.check_stop(self.generation, self.generation_max)

        elif self.stop_condition == 'structure':
            finished = self.stop_condition_implementation.check_stop(fits_populations, self.previous_generation)
            population_size_to_analyze = math.floor(len(fits_populations) * self.population_percentage_to_say_equals)
            self.previous_generation = fits_populations.copy()[0:population_size_to_analyze]

            if finished:
                self.count_of_equal_generations += 1
            else:
                self.count_of_equal_generations = 0

            return self.count_of_equal_generations >= self.generation_number_to_say_equals

        elif self.stop_condition == 'content':
            self.best_fits.append(best_fit)
            if self.generation % self.generation_number_to_say_equals == 0:
                finished = self.stop_condition_implementation.check_stop(self.best_fits, None)
                self.best_fits.clear()
                return finished
            return False

        else:
            return self.stop_condition_implementation.check_stop(best_fit, self.fitness_max)

    def selection(self, fits_populations):
        method1 = self.selection_algorithm_implementation_1.selection(fits_populations,
                                                                      math.ceil(self.k * self.percentage_for_selection))
        method2 = self.selection_algorithm_implementation_2.selection(fits_populations,
                                                                      math.floor(self.k * (1 - self.percentage_for_selection)))
        return method1 + method2

    def crossover(self, father, mother):
        return self.crossover_algorithm_implementation.crossover(father, mother)

    def mutation(self, chromosome):
        return self.mutation_algorithm_implementation.mutate(chromosome)

    def fitness_scaling(self, fits_population):
        return self.scaling_algorithm_implementation.scale(fits_population)

    def replacement(self, parents, children):
        return self.replacement_method_implementation.replacement(parents, children)

    def offspring_size(self):
        return self.replacement_method_implementation.offspring_size()

    def update_parameters(self):
        if 'non_uniform' in self.mutation_algorithm:
            self.mutation_algorithm_implementation.update_parameters()
        self.scaling_algorithm_implementation.update_parameters()

    def parent_selection(self, parent_pool):
        return self.parent_selection_algorithm.selection(parent_pool, 2)

    def plot(self, population_fitness):
        different_chromosomes = set()
        fitness_sum = 0

        for fit, ch in population_fitness:
            fitness_sum += fit
            different_chromosomes.add(ch)

        avg_fitness = fitness_sum / len(population_fitness)
        max_fitness = max(population_fitness)[0]
        self.max_fitness_plot.add(self.generation, max_fitness)
        self.average_fitness_plot.add(self.generation, avg_fitness)
        self.chromosome_diversity_plot.add(self.generation, len(different_chromosomes))
        # plt.pause(0.001)

    def save_data(self):
        self.max_fitness_plot.save(self.export_path + '_max_fitness.p')
        self.average_fitness_plot.save(self.export_path + '_avg_fitness.p')
        self.chromosome_diversity_plot.save(self.export_path + '_chromosome_diversity.p')
