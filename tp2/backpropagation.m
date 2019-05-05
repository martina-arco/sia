%Algoritmo de Entrenamiento de BACKPROPAGATION para Redes Neuronalesfunction learn = backpropagation(XE, S, learnNumber, rate, alfa, dmse)  mse = Inf;                  %Asumiendo Pesos Iniciales Malos  epoch = 1;                  %Rango de valores iniciales [-1 1]  [N, P] = size(XE);           %Numero de Patrones P y Entradas N    %X = ones(learnNumber, P) * -1;  %X(2:learnNumber+1, :) = XE(1:learnNumber, :)  X(1:learnNumber, :) = XE(1:learnNumber, :)    [N, P] = size(X);        %[Q, P] = size(D);           %Numero de Patrones P y Salidas Q   depth = 3;                  %Profundidad de la red (nro capas)    %Inicializar Matriz de Pesos para cada capa en el rango [-1,1]  W = cell(depth - 1, 1);  W{1} = 2.*rand(3, 2) - 1;  W{2} = 2.*rand(1, 3) - 1;  %Inicializar Matrices de los delta-pesos de ajuste  dW = cell(1,depth-1);               %Pre-alocacion de los delta pesos  for m = 1:depth-1      dW{m} = zeros(size(W{m}));  end  %Inicializar los campos locales inducidos 'v'  V = cell(depth, 1);  V{2} = ones(3,learnNumber);  V{3} = ones(1,learnNumber);   %Inicializar las salidas 'y' de cada capa  y = cell(1, depth-1);             %Pre-alocacion de las salidas locales    S = S.';    %% 2. Calculo Forward y Backward para cada epoch  while (mse > dmse) && (epoch <= 10)      %e = zeros(Q, P);      %err = zeros(1, P);              V{1} = X;        V{1} = V{1}.';                for i = 1 : depth - 1            y{i} = W{i} * V{i};                        if i < depth - 1                V{i+1} = tanh(y{i}); %Calculo de la salida con tangente hiperbolica            else                V{i+1} = tanh(y{i});          %Calculo de la salida            end                     end        V                 %Calculo de la señal de error        %e(:, p) = D(:, p) - v{end};                %Calculo de la energia del error        %if size(D, 1) == 1         %   err(1, p) = 0.5 * (e(:, p).^2);        %elseif size(D, 1) > 1         %   err(1, p) = 0.5 * sum(e(:, p).^2);        %end                %Calculo Backward capa-por-capa para cada patron p                %delta = e(:, p).*(tanh('dn', y{end}));             delta = derivateTanH(V{end}) .* (S(:, 1:learnNumber) - V{end});                %Ajuste de pesos        for i = depth-1 : -1 : 1                             %dW{i} = rate * delta * v{i}' + alfa.*dW{i};            V{i-1}            delta            W{i}            dW{i} = derivateTanH(V{i-1}) * delta * W{i}            W{i} = W{i} + dW{i} * rate * V{i-1};                        %if i > 1             %   delta = tanh('dn', y{i-1}).* (delta' * W{i}(:, 1 : end - 1))';            %end        end                      %Calculo del mean square error      mse = (1 / P) * sum(err);      epoch = epoch + 1;      hold on      figure(2)      semilogx(epoch, mse, 'ro')      hold off  end  learn.pesos = W;  learn.epocas = epoch;  learn.estructura = L;  learn.error = mse;endfunctionfunction y = derivateTanH(x)  y = 1 - x.^2;endfunction