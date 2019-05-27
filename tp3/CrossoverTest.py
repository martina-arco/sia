import unittest

from CrossoverAlgorithm import CrossoverAlgorithm
from Chromosome import Chromosome

MOTHER1 = [1, 1, 0, 0, 0, 0, 1, 1, 1]
FATHER1 = [1, 0, 0, 1, 1, 1, 0, 1, 0]

CHILD1 = [1, 1, 0, 1, 1, 1, 0, 1, 0]
CHILD2 = [1, 0, 0, 0, 0, 0, 1, 1, 1]


class CrossoverTest(unittest.TestCase):

    def test_one_point_crossover(self):
        mother1 = Chromosome(genes=[1, 1, 0, 0, 0, 0, 1, 1, 1])
        father1 = Chromosome(genes=[1, 0, 0, 1, 1, 1, 0, 1, 0])

        child1 = Chromosome(genes=[1, 1, 0, 0, 1, 1, 0, 1, 0])
        child2 = Chromosome(genes=[1, 0, 0, 1, 0, 0, 1, 1, 1])
        expected1 = child1, child2
        function_result1 = CrossoverAlgorithm.one_point_crossover(mother1, father1, 4)

        child1 = Chromosome(genes=[1, 1, 0, 0, 0, 0, 1, 1, 1])
        child2 = Chromosome(genes=[1, 0, 0, 1, 1, 1, 0, 1, 0])
        expected2 = child2, child1
        function_result2 = CrossoverAlgorithm.one_point_crossover(mother1, father1, 0)

        self.assertEqual(function_result1, expected1, "Should be equals")
        self.assertEqual(function_result2, expected2, "Should be equals")

    def test_two_points_crossover(self):
        father = Chromosome(genes=[1, 1, 0, 1, 1, 0, 0, 1, 1])
        mother = Chromosome(genes=[0, 1, 1, 1, 0, 0, 1, 0, 1])

        child1 = Chromosome(genes=[1, 1, 0, 1, 0, 0, 0, 1, 1])
        child2 = Chromosome(genes=[0, 1, 1, 1, 1, 0, 1, 0, 1])
        expected1 = child1, child2
        function_result1 = CrossoverAlgorithm.two_point_crossover(father, mother, 3, 4)

        child1 = Chromosome(genes=[0, 1, 1, 1, 1, 0, 0, 1, 1])
        child2 = Chromosome(genes=[1, 1, 0, 1, 0, 0, 1, 0, 1])
        expected2 = child1, child2
        function_result2 = CrossoverAlgorithm.two_point_crossover(father, mother, 0, 2)

        child1 = Chromosome(genes=[1, 1, 1, 1, 1, 0, 0, 1, 1])
        child2 = Chromosome(genes=[0, 1, 0, 1, 0, 0, 1, 0, 1])
        expected3 = child1, child2
        function_result3 = CrossoverAlgorithm.two_point_crossover(father, mother, 2, 2)

        child2 = Chromosome(genes=[0, 1, 0, 1, 1, 0, 0, 1, 1])
        child3 = Chromosome(genes=[1, 1, 1, 1, 0, 0, 1, 0, 1])
        expected4 = child2, child3
        function_result4 = CrossoverAlgorithm.two_point_crossover(father, mother, 0, 0)

        self.assertEqual(function_result1, expected1, "Should be equals")
        self.assertEqual(function_result2, expected2, "Should be equals")
        self.assertEqual(function_result3, expected3, "Should be equals")
        self.assertEqual(function_result4, expected4, "Should be equals")

    def test_anular_crossover(self):
        father = Chromosome(genes=[1, 1, 0, 1, 1, 0, 0, 1, 1])
        mother = Chromosome(genes=[0, 1, 1, 1, 0, 0, 1, 0, 1])

        child1 = Chromosome(genes=[1, 1, 0, 1, 1, 0, 1, 1, 1])
        child2 = Chromosome(genes=[0, 1, 1, 1, 0, 0, 0, 0, 1])
        expected1 = child1, child2
        function_result1 = CrossoverAlgorithm.anular_crossover(father, mother, 5, 2)

        child1 = Chromosome(genes=[0, 1, 0, 1, 1, 0, 0, 0, 1])
        child2 = Chromosome(genes=[1, 1, 1, 1, 0, 0, 1, 1, 1])
        expected2 = child1, child2
        function_result2 = CrossoverAlgorithm.anular_crossover(father, mother, 7, 4)

        self.assertEqual(function_result1, expected1, "Should be equals")
        self.assertEqual(function_result2, expected2, "Should be equals")


if __name__ == "__main__":
    unittest.main()

