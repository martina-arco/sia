%Algoritmo de Entrenamiento de BACKPROPAGATION para Redes Neuronales
function result = backpropagation(X, S, max_epochs, type, learn_percentage, rate, dmse, error_color, rate_color, 
  act_func, structure, optimizer, gamma, epsilon, a, b, eta_epsilon)

  mse = Inf;                  %Asumiendo Pesos Iniciales Malos
  epoch = 0; 

  %Numero de Patrones P y Entradas N
  [P, N] = size(X);
  
  P = floor(P * learn_percentage);
  batch_size = P - 1;
  
  prev_error1 = 0;
  prev_error2 = 0;
  prev_error3 = 0;
  prev_error4 = 0;
  prev_error5 = 0;
  
  if(strcmp(type, 'incremental') == 1)
    batch_size = 1
  endif

  X_train = X(1:P, :);
  S_train = S(1:P, :);

  X_mean = mean(X_train);
  X_std = std(X_train);
  S_mean = mean(S_train);
  S_std = std(S_train);

  X_train = (X_train - X_mean) ./ X_std;
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
  dW_aux = cell(depth-1, 1);
  dB_aux = cell(depth-1, 1);
  dW_aux2 = cell(depth-1, 1);
  dB_aux2 = cell(depth-1, 1);
  for m = 1:depth-1
    dW_aux{m} = zeros(size(W{m}));
    dB_aux{m} = zeros(size(B{m}));
    dW_aux2{m} = zeros(size(W{m}));
    dB_aux2{m} = zeros(size(B{m}));
  end

  %Inicializar los campos locales inducidos 'V'
  V = cell(depth, 1);

  %Inicializar las salidas 'y' de cada capa
  y = cell(depth-1, 1);             %Pre-alocacion de las salidas locales
  
  error_count = 0;
  sum_error = 0;
  hits = 0;
    
  %% 2. Calculo Forward y Backward para cada epoch
  batch_start = 1;
  finished = false;
  while (!finished) && (epoch <= max_epochs)
      e = zeros(batch_size, 1);
      count = 0;

      for m = 1 : depth-1
        dW{m} = zeros(size(W{m}));
        dB{m} = zeros(size(B{m}));
      end
      
      for p = batch_start : batch_start + batch_size
        
        V{1} = X_train(p, :);
        V{1} = V{1}.';
        count++;
        
        for i = 1 : depth - 1
            y{i} = W{i} * V{i} + B{i};
            if(strcmp(act_func, "tanh") == 1)
              V{i+1} = tanh(y{i}); %Calculo de la salida con tangente hiperbolica
            elseif(strcmp(act_func, "exp") == 1)
              V{i+1} = sigmoid(y{i});
            endif  
        end
        
        %Calculo Backward capa-por-capa para cada patron p
        if(strcmp(act_func, "tanh") == 1)     
          e(count, :) = (S_train(p, :) - 2 .* V{end}).^2;
          delta = derivateTanH(V{end}) .* (S_train(p, 1) - 2 .* V{end});
        elseif(strcmp(act_func, "exp") == 1)
          e(count, :) = (S_train(p, :) - (4 .* V{end} - 2)).^2;
          delta = derivateSigmoid(V{end}) .* (S_train(p, 1) - (4 .* V{end} - 2));
        endif  
        
        %Calculo de derivadas
        for i = depth-1 : -1 : 1
          dW{i} = dW{i} + delta * V{i}.';
          dB{i} = dB{i} + delta;
          if(strcmp(act_func, "tanh") == 1)
            delta = derivateTanH(V{i}) .* (W{i}.' * delta);
          elseif(strcmp(act_func, "exp") == 1)
            delta = derivateSigmoid(V{i}) .* (W{i}.' * delta);
          endif
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
      
      if(mse < epsilon)
        hits++;
      end
      
      sum_error += mse;
      error_count++;
      
      batch_start = batch_start + batch_size;
      
      if batch_start > P - batch_size
        batch_start = 1;
        epoch = epoch + 1;
        if (sum_error/error_count) < dmse
          finished = true;
        end
        output = test(X, X_mean, X_std, S, W, B, structure, act_func, 1-learn_percentage);
        plot_error(epoch, output.mse, error_color, 3);
        plot_mean_error(epoch, sum_error/error_count, error_color, 1);
        result.error = sum_error/error_count;
        hit_percentage = hits / error_count;
        plot_rate(epoch, avg_rate, rate_color, 2);
        plot_hits(epoch, hit_percentage, rate_color, 4);
        
        delta1 = prev_error4 - prev_error5;
        delta2 = prev_error3 - prev_error4;
        delta3 = prev_error2 - prev_error3;
        delta4 = prev_error1 - prev_error2;
        delta5 = result.error - prev_error1;
        
        if(strcmp(optimizer, "eta") == 1)
            if(delta1 < epsilon && delta2 < eta_epsilon && delta3 < eta_epsilon && delta4 < eta_epsilon && delta5 < eta_epsilon)
              rate = rate + a
            elseif(delta1 > eta_epsilon && delta2 > eta_epsilon && delta3 > eta_epsilon && delta4 > eta_epsilon && delta5 > eta_epsilon)
              rate = rate - b * rate
            endif
        endif
        
        prev_error5 = prev_error4;
        prev_error4 = prev_error3;
        prev_error3 = prev_error2;
        prev_error2 = prev_error1;
        prev_error1 = result.error;
        
        sum_error = 0;
        hits = 0;
        error_count = 0;
      end
      
  endwhile

  result.weights = W;
  result.biases = B;
  result.X_mean = X_mean;
  result.X_std = X_std;
  result.epochs = epoch - 1;
  result.act_func = act_func;
endfunction

function plot_mean_error(epoch, error, error_color, figure_number)
  hold on
  figure(figure_number);
  semilogy(epoch, error, 'ok', 'Color', error_color);
  title('Mean error', 'fontsize', 20);
  xlabel('Epoch');
  ylabel('Error');
  set(gca,'FontSize',20)
  drawnow
  hold off
endfunction

function plot_error(epoch, error, error_color, figure_number)
  hold on
  figure(figure_number);
  semilogy(epoch, error, 'ok', 'Color', error_color);
  title('Error', 'fontsize', 20);
  xlabel('Epoch');
  ylabel('Error');
  set(gca,'FontSize',20)
  drawnow
  hold off
endfunction

function plot_rate(epoch, rate, rate_color, figure_number)
  hold on
  figure(figure_number);
  semilogy(epoch, rate, 'ok', 'Color', rate_color);
  title('Learning rate', 'fontsize', 20);
  xlabel('Epoch');
  ylabel('Rate');
  set(gca,'FontSize',20)
  drawnow
  hold off
endfunction

function plot_hits(epoch, error, error_color, figure_number)
  hold on
  figure(figure_number);
  plot(epoch, error, 'ok', 'Color', error_color);
  title('Hit Percentage', 'fontsize', 20);
  xlabel('Epoch');
  ylabel('Percentage');
  set(gca,'FontSize',20)
  drawnow
  hold off
endfunction

function y = sigmoid(x)
  y = 1 ./ (1 + e.^-x);
endfunction

function y = derivateTanH(x)
  y = 1 - x.^2;
endfunction

function y = derivateSigmoid(x)
  y = x .* (1 - x);
endfunction
