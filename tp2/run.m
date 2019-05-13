max_epochs = 2000
max_error = 0.0000001
batch_size = 4
learn_percentage = 1
learning_rate = 0.001
optimizer = 'adam'
gamma = 0.9
gamma2 = 0.999
structure = [2, 50, 1]
error_color = 'b';
rate_color = error_color;

result = backpropagation(patterns, S, max_epochs, batch_size, learn_percentage, learning_rate, max_error, error_color, rate_color, structure, optimizer, gamma, gamma2)
