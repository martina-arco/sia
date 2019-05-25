from GeneticFunctions import GeneticFunctions
import random
import numpy as np


class GeneticFunctionsImplementation(GeneticFunctions):
    def __init__(self, parameters):
        # prob_crossover=0.9, prob_mutation=0.2):
        self.counter = 0

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
        # self.size = parameters.size

        # self.prob_crossover = prob_crossover
        # self.prob_mutation = prob_mutation

    # GeneticFunctions interface impls
    # def probability_crossover(self):
    #     return self.prob_crossover
    #
    # def probability_mutation(self):
    #     return self.prob_mutation

    def initial(self):
        return [self.random_chromo() for j in range(self.size)]

    def check_stop(self, fits_populations):
        self.counter += 1
        if self.counter % 10 == 0:
            best_match = list(sorted(fits_populations))[-1][1]
            fits = [f for f, ch in fits_populations]
            best = max(fits)
            worst = min(fits)
            ave = sum(fits) / len(fits)
            print(
                "[G %3d] score=(%4d, %4d, %4d): %r" %
                (self.counter, best, ave, worst,
                 self.chromo2text(best_match)))
            pass
        return self.counter >= self.limit

    def selection(self, fits_populations):
        while True:
            father = self.tournament(fits_populations)
            mother = self.tournament(fits_populations)
            yield (father, mother)

    def crossover(self, parents):
        father, mother = parents
        index1 = random.randint(1, len(self.target) - 2)
        index2 = random.randint(1, len(self.target) - 2)
        if index1 > index2: index1, index2 = index2, index1
        child1 = father[:index1] + mother[index1:index2] + father[index2:]
        child2 = mother[:index1] + father[index1:index2] + mother[index2:]
        return (child1, child2)

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
    #
    # def text2chromo(self, text):
    #     return [ord(ch) for ch in text]
    #
    # def chromo2text(self, chromo):
    #     return "".join(chr(max(1, min(ch, 255))) for ch in chromo)
    #
    def random_chromo(self):
        return [random.randint(1, 255) for i in range(len(self.target))]

    # fitness definition
    def fitness(self, chromo):
        return (self.attack_multiplier * self.attack(chromo)) + \
               (self.defense_multiplier * self.defense(chromo))

    def attack(self, chromo):
        return (self.agility_p(chromo) + self.expertise_p(chromo)) * self.force_p(chromo) * self.ATM(chromo.h)

    def defense(self, chromo):
        return (self.resistance_p(chromo) + self.expertise_p(chromo)) * self.life_p(chromo) * self.DEM(chromo.h)

    def force_p(self, chromo):
        return 100 * np.tanh(0.01 * self.force_multiplier *
                             (self.weapons[chromo.weapon]['Fu'] + self.boots[chromo.boots]['Fu'] +
                              self.helmets[chromo.helmet]['Fu'] + self.gloves[chromo.glove]['Fu'] +
                              self.shirts[chromo.shirt]['Fu']))

    def agility_p(self, chromo):
        return np.tanh(0.01 * self.agility_multiplier *
                       (self.weapons[chromo.weapon]['Ag'] + self.boots[chromo.boots]['Ag'] +
                        self.helmets[chromo.helmet]['Ag'] + self.gloves[chromo.glove]['Ag'] +
                        self.shirts[chromo.shirt]['Ag']))

    def expertise_p(self, chromo):
        return 0.6 * np.tanh(0.01 * self.expertise_multiplier *
                             (self.weapons[chromo.weapon]['Ex'] + self.boots[chromo.boots]['Ex'] +
                              self.helmets[chromo.helmet]['Ex'] + self.gloves[chromo.glove]['Ex'] +
                              self.shirts[chromo.shirt]['Ex']))

    def resistance_p(self, chromo):
        return np.tanh(0.01 * self.resistance_multiplier *
                       (self.weapons[chromo.weapon]['Re'] + self.boots[chromo.boots]['Re'] +
                        self.helmets[chromo.helmet]['Re'] + self.gloves[chromo.glove]['Re'] +
                        self.shirts[chromo.shirt]['Re']))

    def life_p(self, chromo):
        return 100 * np.tanh(0.01 * self.life_multiplier *
                             (self.weapons[chromo.weapon]['Vi'] + self.boots[chromo.boots]['Vi'] +
                              self.helmets[chromo.helmet]['Vi'] + self.gloves[chromo.glove]['Vi'] +
                              self.shirts[chromo.shirt]['Vi']))

    def ATM(self, h):
        return 0.5 - (3 * h - 5) ** 4 + (3 * h - 5) ** 2 + h / 2

    def DEM(self, h):
        return 2 + (3 * h - 5) ** 4 - (3 * h - 5) ** 2 - h / 2
