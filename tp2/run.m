max_epochs = 4000
max_error = 0.02
type = 'incremental'
learn_percentage = 0.9
learning_rate = 0.03
optimizer = 'eta'
gamma = 0.9
a = 1.2
b = 0.9
structure = [2, 50, 1]
act_func = 'tanh'
error_color = 'r';
rate_color = error_color;
epsilon = 0.01;

result = backpropagation(patterns, S, max_epochs, type, learn_percentage, 
learning_rate, max_error, error_color, rate_color, act_func, structure, optimizer, gamma, epsilon, a, b)