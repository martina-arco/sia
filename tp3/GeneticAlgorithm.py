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
        population_scaled = self.genetics.fitness_scaling(population_fitness)
        parents = self.genetics.selection(population_scaled)

        offspring = []
        for i in range(0, self.genetics.offspring_size(), 2):
            father, mother = self.genetics.parent_selection(parents)
            children = self.genetics.crossover(father, mother)
            for ch in children:
                offspring.append(self.genetics.mutation(ch))

        offspring_fitness = [(self.genetics.fitness(ch), ch) for ch in offspring]
        offspring_scaled = self.genetics.fitness_scaling(offspring_fitness)
        next_generation = self.genetics.replacement(population_scaled, offspring_scaled)

        self.genetics.update_parameters()
        return next_generation
