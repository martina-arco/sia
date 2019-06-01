from algorithm_implementation.GeneticFunctionsImplementation import GeneticFunctionsImplementation
import argparse
import csv


def read_file(file_name):
    array = []
    with open(file_name) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
            array.append(row)

    return array


class Parameters:
    def __init__(self):

        self.population_size = 0
        self.prob_crossover = 0.0
        self.prob_mutation = 0.0
        
        self.stop_condition = ''
        self.selection_algorithm = ''
        self.crossover_algorithm = ''
        self.mutation_algorithm = ''

        self.fitness_min = 0
        self.generation_percentage_to_say_equals = 0.0
        self.generation_number_to_say_equals = 0
        self.max_generation = 0

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
        
    def set_prob_crossover(self, prob_crossover):
        self.prob_crossover = prob_crossover

    def set_prob_mutation(self, prob_mutation):
        self.prob_mutation = prob_mutation
        
    def set_stop_condition(self, stop_condition):
        self.stop_condition = stop_condition
    
    def set_selection_algorithm(self, selection_algorithm):
        self.selection_algorithm = selection_algorithm

    def set_crossover_algorithm(self, crossover_algorithm):
        self.crossover_algorithm = crossover_algorithm
        
    def set_mutation_algorithm(self, mutation_algorithm):
        self.mutation_algorithm = mutation_algorithm

    def set_fitness_min(self, fitness_min):
        self.fitness_min = fitness_min

    def set_generation_percentage_to_say_equals(self, generation_percentage_to_say_equals):
        self.generation_percentage_to_say_equals = generation_percentage_to_say_equals

    def set_generation_number_to_say_equals(self, generation_number_to_say_equals):
        self.generation_number_to_say_equals = generation_number_to_say_equals

    def set_max_generation(self, max_generation):
        self.max_generation = max_generation
        
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

    def set_scaling_algorithm(self, resistance_multiplier):
        self.resistance_multiplier = resistance_multiplier

    def set_initial_temperature(self, resistance_multiplier):
        self.resistance_multiplier = resistance_multiplier

    def set_temperature_step(self, resistance_multiplier):
        self.resistance_multiplier = resistance_multiplier
        
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
    parser = argparse.ArgumentParser(description='Run genetic algorithm.')

    parser.add_argument('-ps', '--population_size', type=int, default=1000,
                        help='Initial population size.')
    parser.add_argument('-pc', '--prob_crossover', type=float, default=0.9,
                        help='Probability of doing crossover.')
    parser.add_argument('-pm', '--prob_mutation', type=float, default=0.2,
                        help='Probability of mutating.')
    
    parser.add_argument('-sc', '--stop_condition', type=str, default='generation_number',
                        help='Stop condition for iterations.',
                        choices=['generation_number', 'structure', 'content', 'optimal'])
    parser.add_argument('-sa', '--selection_algorithm', type=str, default='elite',
                        help='Selection algorithm to use.',
                        choices=['elite', 'roulette', 'universal', 'tournament', 'ranking'])
    parser.add_argument('-ca', '--crossover_algorithm', type=str, default='one_point',
                        help='Crossover algorithm to use.',
                        choices=['one_point', 'two_points', 'uniform', 'anular'])
    parser.add_argument('-ma', '--mutation_algorithm', type=str, default='gen',
                        help='Mutation algorithm to use.',
                        choices=['uniform gen', 'uniform multi_gen', 'non_uniform gen', 'non_uniform multi_gen'])
    parser.add_argument('-sca', '--scaling_algorithm', type=str, default='none',
                        help='Scaling algorithm to use.',
                        choices=['none', 'boltzmann'])

    parser.add_argument('-fm', '--fitness_min', type=int, default=0,
                        help='Fitness considered to stop algorithm if it is less than that')
    parser.add_argument('-pe', '--generation_percentage_to_say_equals', type=float, default=1,
                        help='Percentage of equal chromosomes to consider one generation equal to another')
    parser.add_argument('-ne', '--generation_number_to_say_equals', type=int, default=10,
                        help='Number of equal fitnesses to consider it is not changing in generations')
    parser.add_argument('-max_g', '--max_generation', type=str, default=10000,
                        help='Max generation for stop condition.', required=False)
    parser.add_argument('-it', '--initial-temperature', type=int, default=100,
                        help='Initial temperature for scaling algorithm')
    parser.add_argument('-ts', '--temperature-step', type=float, default=1,
                        help='Temperature step per generation')

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

    weapons = read_file(args.weapons)
    boots = read_file(args.boots)
    helmets = read_file(args.helmets)
    gloves = read_file(args.gloves)
    shirts = read_file(args.shirts)

    parameters = Parameters()

    parameters.set_population_size(args.population_size)
    parameters.set_prob_crossover(args.prob_crossover)
    parameters.set_prob_mutation(args.prob_mutation)

    parameters.set_stop_condition(args.stop_condition)
    parameters.set_selection_algorithm(args.selection_algorithm)
    parameters.set_crossover_algorithm(args.crossover_algorithm)
    parameters.set_mutation_algorithm(args.mutation_algorithm)

    parameters.set_fitness_min(args.fitness_min)
    parameters.set_generation_percentage_to_say_equals(args.generation_percentage_to_say_equals)
    parameters.set_generation_number_to_say_equals(args.generation_number_to_say_equals)
    parameters.set_max_generation(args.max_generation)

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

    functionsImplementations = GeneticFunctionsImplementation(parameters)

    # GeneticAlgorithm(functionsImplementations).run()
