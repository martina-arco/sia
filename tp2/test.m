function output = test(X, X_mean, X_std, S, W, B, structure, test_percentage)[P, N] = size(X);amount_tested = floor(P * test_percentage);[aux, depth] = size(structure);              %Numero de Capas Ocultas "Depth"%Inicializar los campos locales inducidos 'v'V = cell(depth, 1);%Inicializar las salidas 'y' de cada capa y = cell(depth+1,1); output.approximate = zeros(amount_tested,1);output.evaluation = X(P-amount_tested:P, :);count = 1;e = zeros(amount_tested, 1);X_train = X(P-amount_tested:P, :);X_train = (X_train - X_mean) ./ X_std;for p = P - amount_tested : P    V{1} = X_train(count, :);  V{1} = V{1}.';    for i = 1 : depth-1      y{i} = W{i} * V{i} + B{i};      V{i+1} = tanh(y{i});  end    e(count, :) = (S(p, :) - V{end}).^2;    output.approximate(count) = V{end};   count++;  endoutput.mse = sum(e) / amount_tested;