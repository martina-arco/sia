### Inicialización

Para poder correr el programa uno debe poner su current folder en tp2 e instalar la librería statistics.

```
pkg install -forge io
pkg install -forge statistics
```

Luego, se debe inicializar con los valores del terreno provistos por *terrain04.data*.

```
initialize
```
## Configuración de parámetros

En el archivo *run.m* se pueden setear los diferentes parámetros para poder configurar la red neuronal como se desee. Estos parámetros incluyen:

* **learn_percentage:** Porcentaje de patrones utilizados para aprendizaje.
* **type:** Batch o incremental.
* **max_epochs:** Cantidad máxima de épocas a utilizar.
* **max_error:** Error máximo a alcanzar.
* **learning_rate:** Factor de aprendizaje.
* **act_func:** Qué función de activación se va  utilizar (tanh, exp).
* **optimizer:** Optimizador (momentum, adagrad, eta).
* **gamma:** Parametros para EMA. Se usa en momentum.
* **error_color:** Color a utilizar para graficar el error.
* **rate_color:** Color a utilizar para graficar el factor de aprendizaje.
* **structure:** Vector con la arquitectura de la red, donde cada elemento es el número de neuronas en esa capa. Siempre debe empezar con 2 y terminar con 1 debido al tipo de problema. En el ejemplo se muestra una red con dos capas ocultas, la primera de 2 neuronas y la segunda de 5.
* **a:** Parámetro de eta.
* **b:** Parámetro de eta.
* **eta_epsilon:** Parámetro de eta.

```
Structure = [2, 2, 5, 1]
```

### Cómo correr

Ejecutar en línea de comandos
```
run
```

### Cómo testear
Para graficar
```
plot_terrain(patterns(:,1), patterns(:,2), S, 'Terrain')
```
Para testear primero debe ejecutarse run. En el ejemplo se muestra un porcentaje de 0.99 pero se puede utilizar cualquiera deseado para determinar la cantidad de muestras a utilizar.
```
output = test(patterns, result.X_mean, result.X_std, S, result.weights, result.biases, structure, result.act_func, 0.99)
```
Si se desea graficar este plano
```
plot_terrain(output.evaluation(:,1), output.evaluation(:,2), output.approximate, 'Approximate terrain')
```
