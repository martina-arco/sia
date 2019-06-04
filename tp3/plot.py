import pickle
import matplotlib.pyplot as plt

dir = 'data/'

for id in ['1', '2', '3']:
    max_fitness = pickle.load(open(dir + id + '_max_fitness.p', "rb"))
    avg_fitness = pickle.load(open(dir + id + '_avg_fitness.p', "rb"))
    chromosome_diversity = pickle.load(open(dir + id + '_chromosome_diversity.p', "rb"))

    plt.figure(1)
    plt.plot(range(len(max_fitness)), max_fitness)
    plt.figure(2)
    plt.plot(range(len(avg_fitness)), avg_fitness)
    plt.figure(3)
    plt.plot(range(len(chromosome_diversity)), chromosome_diversity)

plt.show()
