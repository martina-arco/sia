function w = perceptronSimple()
  X = [-1, -1; 1, -1; -1 1; 1, 1]
  Y = [-1, -1, -1, 1]
  
  YOR = [-1, 1, 1, 1];
  threshold = -1;
  w = learn(X, Y, threshold);
  threshold
  r1 = neuron(w, X(1,:), threshold)
  r2 = neuron(w, X(2,:), threshold)
  r3 = neuron(w, X(3,:), threshold)
  r4 = neuron(w, X(4,:), threshold)
endfunction

function y = escalonada(value)
    if (value >= 0)
        y = 1;
    else
        y = -1;
    endif
endfunction

function o = neuron(w, x, threshold)
  o = escalonada(dot(w, x) + threshold);
endfunction

function w = learn(X, Y, threshold, alpha = 0.1, loops = 100)
    
  w = zeros(1,2);

  converged = false;

  for index = 1:loops

    if converged
      break;
    endif
    
    converged = true;
    
    for i = 1:rows(X)
        xi = X(i, :);
        expected = Y(i);
        o = neuron(w, xi, threshold);

        error = expected - o;
        dw = (alpha * error * xi);
        w = w + dw;
        
        if (error != 0)
            converged = false;
            break;
        endif
    endfor
  endfor

endfunction