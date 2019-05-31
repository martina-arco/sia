import unittest

from Chromosome import Chromosome
from algorithm_implementation.StopConditions import MaxGenerationStopCondition
from algorithm_implementation.StopConditions import StructureStopCondition
from algorithm_implementation.StopConditions import ContentStopCondition
from algorithm_implementation.StopConditions import OptimalStopCondition

chromosome1 = Chromosome(genes=[1, 1, 1])
chromosome2 = Chromosome(genes=[2, 2, 2])


class StopConditionsTest(unittest.TestCase):

    def test_max_generation(self):
        stop_condition = MaxGenerationStopCondition()
        self.assertFalse(stop_condition.check_stop(10, 11))
        self.assertTrue(stop_condition.check_stop(11, 10))

    def test_structure(self):
        stop_condition = StructureStopCondition()
        # first 3 are the same, then they are different
        fits_population = [(10, chromosome1), (4, chromosome2), (9, chromosome1), (8, chromosome2), (5, chromosome2),
                           (5, chromosome1), (10, chromosome1), (5, chromosome1), (7, chromosome2), (5, chromosome1)]

        self.assertFalse(stop_condition.check_stop(fits_population, 0.9))
        self.assertFalse(stop_condition.check_stop(fits_population, 0.4))
        self.assertTrue(stop_condition.check_stop(fits_population, 0.3))

    def test_content(self):
        stop_condition = ContentStopCondition()
        best_fits_equals = [1, 1, 1, 1]
        best_fits_improves = [1, 1, 2, 3]

        self.assertTrue(stop_condition.check_stop(best_fits_equals))
        self.assertFalse(stop_condition.check_stop(best_fits_improves))

    def test_optimal(self):
        stop_condition = OptimalStopCondition()
        pass



