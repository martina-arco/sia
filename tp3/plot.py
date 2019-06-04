import pickle
import matplotlib.pyplot as plt

dir = 'data/'
file_prefix = ''
window = 50
# files = ['one_point', 'two_points', 'uniform', 'anular']
# labels = ['One Point', 'Two Points', 'Uniform', 'Anular']
# file_prefix = 'Crossover'
# files = ['uniform_gen', 'uniform_multi_gen', 'non_uniform_gen', 'non_uniform_multi_gen']
# labels = ['U Gen', 'U MultiGen', 'Non-U Gen', 'Non-U MultiGen']
# file_prefix = 'Mutation'
# files = ['1', '2', '3']
# labels = ['Method 1', 'Method 2', 'Method 3']
# file_prefix = 'Replacement'
# files = ['none', 'boltzmann']
# labels = ['No Scaling', 'Boltzmann']
# file_prefix = 'Scaling'
# file_prefix = 'sel1_full_'
# files = ['elite', 'roulette', 'universal', 'tournament', 'probabilistic_tournament', 'ranking']
# labels = ['Elite', 'Roulette', 'Universal', 'Tournament', 'P-Tournament', 'Ranking']
# file_prefix = 'Selection1'
# file_prefix = 'rpm2_sel3_full_'
# files = ['elite', 'roulette', 'universal', 'tournament', 'probabilistic_tournament', 'ranking']
# labels = ['Elite', 'Roulette', 'Universal', 'Tournament', 'P-Tournament', 'Ranking']
# file_prefix = 'Selection3'
file_prefix = 'sel5_'
files = ['elite', 'roulette', 'universal', 'tournament', 'probabilistic_tournament', 'ranking']
labels = ['Elite', 'Roulette', 'Universal', 'Tournament', 'P-Tournament', 'Ranking']
img_prefix = 'Selection5'


for i in range(len(files)):
    max_fitness = pickle.load(open(dir + file_prefix + files[i] + '_max_fitness.p', "rb"))
    avg_fitness = pickle.load(open(dir + file_prefix + files[i] + '_avg_fitness.p', "rb"))
    chromosome_diversity = pickle.load(open(dir + file_prefix + files[i] + '_chromosome_diversity.p', "rb"))

    plt.figure(1)
    plt.plot(range(len(max_fitness)), max_fitness, label=labels[i])
    plt.figure(2)
    plt.plot(range(len(avg_fitness)), avg_fitness[:window] + [sum(avg_fitness[i:i+window]) / window for i in range(len(avg_fitness) - window)], label=labels[i])
    plt.figure(3)
    plt.plot(range(len(chromosome_diversity)), chromosome_diversity[:window] + [sum(chromosome_diversity[i:i+window]) / window for i in range(len(chromosome_diversity) - window)], label=labels[i])

plt.figure(1).canvas.set_window_title(img_prefix + '_Max_Fitness')
plt.xlabel('Generation')
plt.ylabel('Max Fitness')
plt.legend()
plt.figure(2).canvas.set_window_title(img_prefix + '_Average_Fitness')
plt.xlabel('Generation')
plt.ylabel('Average Fitness')
plt.legend()
plt.figure(3).canvas.set_window_title(img_prefix + '_Chromosome_Diversity')
plt.xlabel('Generation')
plt.ylabel('Amount of different chromosomes')
plt.legend()
plt.show()
