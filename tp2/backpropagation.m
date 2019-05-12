%Algoritmo de Entrenamiento de BACKPROPAGATION para Redes Neuronales
function result = backpropagation(X, S, max_epochs, batch_size, learn_percentage, rate, dmse, error_color, rate_color, structure, optimizer, gamma)

  mse = Inf;                  %Asumiendo Pesos Iniciales Malos
  epoch = 0; 

  %Numero de Patrones P y Entradas N
  [P, N] = size(X);
  
  P = floor(P * learn_percentage);

  X_train = X(1:P, :);
  S_train = S(1:P, :);

  X_mean = mean(X_train);
  X_std = std(X_train);
  S_mean = mean(S_train);
  S_std = std(S_train);

  %X_train = (X_train - X_mean);% ./ X_std;
  %X_train = X_train ./ X_std
  %S_train = (S_train - S_mean) ./ S_std;

  [aux, depth] = size(structure);                  %Profundidad de la red (nro capas)
  
  %Inicializar Matriz de Pesos para cada capa en el rango [-1,1]
  W = cell(depth-1, 1);
  B = cell(depth-1, 1);
  
  for i= 1 : depth-1;
    W{i} = normrnd(0, 1, [structure(i+1), structure(i)]) / sqrt(structure(i));
    B{i} = zeros(structure(i+1), 1);
  end

  %Inicializar Matrices de los delta-pesos de ajuste
  dW = cell(depth-1, 1);
  dB = cell(depth-1, 1);

  %Inicializar matrices auiliares para los optimizadores
  W_update = cell(depth-1, 1);
  B_update = cell(depth-1, 1);
  W_rate = cell(depth-1, 1);
  B_rate = cell(depth-1, 1);
  dW_aux = cell(depth-1, 1);
  dB_aux = cell(depth-1, 1);
  for m = 1:depth-1
    dW_aux{m} = zeros(size(W{m}));
    dB_aux{m} = zeros(size(B{m}));
  end

  %Inicializar los campos locales inducidos 'V'
  V = cell(depth, 1);

  %Inicializar las salidas 'y' de cada capa
  y = cell(depth-1, 1);             %Pre-alocacion de las salidas locales
    
  %% 2. Calculo Forward y Backward para cada epoch
  while (mse > dmse) && (epoch <= max_epochs)
      e = zeros(batch_size, 1);
      count = 0;
      p = 1 + batch_size * epoch;
      
      if p > P - batch_size
        p = 1;
      end

      for m = 1:depth-1
        dW{m} = zeros(size(W{m}));
        dB{m} = zeros(size(B{m}));
      end
      
      for p = p : batch_size + p
        
        V{1} = X_train(p, :);
        V{1} = V{1}.';
        count++;
        
        for i = 1 : depth - 1
            y{i} = W{i} * V{i} + B{i};
            V{i+1} = tanh(y{i}); %Calculo de la salida con tangente hiperbolica
        end
        
        %Calculo de la señal de error
        e(count, :) = (S_train(p, :) - V{end}).^2;
        
        %Calculo Backward capa-por-capa para cada patron p             
        delta = derivateTanH(V{end}) .* (S_train(p, 1) - V{end});
        
        %Calculo de derivadas
        for i = depth-1 : -1 : 1
          dW{i} = dW{i} + delta * V{i}.';
          dB{i} = dB{i} + delta;
          delta = derivateTanH(V{i}) .* (W{i}.' * delta);
        end
        
      end

      %Ajuste de pesos
      switch optimizer
        case 'momentum'
            for i = depth-1 : -1 : 1
                W_update{i} = gamma * dW_aux{i} + rate * dW{i};
                B_update{i} = gamma * dB_aux{i} + rate * dB{i};
                dW_aux{i} = W_update{i};
                dB_aux{i} = B_update{i};
            end
        case 'adagrad'
            for i = depth-1 : -1 : 1
                dW_aux{i} = dW_aux{i} + dW{i} .* dW{i};
                dB_aux{i} = dB_aux{i} + dB{i} .* dB{i};

                W_update{i} = rate * dW{i} ./ sqrt(dW_aux{i} + 1e-8);
                B_update{i} = rate * dB{i} ./ sqrt(dB_aux{i} + 1e-8);
            end
        otherwise
            for i = depth-1 : -1 : 1
                W_update{i} = rate * dW{i};
                B_update{i} = rate * dB{i};
            end
      endswitch

      rate_sum = 0;
      rate_count = 0;
      for i = depth-1 : -1 : 1
          W{i} = W{i} + W_update{i};
          B{i} = B{i} + B_update{i};

          rate_mtx = W_update{i} ./ (dW{i} + 1e-16);
          rate_sum = rate_sum + abs(sum(rate_mtx(:)));
          rate_count = rate_count + length(rate_mtx(:));
      end
      avg_rate = rate_sum / rate_count;
      
      %Calculo del mean square error
      mse = sum(e) / batch_size;
      epoch = epoch + 1;
      if mod(epoch, 10) == 0
        plot_error(epoch, mse, error_color);
        plot_rate(epoch, avg_rate, rate_color);
      end
  endwhile

  result.weights = W;
  result.biases = B;
  result.epochs = epoch - 1;
  result.error = mse;
endfunction

function plot_error(epoch, error, error_color)
  hold on
  figure(1);
  semilogy(epoch, error, 'Color', error_color);
  title('Error', 'fontsize', 20);
  xlabel('Epochs');
  ylabel('Error');
  set(gca,'FontSize',20)
  drawnow
  hold off
endfunction

function plot_rate(epoch, rate, rate_color)
  hold on
  figure(2);
  semilogy(epoch, rate, 'ro', 'Color', rate_color);
  title('Learning rate', 'fontsize', 20);
  xlabel('Epochs');
  ylabel('Rate');
  set(gca,'FontSize',20)
  drawnow
  hold off
endfunction

function y = derivateTanH(x)
  y = 1 - x.^2;
endfunction
