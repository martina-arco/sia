import unittest

from Chromosome import Chromosome
from algorithm_implementation.MutationAlgorithms import GenMutation
from algorithm_implementation.MutationAlgorithms import MultiGenMutation

chromosome1 = Chromosome(genes=[1, 1, 1, 1, 1, 1])
chromosome4 = Chromosome(genes=[4, 4, 4, 4, 4, 4])


class MutationTest(unittest.TestCase):

    def test_gen_mutation(self):
        mutation_algorithm = GenMutation()
        items_size = 3
        chromosome_with_mutation = mutation_algorithm.mutate(chromosome4, items_size, 1)
        chromosome_without_mutation = mutation_algorithm.mutate(chromosome4, items_size, 0)

        self.assertNotEqual(chromosome4, chromosome_with_mutation)
        self.assertEqual(chromosome4, chromosome_without_mutation)

    def test_multi_gen_mutation(self):
        mutation_algorithm = MultiGenMutation()
        items_size = 3
        chromosome_with_mutation = mutation_algorithm.mutate(chromosome4, items_size, 1)
        chromosome_with_some_mutation = mutation_algorithm.mutate(chromosome4, items_size, 0.5)
        chromosome_without_mutation = mutation_algorithm.mutate(chromosome4, items_size, 0)

        self.assertNotEqual(chromosome4, chromosome_with_mutation)
        self.assertNotEqual(chromosome4, chromosome_with_some_mutation)
        self.assertEqual(chromosome4, chromosome_without_mutation)


