import unittest
import utils
import math

from Chromosome import Chromosome
from algorithm_implementation.StopConditions import MaxGenerationStopCondition
from algorithm_implementation.StopConditions import StructureStopCondition
from algorithm_implementation.StopConditions import ContentStopCondition
from algorithm_implementation.StopConditions import OptimalStopCondition

chromosome1 = Chromosome(genes=[1, 1, 1])
chromosome2 = Chromosome(genes=[2, 2, 2])
chromosome3 = Chromosome(genes=[3, 3, 3])
chromosome4 = Chromosome(genes=[4, 4, 4])
chromosome5 = Chromosome(genes=[5, 5, 5])
chromosome6 = Chromosome(genes=[6, 6, 6])


fits_population = [(1, chromosome1), (2, chromosome2), (3, chromosome3), (4, chromosome4), (5, chromosome5),
                   (5, chromosome5), (1, chromosome1), (3, chromosome3), (4, chromosome4), (2, chromosome2)]


class StopConditionsTest(unittest.TestCase):

    def test_max_generation(self):
        stop_condition = MaxGenerationStopCondition()
        self.assertFalse(stop_condition.check_stop(10, 11))
        self.assertTrue(stop_condition.check_stop(11, 10))

    def test_structure(self):
        stop_condition = StructureStopCondition()
        fits_population.sort(key=utils.sort_by_fitness, reverse=True)

        population_size_to_analyze = math.floor(len(fits_population) * 0.4)
        previous_generation_different = fits_population.copy()[0:population_size_to_analyze]
        previous_generation_different[1] = (4, chromosome4)

        self.assertFalse(stop_condition.check_stop(fits_population, previous_generation_different))
        self.assertTrue(stop_condition.check_stop(fits_population, fits_population[0:population_size_to_analyze]))

    def test_content(self):
        stop_condition = ContentStopCondition()
        best_fits_equals = [1, 1, 1, 1]
        best_fits_improves = [1, 1, 2, 3]

        self.assertTrue(stop_condition.check_stop(best_fits_equals))
        self.assertFalse(stop_condition.check_stop(best_fits_improves))

    def test_optimal(self):
        stop_condition = OptimalStopCondition()
        pass



