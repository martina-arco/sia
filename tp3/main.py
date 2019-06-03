import argparse
import csv
import utils
import time
from algorithm_implementation.GeneticFunctionsImplementation import GeneticFunctionsImplementation
from GeneticAlgorithm import GeneticAlgorithm
import matplotlib.pyplot as plt
import numpy as np


def read_file(file_name):
    array = []
    with open(file_name) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
            array.append(parse(row))
    return array


def parse(row):
    for key, value in row.items():
        if key == 'id':
            row[key] = int(value)
        else:
            row[key] = float(value)
    return row


class Parameters:
    def __init__(self):

        self.population_size = 0
        self.seed = ''
        
        self.stop_condition = ''
        self.crossover_algorithm = ''
        self.mutation_algorithm = ''
        self.scaling_algorithm = ''
        
        self.selection_algorithm_1 = ''
        self.selection_algorithm_2 = ''
        self.selection_algorithm_3 = ''
        self.selection_algorithm_4 = ''
        self.parent_selection_algorithm = ''
        self.percentage_for_selection = 0.0
        self.percentage_for_replacement = 0.0

        self.replacement_method = 0
        
        self.k = 0
        self.fitness_max = 0
        self.population_percentage_to_say_equals = 0.0
        self.generation_number_to_say_equals = 0
        self.max_generation = 0
        self.initial_temperature = 1
        self.temperature_step = 1.0
        self.prob_mutation = 0.0
        self.rate_mutation = 0.0

        self.attack_multiplier = ''
        self.defense_multiplier = ''
        
        self.force_multiplier = ''
        self.agility_multiplier = ''
        self.expertise_multiplier = ''
        self.resistance_multiplier = ''
        self.life_multiplier = ''
        
        self.weapons = []
        self.boots = []
        self.helmets = []
        self.gloves = []
        self.shirts = []

    def set_population_size(self, population_size):
        self.population_size = population_size

    def set_seed(self, seed):
        self.seed = seed
        
    def set_stop_condition(self, stop_condition):
        self.stop_condition = stop_condition

    def set_crossover_algorithm(self, crossover_algorithm):
        self.crossover_algorithm = crossover_algorithm
        
    def set_mutation_algorithm(self, mutation_algorithm):
        self.mutation_algorithm = mutation_algorithm
        
    def set_selection_algorithm_1(self, selection_algorithm):
        self.selection_algorithm_1 = selection_algorithm
        
    def set_selection_algorithm_2(self, selection_algorithm):
        self.selection_algorithm_2 = selection_algorithm
        
    def set_selection_algorithm_3(self, selection_algorithm):
        self.selection_algorithm_3 = selection_algorithm
        
    def set_selection_algorithm_4(self, selection_algorithm):
        self.selection_algorithm_4 = selection_algorithm
        
    def set_selection_algorithm_5(self, selection_algorithm):
        self.parent_selection_algorithm = selection_algorithm
        
    def set_percentage_1(self, percentage):
        self.percentage_for_selection = percentage
        
    def set_percentage_2(self, percentage):
        self.percentage_for_replacement = percentage

    def set_replacement_method(self, method):
        self.replacement_method = method

    def set_k(self, k):
        self.k = k

    def set_fitness_max(self, fitness_max):
        self.fitness_max = fitness_max

    def set_population_percentage_to_say_equals(self, generation_percentage_to_say_equals):
        self.population_percentage_to_say_equals = generation_percentage_to_say_equals

    def set_generation_number_to_say_equals(self, generation_number_to_say_equals):
        self.generation_number_to_say_equals = generation_number_to_say_equals

    def set_max_generation(self, max_generation):
        self.max_generation = max_generation

    def set_prob_mutation(self, prob_mutation):
        self.prob_mutation = prob_mutation
    
    def set_rate_mutation(self, rate_mutation):
        self.rate_mutation = rate_mutation
        
    def set_attack_multiplier(self, attack_multiplier):
        self.attack_multiplier = attack_multiplier

    def set_defense_multiplier(self, defense_multiplier):
        self.defense_multiplier = defense_multiplier
    
    def set_force_multiplier(self, force_multiplier):
        self.force_multiplier = force_multiplier
        
    def set_agility_multiplier(self, agility_multiplier):
        self.agility_multiplier = agility_multiplier
    
    def set_expertise_multiplier(self, expertise_multiplier):
        self.expertise_multiplier = expertise_multiplier

    def set_resistance_multiplier(self, resistance_multiplier):
        self.resistance_multiplier = resistance_multiplier

    def set_scaling_algorithm(self, scaling_algorithm):
        self.scaling_algorithm = scaling_algorithm

    def set_initial_temperature(self, initial_temperature):
        self.initial_temperature = initial_temperature

    def set_temperature_step(self, temperature_step):
        self.temperature_step = temperature_step
        
    def set_life_multiplier(self, life_multiplier):
        self.life_multiplier = life_multiplier
        
    def set_weapons(self, weapons):
        self.weapons = weapons
        
    def set_boots(self, boots):
        self.boots = boots
        
    def set_helmets(self, helmets):
        self.helmets = helmets
        
    def set_gloves(self, gloves):
        self.gloves = gloves
        
    def set_shirts(self, shirts):
        self.shirts = shirts


if __name__ == "__main__":
    start = time.time()
    parser = argparse.ArgumentParser(description='Run genetic algorithm.')

    parser.add_argument('-ps', '--population_size', type=int, default=100,
                        help='Initial population size.')
    parser.add_argument('-sd', '--seed', type=str, required=False,
                        help='Seed for initial population, must be a string of population size length')
    
    parser.add_argument('-sc', '--stop_condition', type=str, default='content',
                        help='Stop condition for iterations.',
                        choices=['generation_number', 'structure', 'content', 'optimal'])
    parser.add_argument('-ca', '--crossover_algorithm', type=str, default='one_point',
                        help='Crossover algorithm to use.',
                        choices=['one_point', 'two_points', 'uniform', 'anular'])
    parser.add_argument('-ma', '--mutation_algorithm', type=str, default='uniform_gen',
                        help='Mutation algorithm to use.',
                        choices=['uniform_gen', 'uniform_multi_gen', 'non_uniform_gen', 'non_uniform_multi_gen'])
    parser.add_argument('-sca', '--scaling_algorithm', type=str, default='none',
                        help='Scaling algorithm to use.',
                        choices=['none', 'boltzmann'])
    parser.add_argument('-rpm', '--replacement_method', type=int, default=1,
                        help='Replacement method to use.',
                        choices=[1, 2, 3])

    parser.add_argument('-sa1', '--selection_algorithm_1', type=str, default='probabilistic_tournament',
                        help='Selection algorithm to use for selection.',
                        choices=['elite', 'roulette', 'universal', 'tournament', 'probabilistic_tournament', 'ranking'])
    parser.add_argument('-sa2', '--selection_algorithm_2', type=str, default='roulette',
                        help='Selection algorithm to use for selection.',
                        choices=['elite', 'roulette', 'universal', 'tournament', 'probabilistic_tournament', 'ranking'])
    parser.add_argument('-sa3', '--selection_algorithm_3', type=str, default='probabilistic_tournament',
                        help='Selection algorithm to use for replacement.',
                        choices=['elite', 'roulette', 'universal', 'tournament', 'probabilistic_tournament', 'ranking'])
    parser.add_argument('-sa4', '--selection_algorithm_4', type=str, default='roulette',
                        help='Selection algorithm to use for replacement.',
                        choices=['elite', 'roulette', 'universal', 'tournament', 'probabilistic_tournament', 'ranking'])
    parser.add_argument('-sa5', '--selection_algorithm_5', type=str, default='tournament',
                        help='Selection algorithm to use for parents to crossover.',
                        choices=['elite', 'roulette', 'universal', 'tournament', 'probabilistic_tournament', 'ranking'])

    parser.add_argument('-p1', '--percentage_for_selection', type=float, default=0.5,
                        help='Percentage to use method 1 and 2 for selection.',
                        choices=np.arange(0, 1, 0.01))
    parser.add_argument('-p2', '--percentage_for_replacement', type=float, default=0.5,
                        help='Percentage to use method 3 and 4 for replacement.',
                        choices=np.arange(0, 1, 0.01))

    parser.add_argument('-k', '--k_selection', type=int, default=50,
                        help='Number of individuals to be selected.')
    parser.add_argument('-fm', '--fitness_max', type=int, default=0,
                        help='Fitness considered to stop algorithm if it is more than that')

    parser.add_argument('-pe', '--population_percentage_to_say_equals', type=float, default=0.7,
                        help='Percentage of equal chromosomes in population to consider one population equal to another',
                        choices=np.arange(0, 1, 0.01))
    parser.add_argument('-ne', '--generation_number_to_say_equals', type=int, default=10,
                        help='Number of equal generations, in the case of content it will be based on fitness, '
                             'in structure it is based on chromosome genes')

    parser.add_argument('-max_g', '--max_generation', type=int, default=1000,
                        help='Max generation for stop condition.', required=False)
    parser.add_argument('-it', '--initial-temperature', type=int, default=100,
                        help='Initial temperature for scaling algorithm')
    parser.add_argument('-ts', '--temperature-step', type=float, default=1,
                        help='Temperature step per generation')
    parser.add_argument('-pm', '--prob_mutation', type=float, default=0.2,
                        help='Probability of mutating.',
                        choices=np.arange(0, 1, 0.01))
    parser.add_argument('-rm', '--rate_mutation', type=float, default=0.2,
                        help='Rate at which mutation will decline in non uniform mutation.',
                        choices=np.arange(0, 1, 0.01))

    parser.add_argument('-atm', '--attack_multiplier', type=float, default=0.9,
                        help='Attack multiplier to use when calculating fitness.')
    parser.add_argument('-dfm', '--defense_multiplier', type=float, default=0.1,
                        help='Defense multiplier to use when calculating fitness.')

    parser.add_argument('-frm', '--force_multiplier', type=float, default=0.9,
                        help='Force multiplier to use when calculating fitness.')
    parser.add_argument('-agm', '--agility_multiplier', type=float, default=1.1,
                        help='Agility multiplier to use when calculating fitness.')
    parser.add_argument('-exm', '--expertise_multiplier', type=float, default=1,
                        help='Expertise multiplier to use when calculating fitness.')
    parser.add_argument('-rsm', '--resistance_multiplier', type=float, default=0.9,
                        help='Resistance multiplier to use when calculating fitness.')
    parser.add_argument('-lfm', '--life_multiplier', type=float, default=0.8,
                        help='Life multiplier to use when calculating fitness.')

    parser.add_argument('-w', '--weapons', type=str, default='testdata/armas.tsv',
                        help='Path to weapons file.')
    parser.add_argument('-b', '--boots', type=str, default='testdata/botas.tsv',
                        help='Path to boots file.')
    parser.add_argument('-hm', '--helmets', type=str, default='testdata/cascos.tsv',
                        help='Path to helmets file.')
    parser.add_argument('-g', '--gloves', type=str, default='testdata/guantes.tsv',
                        help='Path to helmets file.')
    parser.add_argument('-s', '--shirts', type=str, default='testdata/pecheras.tsv',
                        help='Path to shirts file.')

    args = parser.parse_args()

    if args.seed is not None and len(args.seed) != args.population_size:
        raise ValueError("Seed length must be equals to population size.")

    if args.k_selection > args.population_size or args.k_selection % 2 == 1:
        raise ValueError("K should be even and smaller than population size.")

    print('Loading data...')
    weapons = read_file(args.weapons)
    boots = read_file(args.boots)
    helmets = read_file(args.helmets)
    gloves = read_file(args.gloves)
    shirts = read_file(args.shirts)

    parameters = Parameters()

    parameters.set_population_size(args.population_size)
    parameters.set_seed(args.seed)

    parameters.set_stop_condition(args.stop_condition)
    parameters.set_crossover_algorithm(args.crossover_algorithm)
    parameters.set_mutation_algorithm(args.mutation_algorithm)
    parameters.set_scaling_algorithm(args.scaling_algorithm)

    parameters.set_selection_algorithm_1(args.selection_algorithm_1)
    parameters.set_selection_algorithm_2(args.selection_algorithm_2)
    parameters.set_selection_algorithm_3(args.selection_algorithm_3)
    parameters.set_selection_algorithm_4(args.selection_algorithm_4)
    parameters.set_selection_algorithm_5(args.selection_algorithm_5)

    parameters.set_percentage_1(args.percentage_for_selection)
    parameters.set_percentage_2(args.percentage_for_replacement)

    parameters.set_replacement_method(args.replacement_method)

    parameters.set_k(args.k_selection)
    parameters.set_fitness_max(args.fitness_max)
    parameters.set_population_percentage_to_say_equals(args.population_percentage_to_say_equals)
    parameters.set_generation_number_to_say_equals(args.generation_number_to_say_equals)
    parameters.set_max_generation(args.max_generation)
    parameters.set_initial_temperature(args.initial_temperature)
    parameters.set_temperature_step(args.temperature_step)
    parameters.set_prob_mutation(args.prob_mutation)
    parameters.set_rate_mutation(args.rate_mutation)

    parameters.set_attack_multiplier(args.attack_multiplier)
    parameters.set_defense_multiplier(args.defense_multiplier)

    parameters.set_force_multiplier(args.force_multiplier)
    parameters.set_agility_multiplier(args.agility_multiplier)
    parameters.set_expertise_multiplier(args.expertise_multiplier)
    parameters.set_resistance_multiplier(args.resistance_multiplier)
    parameters.set_life_multiplier(args.life_multiplier)

    parameters.set_weapons(weapons)
    parameters.set_boots(boots)
    parameters.set_helmets(helmets)
    parameters.set_gloves(gloves)
    parameters.set_shirts(shirts)

    print('Initializing algorithm')
    start_algorithm = time.time()
    functionsImplementations = GeneticFunctionsImplementation(parameters)

    GeneticAlgorithm(functionsImplementations).run()
    time_taken = time.time() - start
    print('Total time taken: ' + str(time_taken) + ' s')
    time_taken = time.time() - start_algorithm
    print('Algorithm time taken: ' + str(time_taken) + ' s')
    print('Amount of generations: ' + str(functionsImplementations.generation))
    print('Best fitness reached: ' + str(functionsImplementations.best_chromosome[utils.FITNESS]))
    print('Best chromosome: ' + str(functionsImplementations.best_chromosome[utils.CHROMOSOME]))
    plt.show()
