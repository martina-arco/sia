import random


class GeneticAlgorithm(object):
    def __init__(self, genetics):
        self.genetics = genetics

    def run(self):
        population = self.genetics.initial
        finished = False

        while not finished:
            population_fitness = [(self.genetics.fitness(ch), ch) for ch in population]
            finished = self.genetics.check_stop(population_fitness)
            if not finished:
                population = self.next_generation(population_fitness)

        return population

    def next_generation(self, population_fitness):
        parents_generator = self.genetics.selection(population_fitness)
        next_generation = []

        for parents in parents_generator:
            # cross = random.random() < self.genetics.probability_crossover()
            # children = self.genetics.crossover(parents) if cross else parents
            children = self.genetics.crossover(parents)
            for ch in children:
                next_generation.append(self.genetics.mutation(ch))

        # falta el reemplazo
        return next_generation
