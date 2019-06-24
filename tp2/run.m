max_epochs = 4000
max_error = 0.02
type = 'batch'
learn_percentage = 0.9
learning_rate = 0.0003
optimizer = 'eta'
gamma = 0.9
a = 0.000001
b = 0.1
structure = [2, 50, 1]
act_func = 'tanh'
error_color = 'r';
rate_color = error_color;
epsilon = 0.01;
eta_epsilon = 0.001

result = backpropagation(patterns, S, max_epochs, type, learn_percentage, 
learning_rate, max_error, error_color, rate_color, act_func, structure, optimizer, gamma, epsilon, a, b, eta_epsilon)