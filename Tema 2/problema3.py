from random import randint
import math


def buscarMinMax(V, n):
    mitad = math.ceil(n / 2)

    # Se recorre el vector desde 0 a n/2 (la mitad)
    for i in range(0, mitad):
        i_opuesta = n - 1 - i # La posición opuesta de i
        if V[i] > V[i_opuesta]:
            # Si los valores de la izquierda es mayor que los de la derecha, se intercambian
            # dejando así los valores menores a la izquierda y los mayores a la derecha del vector
            tmp = V[i]
            V[i] = V[i_opuesta]
            V[i_opuesta] = tmp

    print("Se recorre la mitad y si los valores de la izquierda es mayor que los de la derecha, se intercambian")
    print(V)

    # Se busca el mínimo desde 0 a n/2 (la mitad)
    min = V[0]
    for i in range(0, mitad):
        if V[i] < min:
            min = V[i]

    # Se busca el máximo desde n/2 a n (la otra mitad restante)
    max = V[mitad]
    for i in range(mitad, n):
        if V[i] > max:
            max = V[i]

    # En total se ha recorrido el vector en 3n/2
    return (min, max)


# Caso de prueba aleatorio
n = randint(2, 50)
V = [randint(-99, 99) for i in range(n)]
print("El vector generado es: ")
print(V)
minMax = buscarMinMax(V, n)
print("El valor mínimo es: " + str(minMax[0]) + " y el valor máximo es " + str(minMax[1]))
print()

# Caso de prueba cuando n es par
n = 4
V = [30, 20, 10, 40]
print(V)
minMax = buscarMinMax(V, n)
print("El valor mínimo es: " + str(minMax[0]) + " y el valor máximo es " + str(minMax[1]))
print()

# Caso de prueba cuando n es impar y el mínimo esta en medio
n = 3
V = [56, -39, 73]
print(V)
minMax = buscarMinMax(V, n)
print("El valor mínimo es: " + str(minMax[0]) + " y el valor máximo es " + str(minMax[1]))