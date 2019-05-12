max_epochs = 1500
max_error = 0.0000001
batch_size = 4
learn_percentage = 1
learning_rate = 0.01
optimizer = 'adagrad'
gamma = 0.9
structure = [2, 50, 1]
error_color = 'g';
rate_color = error_color;

result = backpropagation(patterns, S, max_epochs, batch_size, learn_percentage, learning_rate, max_error, error_color, rate_color, structure, optimizer, gamma)
