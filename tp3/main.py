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
        
        self.stop_condition = ''
        self.selection_algorithm = ''
        self.crossover_algorithm = ''
        self.mutation_algorithm = ''

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

        self.max_generation = 1000
        self.population_size = 1000
        
    def set_stop_condition(self, stop_condition):
        self.stop_condition = stop_condition
    
    def set_selection_algorithm(self, selection_algorithm):
        self.selection_algorithm = selection_algorithm

    def set_crossover_algorithm(self, crossover_algorithm):
        self.crossover_algorithm = crossover_algorithm
        
    def set_mutation_algorithm(self, mutation_algorithm):
        self.mutation_algorithm = mutation_algorithm
        
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

    def set_population_size(self, population_size):
        self.population_size = population_size

    def set_max_generation(self, max_generation):
        self.max_generation = max_generation


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run genetic algorithm.')
    parser.add_argument('-sc', '--stop_condition', type=str, default='generation_number',
                        help='Stop condition for iterations.')
    parser.add_argument('-sa', '--selection_algorithm', type=str, default='elite',
                        help='Selection algorithm to use.')
    parser.add_argument('-ca', '--crossover_algorithm', type=str, default='one_point',
                        help='Crossover algorithm to use.',
                        choices=['one_point', 'two_points', 'uniform', 'anular'])
    parser.add_argument('-ma', '--mutation_algorithm', type=str, default='gen',
                        help='Mutation algorithm to use.')

    parser.add_argument('-am', '--attack_multiplier', type=float, default=0.9,
                        help='Attack multiplier to use when calculating fitness.')
    parser.add_argument('-dm', '--defense_multiplier', type=float, default=0.1,
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

    parser.add_argument('-max_g', '--max_generation', type=str, default=10000,
                        help='Max generation for stop condition.', required=False)
    args = parser.parse_args()

    weapons = read_file(args.weapons)
    boots = read_file(args.boots)
    helmets = read_file(args.helmets)
    gloves = read_file(args.gloves)
    shirts = read_file(args.shirts)

    parameters = Parameters()

    parameters.set_stop_condition(args.stop_condition)
    parameters.set_selection_algorithm(args.selection_algorithm)
    parameters.set_crossover_algorithm(args.crossover_algorithm)
    parameters.set_mutation_algorithm(args.mutation_algorithm)

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

    parameters.set_max_generation(args.max_generation)

    functionsImplementations = GeneticFunctionsImplementation(parameters)

    # GeneticAlgorithm(functionsImplementations).run()
