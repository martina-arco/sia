import unittest
import main
import numpy as np

from Chromosome import Chromosome

chromosome1 = Chromosome(genes=[1, 1, 1, 1, 1, 1.5])


class FitnessTest(unittest.TestCase):

    def test_fitness(self):
        weapons = main.read_file('../testdata/armas.tsv')
        boots = main.read_file('../testdata/botas.tsv')
        helmets = main.read_file('../testdata/cascos.tsv')
        gloves = main.read_file('../testdata/guantes.tsv')
        shirts = main.read_file('../testdata/pecheras.tsv')

        attack_multiplier = 0.9
        defense_multiplier = 0.1
        force_multiplier = 0.9
        agility_multiplier = 1.1
        expertise_multiplier = 1
        resistance_multiplier = 0.9
        life_multiplier = 0.8

        expected_p_force = 100 * np.tanh(0.01 * force_multiplier * (6.222216242390499 + 2.2027931206638347 +
                                                                    7.658380825287503 + 1.5663864556588252 +
                                                                    9.723360073495009))
        expected_p_agility = np.tanh(0.01 * agility_multiplier * (6.541324168418127 + 2.1657134566632457 +
                                                                  4.820703103477169 + 2.9881879858036853 +
                                                                  3.3550178576619367))
        expected_p_expertise = 0.6 * np.tanh(0.01 * expertise_multiplier * (12.31869383349377 + 0.8576268312008092 +
                                                                            2.5555670851728705 + 0.6172399843576923 +
                                                                            5.242037515433561))
        expected_p_resistance = np.tanh(0.01 * resistance_multiplier * (7.171230587646848 + 2.117799836003941 +
                                                                        6.664915444307471 + 0.971997463425301 +
                                                                        17.913489499483834))
        expected_p_life = 100 * np.tanh(0.01 * life_multiplier * (9.506924539924945 + 1.4986193316990624 +
                                                                  4.495328669692497 + 3.0986140589878577 +
                                                                  2.726878650158977))

        expected_atm = 1.4375
        expected_dem = 1.0625
        attack = (expected_p_agility + expected_p_expertise) * expected_p_force * expected_atm
        defense = (expected_p_resistance + expected_p_expertise) * expected_p_life * expected_dem
        expected_fitness = attack * attack_multiplier + defense * defense_multiplier
        fitness = chromosome1.calculate_fitness(attack_multiplier, defense_multiplier, force_multiplier,
                                                agility_multiplier, expertise_multiplier, resistance_multiplier,
                                                life_multiplier, weapons, boots, helmets, gloves, shirts)
        self.assertEqual(fitness, expected_fitness)


