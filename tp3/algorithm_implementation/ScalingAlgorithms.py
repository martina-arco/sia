import math


class ScalingAlgorithm(object):
    def update_parameters(self):
        pass

    def scale(self, fits_population):
        return fits_population


class BoltzmannSelection(ScalingAlgorithm):
    def __init__(self, initial_temp, step):
        self.temp = initial_temp
        self.step = step

    def update_parameters(self):
        if self.temp - self.step >= 1.0:
            self.temp -= self.step

    def scale(self, fits_population):
        new_fitness = [math.exp(t[0] / self.temp) for t in fits_population]
        avg_new_fitness = sum(new_fitness) / len(new_fitness)
        scaled_fitness = [f / avg_new_fitness for f in new_fitness]
        scaled_population = [(scaled_fitness[i], fits_population[i][1]) for i in range(len(fits_population))]
        return scaled_population


class NoScaling(ScalingAlgorithm):
    pass


class RelativeScaling(ScalingAlgorithm):
    def scale(self, fits_population):
        avg_fitness = sum(fit for fit, ch in fits_population) / len(fits_population)
        scaled_population = [(f / avg_fitness, ch) for f, ch in fits_population]
        return scaled_population
