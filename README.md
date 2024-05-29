# ÁLVARO GONZÁLEZ FERNÁNDEZ.

#  FACTORIAL EXPLICACION

La función factorial es una función que emplea recursividad para su resolución. El factorial de un número es el producto de todos los números enteros desde 1 hasta ese número, 
incluidos ambos y, por convenio, se acordó que el factorial de 0 es 1 y coincide con el factorial de 1. Como siempre, para la resolución de estas funciones recursivas, necesitamos un caso base.

### Caso base:

Tomaremos en este caso que el caso base será si el  número introducido es igual a 0 o 1, ya que habrá terminado el algoritmo y devolverá 1.

### Parte recursiva:

 En caso contrario, es decir,  si el número es estrictamente mayor que 1 pues la función devolverá el producto de ese número con el factorial de n-1 (es decir, el número -1) y aquí está la parte recursiva.
Esto significa que hasta que el número no sea 1, la función se llamará recursivamente y se estará multiplicando, como digo, hasta que el número que entre como parámtero sea 




# Bubble sort:

El método bubble sort es un algoritmo un tanto complejo utilizado para la ordenación de listas y tablas.  Consoiste básicamente en recorrer la lista tantas veces como elementos haya.
Esto significa que para su implementación necesitaremos una iteración dentro de otra, es decir, primero necesitaremos un for que recorra la lista n veces, siendo n la longitud 
de la lista. A continuación crearemos otro bucle for que recorrerá la lista e irá comparando cada elemento con el siguiente. En caso de que el elemento i sea mayor que el siguiente
pues estos dos se intercambian, y así hasta dejar ordenada toda la tabla.
### Ejemplo visual bubble sort.


 [34,7,23,32,5] Tabla desordenada. Empieza moviendo el primer número, el 34, y según sea mayor que el siguiente, se intercambiará.
 [7,34,23,32,5] 
 [7,23,34,32,5]
 [7,23,32,34,5]
 [7,23,32,5,34]  Así queda la tabla después de la primera vuelta
 [7,23,5,32,34] 
 [7,5,23,32,34] Segunda vuelta
 [5,7,23,32,34] Ultima vuelta, tabla ordenada (Aunque el bubble sort siempre hace como una ultima vuelta de comprobación).
