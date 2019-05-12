%Algoritmo de Entrenamiento de BACKPROPAGATION para Redes Neuronales
function result = backpropagation(X, S, max_epochs, batch_size, learn_percentage, rate, dmse, error_color, rate_color)

  mse = Inf;                  %Asumiendo Pesos Iniciales Malos
  epoch = 0;                  %Rango de valores iniciales [-1 1]

  %Numero de Patrones P y Entradas N
  [P, N] = size(X);
  
  P = floor(P * learn_percentage);
      
  depth = 3;                  %Profundidad de la red (nro capas)
  
  %Inicializar Matriz de Pesos para cada capa en el rango [-1,1]
  W = cell(depth-1, 1);
  W{1} = normrnd(0, 1, [50, 2]) / sqrt(2);
  W{2} = normrnd(0, 1, [1, 50]) / sqrt(50);

  B = cell(depth-1, 1);
  B{1} = zeros(50, 1);
  B{2} = zeros(1, 1);

  %Inicializar Matrices de los delta-pesos de ajuste
  dW = cell(depth-1, 1);               %Pre-alocacion de los delta pesos
  dB = cell(depth-1, 1);

  %Inicializar los campos locales inducidos 'v'
  V = cell(depth, 1);
  V{2} = ones(3,1);
  V{3} = ones(1,1); 

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
        
        V{1} = X(p, :);
        V{1} = V{1}.';
        count++;
        
        for i = 1 : depth - 1
            y{i} = W{i} * V{i} + B{i};
            V{i+1} = tanh(y{i}); %Calculo de la salida con tangente hiperbolica
        end
        
        %Calculo de la señal de error
        e(count, :) = (S(p, :) - V{end}).^2;
        
        %Calculo Backward capa-por-capa para cada patron p             
        delta = derivateTanH(V{end}) .* (S(p, 1) - V{end});
        
        %Calculo de derivadas
        for i = depth-1 : -1 : 1
          dW{i} = dW{i} + rate * delta * V{i}.';
          dB{i} = dB{i} + rate * delta;
          delta = derivateTanH(V{i}) .* (W{i}.' * delta);
        end
        
      end

      %Ajuste de pesos
      for i = depth-1 : -1 : 1
        W{i} = W{i} + dW{i};
        B{i} = B{i} + dB{i};
      end
      
      %Calculo del mean square error
      mse = sum(e) / batch_size;
      epoch = epoch + 1;
      plot_error(epoch, mse, error_color);
      plot_rate(epoch, rate, rate_color);
  endwhile

  result.weights = W;
  result.biases = B;
  result.epochs = epoch - 1;
  result.error = mse;
endfunction

function plot_error(epoch, error, error_color)
  hold on
  figure(1);
  semilogy(epoch, error, 'ro', 'Color', error_color)
  title('Error', 'fontsize', 20);
  xlabel('Epochs', 'fontsize', 11);
  ylabel('Error', 'fontsize', 11);
  hold off
endfunction

function plot_rate(epoch, rate, rate_color)
  hold on
  figure(2);
  plot(epoch, rate, 'ro', 'Color', rate_color)
  title('Learning rate', 'fontsize', 20);
  xlabel('Epochs', 'fontsize', 11);
  ylabel('Rate', 'fontsize', 11);
  hold off
endfunction

function y = derivateTanH(x)
  y = 1 - x.^2;
endfunction
