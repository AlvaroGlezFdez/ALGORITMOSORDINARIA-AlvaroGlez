

"""
Inicio

# Definición de la función para calcular los números de Fibonacci
Función fibonacci(n):
    Si n es igual a 0:
        Devolver 0
    Si n es igual a 1:
        Devolver 1
    Si n es mayor que 1:
        Devolver fibonacci(n-1) + fibonacci(n-2)

# Definición de la función principal
Función principal main():
    
    Imprimir "=================================================================."
    Imprimir "Test Case 1: Calculate the 0-th Fibonacci number."
    Imprimir "=================================================================."
    Si fibonacci(0) es igual a 0:
        Imprimir "Test PASS. The 0-th Fibonacci number is correct."
        Imprimir "The 0-th Fibonacci number is: ", fibonacci(0)
    De lo contrario:
        Imprimir "Test FAIL. The 0-th Fibonacci number is incorrect."

    [Repetir para los casos de prueba 2 a 6, cambiando el número de Fibonacci y el mensaje correspondientes]

# Verificar si este módulo se está ejecutando de manera independiente.
Si __name__ es igual a "__main__":
    Llamar a la función principal main()


    Fin 

"""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    
    print("=================================================================.")
    print("Test Case 1: Calculate the 0-th Fibonacci number.")
    print("=================================================================.")
    if fibonacci(0) == 0:
        print("Test PASS. The 0-th Fibonacci number is correct.")
        print("The 0-th Fibonacci number is: ", fibonacci(0))
    else:
        print("Test FAIL. The 0-th Fibonacci number is incorrect.")

    print("=================================================================.")
    print("Test Case 2: Calculate the 1-st Fibonacci number.")
    print("=================================================================.")
    if fibonacci(1) == 1:
        print("Test PASS. The 1-st Fibonacci number is correct.")
        print("The 1-st Fibonacci number is: ", fibonacci(1))
    else:
        print("Test FAIL. The 1-st Fibonacci number is incorrect.")

    print("=================================================================.")
    print("Test Case 3: Calculate the 2-nd Fibonacci number.")
    print("=================================================================.")
    if fibonacci(2) == 1:
        print("Test PASS. The 2-nd Fibonacci number is correct.")
        print("The 2-nd Fibonacci number is: ", fibonacci(2))
    else:
        print("Test FAIL. The 2-nd Fibonacci number is incorrect.")

    print("=================================================================.")
    print("Test Case 4: Calculate the 10-th Fibonacci number.")
    print("=================================================================.")
    if fibonacci(10) == 55:
        print("Test PASS. The 10-th Fibonacci number is correct.")
        print("The 10-th Fibonacci number is: ", fibonacci(10))
    else:
        print("Test FAIL. The 10-th Fibonacci number is incorrect.")

    print("=================================================================.")
    print("Test Case 5: Calculate the 15-th Fibonacci number.")
    print("=================================================================.")
    if fibonacci(15) == 610:
        print("Test PASS. The 15-th Fibonacci number is correct.")
        print("The 15-th Fibonacci number is: ", fibonacci(15))
    else:
        print("Test FAIL. The 15-th Fibonacci number is incorrect.")

    print("=================================================================.")
    print("Test Case 6: Calculate the 20-th Fibonacci number.")
    print("=================================================================.")
    if fibonacci(20) == 6765:
        print("Test PASS. The 20-th Fibonacci number is correct.")
        print("The 20-th Fibonacci number is: ", fibonacci(20))
    else:
        print("Test FAIL. The 20-th Fibonacci number is incorrect.")

if __name__ == "__main__":
    main()

