# Simple Squares

##Argumentos para correr el ejecutable
* -a : algoritmo de busqueda a utilizar (BFS, DFS, IDDFS, ASTAR, GREEDY)
* -h1 : uso de heuristica de distancia lineal
* -h2 : uso de heuristica
* -b : path para el archivo json que va a describir el tablero inicial partiendo como root sia-2019-1c-04

###Para armar un tablero
Los tableros ingresados deben ser cuadrados (nxn).
Se debe crear el array "squares" con los cuadrados a utilizar. Cada elemento va a tener:
* "name": que se utilizará para ubicarlo en el board
* "color" : color del cuadrado
* "direction" : sentido en el que se va a mover
```
"squares": [
    {"name":"s1", "color": "red", "direction": "down"},
    {"name":"s2", "color": "green", "direction":"down"},
    {"name":"s3", "color": "orange", "direction":"right"}
  ]
```

Se debe crear el array "circles" con los circulos a utilizar. Su composicion es similar al de squares.

```
"circles": [
    {"name":"c1", "color":"red"},
    {"name":"c2", "color":"green"},
    {"name":"c3", "color":"orange"}
  ],
```

Se debe crear la matriz "board" para posicionar cada elemento como se desee. Para una celda vacía se pone "0".

```
"board": [
    ["0", "s1","0","0"],
    ["s3", "c1","s2","0"],
    ["0", "0", "c2","0"],
    ["0","0","0","c3"]
  ]
```

Se encuentran múltiplos ejemplos en el repositorio.

##Para ejecutar

Posicionarse en carpeta root (sia-2019-1c-04)
```
mvn clean package
java -jar target/gps-1.0.jar (argumentos deseados)
```

##Ejemplos para correr


###Ejemplo clásico

```
java -jar target/gps-1.0.jar -a BFS -b board5.json
java -jar target/gps-1.0.jar -a DFS -b board5.json
java -jar target/gps-1.0.jar -a IDDFS -b board5.json
java -jar target/gps-1.0.jar -a GREEDY -h1 -b board5.json
java -jar target/gps-1.0.jar -a ASTAR -h1 -b board5.json
```

###Ejemplo para comparar heurísticas

```
java -jar target/gps-1.0.jar -a ASTAR -h1 -b board5.json
java -jar target/gps-1.0.jar -a ASTAR -h2 -b board5.json
```

###Ejemplo sin solución

```
java -jar target/gps-1.0.jar -a BFS -b noSolutionBoard.json
java -jar target/gps-1.0.jar -a DFS -b noSolutionBoard.json
java -jar target/gps-1.0.jar -a IDDFS -b noSolutionBoard.json
java -jar target/gps-1.0.jar -a GREEDY -h1 -b noSolutionBoard.json
java -jar target/gps-1.0.jar -a ASTAR -h1 -b noSolutionBoard.json
```

##Cómo correr los tests

```
mkdir output
mvn package | tee output/student_package_result.txt
cd ..
mvn install:install-file -Dfile=./sia-2019-1c-04/target/gps-1.0.jar -DgroupId=ar.edu.itba.sia -DartifactId=gps -Dversion=1.0 -Dpackaging=jar | tee ./sia-2019-1c-04/output/student_package_installing_result.txt
cd itba_sia_test
mvn package | tee ../sia-2019-1c-04/output/test_result.txt
```

Se cuenta con un archivo *how_will_test.sh* en el repositorio para correrlo directamente.
Los resultados quedarán en sia-2019-1c-04/output

