function plot_terrain(X, Y, Z, grid_title)  xq = linspace(min(X), max(X));  yq = linspace(min(Y), max(Y));  [x,y] = meshgrid(xq, yq);  z_plot = griddata(X, Y, Z, x, y);  figure;  surf(x, y, z_plot);  title(grid_title, 'fontsize', 20);  xlabel('x');  ylabel('y');  zlabel('z');  grid on;
endfunction
