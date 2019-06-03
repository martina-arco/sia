import math


class ReplacementMethod(object):
    def offspring_size(self):
        pass

    def replacement(self, population, offspring):
        pass


class ReplacementOne(ReplacementMethod):
    def __init__(self, pop_size):
        self.pop_size = pop_size

    def offspring_size(self):
        return self.pop_size

    def replacement(self, population, offspring):
        return [ch for fit, ch in offspring]


class ReplacementTwo(ReplacementMethod):
    def __init__(self, pop_size, selection_algorithm_1, percentage_1, selection_algorithm_2):
        self.pop_size = pop_size
        self.selection_algorithm_1 = selection_algorithm_1
        self.percentage_1 = percentage_1
        self.selection_algorithm_2 = selection_algorithm_2

    def offspring_size(self):
        return self.pop_size

    def replacement(self, population, offspring):
        count_to_select = len(population) - len(offspring)
        count_to_select_1 = math.floor(count_to_select*self.percentage_1)
        count_to_select_2 = count_to_select - count_to_select_1
        selected_1 = self.selection_algorithm_1.selection(population, count_to_select_1)
        chromosomes_selected_1 = [ch for fit, ch in selected_1]
        selected_2 = self.selection_algorithm_2.selection(population, count_to_select_2)
        chromosomes_selected_2 = [ch for fit, ch in selected_2]
        offspring_chromosomes = [ch for fit, ch in offspring]

        new_gen = []
        for c in chromosomes_selected_1:
            new_gen.append(c)
        for c in chromosomes_selected_2:
            new_gen.append(c)
        for c in offspring_chromosomes:
            new_gen.append(c)

        return new_gen


class ReplacementThree(ReplacementMethod):
    def __init__(self, pop_size, selection_algorithm_1, percentage_1, selection_algorithm_2):
        self.pop_size = pop_size
        self.selection_algorithm_1 = selection_algorithm_1
        self.percentage_1 = percentage_1
        self.selection_algorithm_2 = selection_algorithm_2

    def offspring_size(self):
        return self.pop_size

    def replacement(self, population, offspring):
        count_to_select = len(population) - len(offspring)
        count_to_select_1 = math.floor(count_to_select*self.percentage_1)
        count_to_select_2 = count_to_select - count_to_select_1
        selected_1 = self.selection_algorithm_1.selection(population, count_to_select_1)
        chromosomes_selected_1 = [ch for fit, ch in selected_1]
        selected_2 = self.selection_algorithm_2.selection(population, count_to_select_2)
        chromosomes_selected_2 = [ch for fit, ch in selected_2]

        new_gen = []
        for c in chromosomes_selected_1:
            new_gen.append(c)
        for c in chromosomes_selected_2:
            new_gen.append(c)

        new_count_to_select = len(offspring)
        new_count_to_select_1 = math.floor(new_count_to_select*self.percentage_1)
        new_count_to_select_2 = new_count_to_select - new_count_to_select_1
        new_pop = []
        for c in population:
            new_pop.append(c)
        for c in offspring:
            new_pop.append(c)
        new_selected_1 = self.selection_algorithm_1.selection(new_pop, new_count_to_select_1)
        new_chromosomes_selected_1 = [ch for fit, ch in new_selected_1]
        new_selected_2 = self.selection_algorithm_2.selection(new_pop, new_count_to_select_2)
        new_chromosomes_selected_2 = [ch for fit, ch in new_selected_2]

        for c in new_chromosomes_selected_1:
            new_gen.append(c)
        for c in new_chromosomes_selected_2:
            new_gen.append(c)

        return new_gen
