import pickle
import matplotlib.pyplot as plt

dir = 'data/'
window = 50

for id in ['one_point', 'two_points', 'uniform', 'anular']:
    max_fitness = pickle.load(open(dir + id + '_max_fitness.p', "rb"))
    avg_fitness = pickle.load(open(dir + id + '_avg_fitness.p', "rb"))
    chromosome_diversity = pickle.load(open(dir + id + '_chromosome_diversity.p', "rb"))

    plt.figure(1)
    plt.plot(range(len(max_fitness)), max_fitness)
    plt.figure(2)
    plt.plot(range(len(avg_fitness)), avg_fitness[:window] + [sum(avg_fitness[i:i+window]) / window for i in range(len(avg_fitness) - window)])
    plt.figure(3)
    plt.plot(range(len(chromosome_diversity)), chromosome_diversity[:window] + [sum(chromosome_diversity[i:i+window]) / window for i in range(len(chromosome_diversity) - window)])

plt.show()
