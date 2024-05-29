# ÁLVARO GONZÁLEZ FERNÁNDEZ.

#  EJERCICIO FIBONACCI

Este ejercicio de fibonacci consiste en replicar la sucesión de fibonacci utilizando un programa que contenga una parte recursiva. Como cualquier función recusriva, cuenta con un caso base y una parte recursiva.

### Caso base:
El caso base nos permite identificar uno de los ultimos pasos dde un porgrama, de tal forma que en la parte recursiva se ejecuta el programa indefinidamente a menos que haya una parte recursiva. Consiste, en nuestro ejemplo en una condición tal que si nuestro número o parámtero n es igual a 0 o a 1, la función devolverá 0 o 1 sumado a todo lo que se acumuló en la parte recursiva.



### Parte recursiva:
Bien en esta parte, la función se llama constantemente a si misma pero cada vez acercándose más al cas o base, momento en el que se detendrá. En la sucesión de fibonacci, un número n se obteniene de sumar los dos números que le preceden, es decir, n-1 y n-2, y en eso consiste nuestra parte recursiva.
 



# Bubble sort:

El método bubble sort es un algoritmo un tanto complejo utilizado para la ordenación de listas y tablas.  Consoiste básicamente en recorrer la lista tantas veces como elementos haya.
Esto significa que para su implementación necesitaremos una iteración dentro de otra, es decir, primero necesitaremos un for que recorra la lista n veces, siendo n la longitud 
de la lista. A continuación crearemos otro bucle for que recorrerá la lista e irá comparando cada elemento con el siguiente. En caso de que el elemento i sea mayor que el siguiente
pues estos dos se intercambian, y así hasta dejar ordenada toda la tabla.
### Ejemplo visual bubble sort.
[41, 33, 17, 80, 61]. Esta es la lista al inicio.
[33, 17, 41, 80, 61]. Así quedaría la lista después de la primera iteración
[17, 33, 41, 80, 61] Así quedaría la lista después de la segunda iteración.
[17, 33, 41, 61, 80] Así quedaría la lista después de la tercera iteración
y una cosa a tener en cuenta es que el método bubble sort, siempre hace una ultima iteración de comprobación.



