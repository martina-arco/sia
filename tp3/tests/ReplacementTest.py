import unittest
from Chromosome import Chromosome

from algorithm_implementation.ReplacementMethods import ReplacementTwo
from algorithm_implementation.ReplacementMethods import ReplacementThree

from algorithm_implementation.SelectionAlgorithms import EliteSelection
from algorithm_implementation.SelectionAlgorithms import RouletteSelection

chromosome1 = Chromosome(genes=[1, 1, 1])
chromosome2 = Chromosome(genes=[2, 2, 2])
chromosome3 = Chromosome(genes=[3, 3, 3])
chromosome4 = Chromosome(genes=[4, 4, 4])
chromosome5 = Chromosome(genes=[5, 5, 5])
chromosome6 = Chromosome(genes=[6, 6, 6])
chromosome7 = Chromosome(genes=[7, 7, 7])
chromosome8 = Chromosome(genes=[8, 8, 8])
chromosome9 = Chromosome(genes=[9, 9, 9])
chromosome10 = Chromosome(genes=[10, 10, 10])


fits_population = [(1, chromosome1), (2, chromosome2), (3, chromosome3), (4, chromosome4), (5, chromosome5),
                   (6, chromosome6)]

offspring = [(7, chromosome7), (8, chromosome8), (9, chromosome9), (10, chromosome10)]


class ReplacementTest(unittest.TestCase):
    def test_replacement_two(self):
        selection_1 = RouletteSelection()
        selection_2 = EliteSelection()
        replacement_method = ReplacementTwo(len(offspring), selection_1, 0.5, selection_2, 0.5)

        selected = replacement_method.replacement(fits_population, offspring)
        self.assertIn(offspring[0][1], selected)
        self.assertIn(offspring[1][1], selected)
        self.assertIn(offspring[2][1], selected)
        self.assertIn(offspring[3][1], selected)
        self.assertEqual(len(selected), len(fits_population))

    def test_replacement_three(self):
        selection_1 = RouletteSelection()
        selection_2 = EliteSelection()
        replacement_method = ReplacementThree(len(offspring), selection_1, 0.5, selection_2, 0.5)

        selected = replacement_method.replacement(fits_population, offspring)

        self.assertEqual(len(selected), len(fits_population))