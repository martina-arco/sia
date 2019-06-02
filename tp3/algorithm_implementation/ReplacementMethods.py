class ReplacementMethod(object):
    def replacement(self, fits_population, k, items_size, prob_mutation):
        return fits_population


class ReplacementOne(ReplacementMethod):
    def replacement(self, fits_population, k, items_size, prob_mutation):
        new_population = []

        for i in range(0, len(fits_population)):
            chromosomes = selection(self, fits_population, 2)
            children = crossover(self, chromosomes[0], chromosomes[1])
            mutated_child = mutate(self, children[0], items_size, prob_mutation)
            new_population.append(mutated_child)

        return new_population


class ReplacementTwo(ReplacementMethod):
    def replacement(self, fits_population, k, items_size, prob_mutation):
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
    def replacement(self, fits_population, k, items_size, prob_mutation):
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