class GeneticAlgorithm(object):
    def __init__(self, genetics):
        self.genetics = genetics

    def run(self):
        population = self.genetics.initial()
        finished = False

        while not finished:
            population_fitness = [(self.genetics.fitness(ch), ch) for ch in population]
            if self.genetics.generation % self.genetics.plot_freq == 0:
                self.genetics.plot(population_fitness)
            finished = self.genetics.check_stop(population_fitness)
            if not finished:
                population = self.next_generation(population_fitness)

        return population

    def next_generation(self, population_fitness):
        population_scaled = self.genetics.fitness_scaling(population_fitness)
        parent_pool = self.genetics.selection(population_scaled)

        offspring = []
        for i in range(0, self.genetics.offspring_size(), 2):
            parents = self.genetics.parent_selection(parent_pool)
            children = self.genetics.crossover(parents[0][1], parents[1][1])
            for ch in children:
                offspring.append(self.genetics.mutation(ch))

        offspring_fitness = [(self.genetics.fitness(ch), ch) for ch in offspring]
        offspring_scaled = self.genetics.fitness_scaling(offspring_fitness)
        next_generation = self.genetics.replacement(population_scaled, offspring_scaled)

        self.genetics.update_parameters()
        return next_generation
