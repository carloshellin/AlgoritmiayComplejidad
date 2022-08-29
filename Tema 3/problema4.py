
def quicksort(C, B, indice):
    # Caso base cuando hay uno o ceros elementos
    if len(C) <= 1:
        return C
    # Y cuando hay dos elementos
    elif len(C) == 2:
        return C if C[0] <= C[1] else [C[1], C[0]]

    izquierda = []
    derecha = []

    # Se usa como pivote los elementos que hay en la botellas
    valor = B[indice]
    try:
        index = C.index(valor)
    except:
        index = 0
    pivote = C[index]


    # Se recorren los corchos sin tener en cuenta el pivote
    for i in C[:index] + C[index + 1:]:
        # Los elementos menores o iguales que el pivote, van a la izquierda
        if i <= pivote:
            izquierda.append(i)
        # Los elementos mayores a la derecha
        else:
            derecha.append(i)

    # Se llama recursivamente a quicksort para la izquierda y derecha aumentando el indice para acceder a las botellas
    return quicksort(izquierda, B, indice + 1) + [pivote] + quicksort(derecha, B, indice + 1)


def ordenarCorchosBotellas(C, B):
    # Se realiza el quicksort de botellas y luego el de corchos usando las botellas ya ordenadas por quicksort
    B = quicksort(B, C, 0)
    C = quicksort(C, B, 0)

    # Se muestran los resultados
    for i in range(len(C)):
        print("El corcho del tamaño", C[i], "coincide con la botella del tamaño", B[i])
    print()


# Caso de prueba con 3 corchos y botellas para depurar con más facilidad
C = [1, 4, 3]
B = [4, 1, 3]
ordenarCorchosBotellas(C, B)

# Primer caso del anexo: 10 Corchos y botellas
C = [3, 5, 1, 7, 2, 10, 9, 4, 8, 6]
B = [6, 4, 3, 1, 9, 8, 10, 7, 5, 2]
ordenarCorchosBotellas(C, B)

# Segundo caso del anexo: 20 Corchos y botellas
C = [12, 1, 3, 10, 11, 2, 7, 15, 18, 5, 9, 20, 19, 4, 14, 13, 17, 16, 6, 8]
B = [7, 13, 2, 19, 10, 4, 9, 20, 1, 5, 15, 17, 6, 18, 3, 14, 16, 8, 12, 11]
ordenarCorchosBotellas(C, B)