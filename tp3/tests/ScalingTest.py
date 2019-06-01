import unittest
import utils
import operator
from Chromosome import Chromosome

from algorithm_implementation.ScalingAlgorithms import NoScaling
from algorithm_implementation.ScalingAlgorithms import BoltzmannSelection

chromosome1 = Chromosome(genes=[1, 1, 1])
chromosome2 = Chromosome(genes=[2, 2, 2])
chromosome3 = Chromosome(genes=[3, 3, 3])
chromosome4 = Chromosome(genes=[4, 4, 4])
chromosome5 = Chromosome(genes=[5, 5, 5])
chromosome6 = Chromosome(genes=[6, 6, 6])


fits_population = [(1, chromosome1), (2, chromosome2), (3, chromosome3), (4, chromosome4), (5, chromosome5),
                   (6, chromosome6)]


def sorted_population():
    return sorted(fits_population, key=utils.sort_by_fitness, reverse=True)


class SelectionTest(unittest.TestCase):

    def test_no_scaling(self):
        scaling_algorithm = NoScaling()
        scaled_population = scaling_algorithm.scale(fits_population)
        self.assertEqual(scaled_population, fits_population)

    def test_roulette_selection(self):
        scaling_algorithm = BoltzmannSelection(100, 1)
        scaled_population = scaling_algorithm.scale(fits_population)
        self.assertEqual(len(scaled_population), len(fits_population))
        self.assertEqual(chromosome1, min(scaled_population)[1])    # Worst is still worst
        self.assertEqual(chromosome6, max(scaled_population)[1])    # Best is still best
