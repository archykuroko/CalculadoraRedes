## Calculadora colaborativa en Github ##
# Integrantes:
#   1.  Escárcega Hernández Steven Arturo
#   2.  Dominguez Moreno Fernanda Michelle
#   3.  Absalón Cortés Sebastián
#   4.  Flores Osorio Adolfo
#   5.  
#   6. Rodriguez Garcia Pedro Uriel


import math

def suma (a, b):
    return a + b


def multiplicacion(a, b):
    return a * b

def potencia(a, b):
    return math.pow(a,b)

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b


def resta(a,b):
    return a-b



def mostrar_menu():
    print("Calculadora Básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == '6':
            print("Saliendo de la calculadora...")
            break
        
        if opcion in ('1', '2', '3', '4', '5'):
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            operaciones = {
                '1': suma,
                '2': resta,
                '3': multiplicacion,
                '4': division,
                '5': potencia
            }
            
            resultado = operaciones[opcion](num1, num2)
            print(f"El resultado es: {resultado}")
        else:
            print("Opción no válida, intente de nuevo.")

main()

