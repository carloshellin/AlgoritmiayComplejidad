from random import randint


def mejorCoste(escaleras):
    minutos = []
    total = 0
    i = 0

    # Para ejecutar el algoritmo debe haber dos o más escaleras
    while len(escaleras) >= 2:
        print("Iteración:", i)

        # Se ordenan las escaleras de menor a mayor, para buscar la forma óptima
        escaleras.sort()
        print("Se ordenan las escaleras de menor a mayor", escaleras)

        # Se asigna el valor de la primera y segunda escalera menor
        primerMenor = escaleras.pop(0)
        segundoMenor = escaleras.pop(0)
        print("Primer menor:", primerMenor, "Segundo menor:", segundoMenor)

        # Se suma sus valores menores y añadiendo el resultado a minutos
        suma = primerMenor + segundoMenor
        minutos.append(suma)
        print("Suma de ambos menores:", primerMenor, "+", segundoMenor, "=", suma)

        # Se añade la suma a las escaleras que en la siguiente iteración volverá a ordenarse de menor a mayor
        escaleras.append(suma)
        print("La suma se le añade a las escaleras:", escaleras)

        # Se va sumando el total del coste
        total += primerMenor + segundoMenor
        print("Se añade al total:", total)
        print()
        i += 1

    return minutos, total

# Caso de prueba del enunciado
escaleras = [6, 8, 7]
print("Escaleras:", escaleras)
minutos, total = mejorCoste(escaleras)
print("Los minutos de soldar son los siguientes:", minutos, "que en total son", total, "minutos")
print()

# Caso de prueba con repeticiones
escaleras = [4, 3, 2, 2, 8]
print("Escaleras:", escaleras)
minutos, total = mejorCoste(escaleras)
print("Los minutos de soldar son los siguientes:", minutos, "que en total son", total, "minutos")
print()

# Caso de prueba aleatorio
n = randint(2, 10)
escaleras = [randint(1, 10) for i in range(n)]
print("Escaleras:", escaleras)
minutos, total = mejorCoste(escaleras)
print("Los minutos de soldar son los siguientes:", minutos, "que en total son", total, "minutos")
print()

escaleras = [4]
print("Escaleras:", escaleras)
minutos, total = mejorCoste(escaleras)
print(total, ": el coste total es cero si solo hay una escalera para soldar")