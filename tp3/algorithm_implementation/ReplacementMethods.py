class ReplacementMethod(object):
    def offspring_size(self):
        pass

    def replacement(self, parents, children):
        pass


class ReplacementOne(ReplacementMethod):
    def __init__(self, pop_size):
        self.pop_size = pop_size

    def offspring_size(self):
        return self.pop_size

    def replacement(self, parents, children):
        return [ch for fit, ch in children]


class ReplacementTwo(ReplacementMethod):
    def replacement(self, parents, children):
        new_population = []

        chromosomes = selection(self, fits_population, k)
        for i in range(0, len(chromosomes), 2):
            children = crossover(self, chromosomes[i], chromosomes[i+1])
            mutated_child = mutate(self, children[0], items_size, prob_mutation)
            new_population.append(mutated_child)

        for p in fits_population:
            if p not in chromosomes:
                new_population.append(p)

        return new_population


class ReplacementThree(ReplacementMethod):
    def replacement(self, parents, children):
        new_population = []

        chromosomes = selection(self, fits_population, k)
        for i in range(0, len(chromosomes), 2):
            children = crossover(self, chromosomes[i], chromosomes[i + 1])
            mutated_child = mutate(self, children[0], items_size, prob_mutation)
            new_population.append(mutated_child)

        for p in fits_population:
            if p not in chromosomes:
                new_population.append(p)

        big_population = [fits_population, chromosomes]

        new_chromosomes = selection(self, big_population, k)
        return new_chromosomes