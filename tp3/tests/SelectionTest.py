import random
import unittest
import utils
from Chromosome import Chromosome

from algorithm_implementation.SelectionAlgorithms import EliteSelection, TournamentSelection
from algorithm_implementation.SelectionAlgorithms import RouletteSelection
from algorithm_implementation.SelectionAlgorithms import UniversalSelection
from algorithm_implementation.SelectionAlgorithms import RankingSelection

chromosome1 = Chromosome(genes=[1, 1, 1])
chromosome2 = Chromosome(genes=[2, 2, 2])
chromosome3 = Chromosome(genes=[3, 3, 3])
chromosome4 = Chromosome(genes=[4, 4, 4])
chromosome5 = Chromosome(genes=[5, 5, 5])
chromosome6 = Chromosome(genes=[6, 6, 6])


fits_population = [(1, chromosome1), (2, chromosome2), (3, chromosome3), (4, chromosome4), (5, chromosome5),
                   (5, chromosome5), (1, chromosome1), (3, chromosome3), (4, chromosome4), (2, chromosome2)]

fits_population_with_large_fitness = [(1000, chromosome1), (2, chromosome2), (3, chromosome3)]


def sorted_population():
    return sorted(fits_population, key=utils.sort_by_fitness, reverse=True)


class SelectionTest(unittest.TestCase):

    def test_elite_selection(self):
        selection_algorithm = EliteSelection()

        parents = selection_algorithm.selection(fits_population, 5)
        expected = [(5, chromosome5), (5, chromosome5), (4, chromosome4), (4, chromosome4), (3, chromosome3)]
        self.assertEqual(parents, expected)

    def test_roulette_selection(self):
        selection_algorithm = RouletteSelection()
        parents = selection_algorithm.selection(fits_population_with_large_fitness, 10)
        self.assertIn((1000, chromosome1), parents)
        parents = selection_algorithm.selection(fits_population, 5)
        self.assertEqual(len(parents), 5)
        parents = selection_algorithm.selection(fits_population, 10)
        self.assertEqual(len(parents), 10)

    def test_universal_selection(self):
        selection_algorithm = UniversalSelection()
        parents = selection_algorithm.selection(fits_population_with_large_fitness, 10)
        self.assertIn((1000, chromosome1), parents)
        parents = selection_algorithm.selection(fits_population, 5)
        self.assertEqual(len(parents), 5)
        parents = selection_algorithm.selection(fits_population, 10)
        self.assertEqual(len(parents), 10)

    def test_ranking_selection(self):
        rank_chromosomes = []
        fits_large_population = []
        result_selection = {}
        for i in range(0, 100):
            chromo = Chromosome(genes=[i, i, i])
            rank_chromosomes.append(chromo)
            result_selection[chromo] = 0
            fits_large_population.append((i, rank_chromosomes[i]))
        expected_chromosome = rank_chromosomes[99]
        random.shuffle(rank_chromosomes)
        selection_algorithm = RankingSelection()
        for i in range(0, 100):
            parents = selection_algorithm.selection(fits_large_population, 5)
            for x in range(0, len(parents)):
                result_selection[parents[x][1]] += 1

        max_chromosome_selected = None
        max_chromosome_selected_num = 0
        for x in range(0, 100):
            if max_chromosome_selected_num < result_selection[rank_chromosomes[x]]:
                max_chromosome_selected = rank_chromosomes[x]
                max_chromosome_selected_num = result_selection[rank_chromosomes[x]]

        self.assertEqual(expected_chromosome, max_chromosome_selected)

        parents = selection_algorithm.selection(fits_population, 5)
        self.assertEqual(len(parents), 5)
        parents = selection_algorithm.selection(fits_population, 10)
        self.assertEqual(len(parents), 10)

    def test_tournament_selection(self):
        result_selection = {chromosome1: 0,
                            chromosome2: 0,
                            chromosome3: 0
                            }
        selection_algorithm = TournamentSelection(is_tournament_probabilistic=False)
        for i in range(0, 100):
            parents = selection_algorithm.selection(fits_population_with_large_fitness, 3)
            for x in range(0, len(parents)):
                result_selection[parents[x][1]] += 1

        max_chromosome_selected = None

        if result_selection[chromosome1] > result_selection[chromosome2]:
            if result_selection[chromosome1] > result_selection[chromosome3]:
                max_chromosome_selected = chromosome1
            else:
                max_chromosome_selected = chromosome3
        else:
            if result_selection[chromosome2] > result_selection[chromosome3]:
                max_chromosome_selected = chromosome2
            else:
                max_chromosome_selected = chromosome3

        self.assertEqual(chromosome1, max_chromosome_selected)


