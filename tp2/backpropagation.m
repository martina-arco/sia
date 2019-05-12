%Algoritmo de Entrenamiento de BACKPROPAGATION para Redes Neuronalesfunction result = backpropagation(X, S, epochNumber, batchSize, learnPercentage, rate, dmse)  mse = Inf;                  %Asumiendo Pesos Iniciales Malos  epoch = 0;                  %Rango de valores iniciales [-1 1]  %Numero de Patrones P y Entradas N  [P, N] = size(X);    P = floor(P * learnPercentage);        depth = 3;                  %Profundidad de la red (nro capas)    %Inicializar Matriz de Pesos para cada capa en el rango [-1,1]  W = cell(depth-1, 1);  W{1} = 	normrnd(0, 1, [100, 2]) / sqrt(2);  W{2} = 	normrnd(0, 1, [1, 100]) / sqrt(100);  %Inicializar Matrices de los delta-pesos de ajuste  dW = cell(depth-1, 1);               %Pre-alocacion de los delta pesos  for m = 1:depth-1      dW{m} = zeros(size(W{m}));  end  %Inicializar los campos locales inducidos 'v'  V = cell(depth, 1);  V{2} = ones(3,1);  V{3} = ones(1,1);   %Inicializar las salidas 'y' de cada capa  y = cell(depth-1);             %Pre-alocacion de las salidas locales      %% 2. Calculo Forward y Backward para cada epoch  while (mse > dmse) && (epoch <= epochNumber)      e = zeros(batchSize, 1);      count = 0;      p = 1 + batchSize * epoch;            if p > P - batchSize        p = 1;      end            for p = p : batchSize + p                V{1} = X(p, :);        V{1} = V{1}.';        count++;                for i = 1 : depth - 1            y{i} = W{i} * V{i};            V{i+1} = tanh(y{i}); %Calculo de la salida con tangente hiperbolica        end                %Calculo de la señal de error        e(count, :) = (S(p, :) - V{end}).^2;                %Calculo Backward capa-por-capa para cada patron p                     delta = derivateTanH(V{end}) .* (S(p, 1) - V{end});                %Ajuste de pesos        for i = depth-1 : -1 : 1          dW{i} = rate * delta * V{i}.';          W{i} = W{i} + dW{i};          delta = derivateTanH(V{i}) .* (W{i}.' * delta);        end              end            %Calculo del mean square error      mse = sum(e) / batchSize;      epoch = epoch + 1;      hold on      semilogy(epoch, mse, 'ro')      hold off  endwhile  result.weights = W;  result.epochs = epoch - 1;  result.error = mse;endfunctionfunction y = derivateTanH(x)  y = 1 - x.^2;endfunction