class GeneticAlgorithm(object):
    def __init__(self, genetics):
        self.genetics = genetics

    def run(self):
        population = self.genetics.initial()
        finished = False

        while not finished:
            population_fitness = [(self.genetics.fitness(ch), ch) for ch in population]
            finished = self.genetics.check_stop(population_fitness)
            if not finished:
                population = self.next_generation(population_fitness)

        return population

    def next_generation(self, population_fitness):
        parents = self.genetics.selection(population_fitness)
        next_generation = []
        i = 0

        while i < len(parents)-2:
            father = parents[i]
            mother = parents[i+1]
            children = self.genetics.crossover(father, mother)
            for ch in children:
                next_generation.append(self.genetics.mutation(ch))
            i += 2

        # falta el reemplazo
        return next_generation
