import numpy as np
import random
import utils


class Chromosome:

    def __init__(self, items_size=0, genes=None, seed=None):
        if seed is not None:
            self.genes = []
            random.seed(seed)
            for i in range(utils.CHROMOSOME_SIZE):
                if i != utils.HEIGHT:
                    self.genes.append(random.randint(0, items_size-1))
                else:
                    self.genes.append(random.uniform(1.3, 2))

        elif genes is None:
            self.genes = [random.randint(0, items_size - 1), random.randint(0, items_size - 1), random.randint(0, items_size - 1),
                          random.randint(0, items_size - 1), random.randint(0, items_size - 1), random.uniform(1.3, 2)]
        else:
            self.genes = genes

    def calculate_fitness(self, attack_multiplier, defense_multiplier, force_multiplier, agility_multiplier,
                          expertise_multiplier, resistance_multiplier, life_multiplier,
                          weapons, boots, helmets, gloves, shirts):

        return (attack_multiplier *
                self.attack(force_multiplier, agility_multiplier, expertise_multiplier, weapons, boots, helmets, gloves,
                            shirts)) + \
               (defense_multiplier *
                self.defense(expertise_multiplier, resistance_multiplier, life_multiplier, weapons, boots, helmets,
                             gloves, shirts))

    def attack(self, force_multiplier, agility_multiplier, expertise_multiplier,
               weapons, boots, helmets, gloves, shirts):
        return (self.agility_p(agility_multiplier, weapons, boots, helmets, gloves, shirts) +
                self.expertise_p(expertise_multiplier, weapons, boots, helmets, gloves, shirts)) * \
               self.force_p(force_multiplier, weapons, boots, helmets, gloves, shirts) * self.atm()

    def defense(self, expertise_multiplier, resistance_multiplier, life_multiplier,
                weapons, boots, helmets, gloves, shirts):
        return (self.resistance_p(resistance_multiplier, weapons, boots, helmets, gloves, shirts) +
                self.expertise_p(expertise_multiplier, weapons, boots, helmets, gloves, shirts)) * \
               self.life_p(life_multiplier, weapons, boots, helmets, gloves, shirts) * self.dem()

    def force_p(self, force_multiplier, weapons, boots, helmets, gloves, shirts):
        return 100 * self.calculate_stat('Fu', force_multiplier, weapons, boots, helmets, gloves, shirts)

    def agility_p(self, agility_multiplier, weapons, boots, helmets, gloves, shirts):
        return self.calculate_stat('Ag', agility_multiplier, weapons, boots, helmets, gloves, shirts)

    def expertise_p(self, expertise_multiplier, weapons, boots, helmets, gloves, shirts):
        return 0.6 * self.calculate_stat('Ex', expertise_multiplier, weapons, boots, helmets, gloves, shirts)

    def resistance_p(self, resistance_multiplier, weapons, boots, helmets, gloves, shirts):
        return self.calculate_stat('Re', resistance_multiplier, weapons, boots, helmets, gloves, shirts)

    def life_p(self, life_multiplier, weapons, boots, helmets, gloves, shirts):
        return 100 * self.calculate_stat('Vi', life_multiplier, weapons, boots, helmets, gloves, shirts)

    def atm(self):
        return 0.5 - (3 * self.genes[utils.HEIGHT] - 5) ** 4 + (3 * self.genes[utils.HEIGHT] - 5) ** 2 + \
               self.genes[utils.HEIGHT] / 2

    def dem(self):
        return 2 + (3 * self.genes[utils.HEIGHT] - 5) ** 4 - (3 * self.genes[utils.HEIGHT] - 5) ** 2 - \
               self.genes[utils.HEIGHT] / 2

    def calculate_stat(self, stat, multiplier, weapons, boots, helmets, gloves, shirts):
        return np.tanh(0.01 * multiplier *
                       (weapons[self.genes[utils.WEAPON]][stat] + boots[self.genes[utils.BOOT]][stat] +
                        helmets[self.genes[utils.HELMET]][stat] + gloves[self.genes[utils.GLOVE]][stat] +
                        shirts[self.genes[utils.SHIRT]][stat]))

    def __str__(self):
        string = "Weapon: " + str(self.genes[utils.WEAPON]) + ", "
        string += "Boot: " + str(self.genes[utils.BOOT]) + ", "
        string += "Helmet: " + str(self.genes[utils.HELMET]) + ", "
        string += "Glove: " + str(self.genes[utils.GLOVE]) + ", "
        string += "Shirt: " + str(self.genes[utils.SHIRT]) + ", "
        string += "Height: " + str(self.genes[utils.HEIGHT])
        return string

    def __hash__(self):
        hash_result = 0
        for i in range(0, len(self.genes)):
            hash_result += hash(self.genes[i])
        return hash_result

    def __eq__(self, other):
        if isinstance(other, Chromosome):
            return np.array_equal(self.genes, other.genes)
        return False
