
class StopCondition(object):
    def check_stop(self, arg1, arg2):
        pass


class MaxGenerationStopCondition(StopCondition):
    def check_stop(self, generation, max_generation):
        return generation > max_generation


class StructureStopCondition(StopCondition):
    def check_stop(self, sorted_population, previous_generation):
        for i in range(1, len(previous_generation)):
            if sorted_population[i][1] != previous_generation[i][1]:
                return False
        return True


class ContentStopCondition(StopCondition):
    def check_stop(self, best_fits, arg2=None):
        for i in range(1, len(best_fits)):
            if best_fits[i] != best_fits[i-1]:
                return False
        return True


class OptimalStopCondition(StopCondition):
    def check_stop(self, best_fit, fitness_max):
        return best_fit > fitness_max
