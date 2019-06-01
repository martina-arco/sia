
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


# todavia no se muy bien que hacer
class OptimalStopCondition(StopCondition):
    def check_stop(self, fits_population, fitness_min):
        fits = [f for f, ch in fits_population]
        ave = sum(fits) / len(fits)
        return ave < fitness_min

        # if self.counter % 10 == 0:
        #     best_match = list(sorted(fits_populations))[-1][1]
        #     fits = [f for f, ch in fits_populations]
        #     best = max(fits)
        #     worst = min(fits)
        #     ave = sum(fits) / len(fits)
        #     print(
        #         "[G %3d] score=(%4d, %4d, %4d): %r" %
        #         (self.counter, best, ave, worst,
        #          self.chromo2text(best_match)))
        #     pass
        # return self.counter >= self.limit
