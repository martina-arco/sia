import unittest
import utils
from Chromosome import Chromosome

from algorithm_implementation.SelectionAlgorithms import EliteSelection
from algorithm_implementation.SelectionAlgorithms import RouletteSelection

chromosome1 = Chromosome(genes=[1, 1, 1])
chromosome2 = Chromosome(genes=[2, 2, 2])
chromosome3 = Chromosome(genes=[3, 3, 3])
chromosome4 = Chromosome(genes=[4, 4, 4])
chromosome5 = Chromosome(genes=[5, 5, 5])
chromosome6 = Chromosome(genes=[6, 6, 6])


fits_population = [(1, chromosome1), (2, chromosome2), (3, chromosome3), (4, chromosome4), (5, chromosome5),
                   (5, chromosome5), (1, chromosome1), (3, chromosome3), (4, chromosome4), (2, chromosome2)]


def sorted_population():
    return sorted(fits_population, key=utils.sort_by_fitness, reverse=True)


class SelectionTest(unittest.TestCase):

    def test_elite_selection(self):
        selection_algorithm = EliteSelection()

        parents = selection_algorithm.selection(fits_population, 5)
        expected = [chromosome5, chromosome5, chromosome4, chromosome4, chromosome3]
        self.assertEqual(parents, expected)

    def test_roulette_selection(self):
        selection_algorithm = RouletteSelection()
        parents = selection_algorithm.selection(fits_population, 5)
        self.assertEqual(len(parents), 5)
        parents = selection_algorithm.selection(fits_population, 10)
        self.assertIn(chromosome1, parents)


