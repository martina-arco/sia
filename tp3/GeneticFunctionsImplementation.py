import GeneticFunctions
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

        self.limit = parameters.limit
        self.size = parameters.size

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
    # def random_chromo(self):
    #     return [random.randint(1, 255) for i in range(len(self.target))]

    def fitness(self, chromo):

        return self.attack_multiplier * self.attack(items, chromo.h) + self.defense_multiplier * self.defense(items, chromo.h)

    def force_p(self, items):
        return 100 * np.tanh(0.01 * self.force_multiplier * (weapons[items.weapon]['Fu'] + items.boots.Fu + items.helmet.Fu +
                                                             items.gloves.Fu + items.shirt.Fu))

    def agility_p(self, items):
        return np.tanh(0.01 * self.agility_multiplier * (items.weapon.Ag + items.boots.Ag + items.helmet.Ag +
                                                         items.gloves.Ag + items.shirt.Ag))

    def expertise_p(self, items):
        return 0.6 * np.tanh(0.01 * self.expertise_multiplier * (items.weapon.Ex + items.boots.Ex + items.helmet.Ex +
                                                                 items.gloves.Ex + items.shirt.Ex))

    def resistance_p(self, items):
        return np.tanh(0.01 * self.resistance_multiplier * (items.weapon.Re + items.boots.Re + items.helmet.Re +
                                                            items.gloves.Re + items.shirt.Re))

    def life_p(self, items):
        return 100 * np.tanh(0.01 * self.life_multiplier * (items.weapon.Vi + items.boots.Vi + items.helmet.Vi +
                                                            items.gloves.Vi + items.shirt.Vi))

    def ATM(self, h):
        return 0.5 - (3*h-5)**4 + (3*h-5)**2 + h/2

    def DEM(self, h):
        return 2 + (3*h-5)**4 - (3*h-5)**2 - h/2

    def attack(self, items, h):
        return (self.agility_p(items) + self.expertise_p(items)) * self.force_p(items) * self.ATM(h)

    def defense(self, items, h):
        return (self.resistance_p(items) + self.expertise_p(items)) * self.life_p(items) * self.DEM(h)

