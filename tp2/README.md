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

* **learnPercentage:** Porcentaje de patrones utilizados para aprendizaje.
* **batchSize:** Tamaño del bache para calcular error (en caso de que sea 1 se corre de forma iterativa).
* **epochNumber:** Cantidad máxima de épocas a utilizar.
* **maxError:** Error máximo a alcanzar.
* **learningRate:** Factor de aprendizaje.
* **actFunc:** Qué función de activación se va  utilizar (tanh, exp)
* **structure:** Vector con la arquitectura de la red, donde cada elemento es el número de neuronas en esa capa. En el ejemplo se muestra una red con dos capas ocultas, la primera de 2 neuronas y la segunda de 5.
* **optimizer:** Optimizador (momentum, adagrad, rmsprop, adam)
* **gamma:** Parametros para EMA. Se usa en momentum, rmsprop y adam
* **gamma2:** Parametros para EMA. Se usa en adam
```
Structure = [2, 5]
```

### Cómo correr

Ejecutar en línea de comandos
```
run
```
