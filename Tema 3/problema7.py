from math import log, floor


def dividir(matriz, inicioColumna, finalColumna, inicioFila, finalFila):
    # Funciòn auxiliar para realizar la división de una matriz
    m = []
    i = 0
    for columna in range(inicioColumna, finalColumna):
        m.append([])
        for fila in range(inicioFila, finalFila):
            m[i].append(matriz[columna][fila])
        i += 1

    return m


def dividirEnCuadrantes(matriz):
    m1 = []
    m2 = []
    m3 = []
    m4 = []

    N = len(matriz)
    division = N // 2

    # Se divide la matriz en N / 2
    m1 = dividir(matriz, 0, division, 0, division)
    m2 = dividir(matriz, division, N, 0, division)
    m3 = dividir(matriz, 0, division, division, N)
    m4 = dividir(matriz, division, N, division, N)

    return (m1, m2, m3, m4)

def colocarCuadrantes(t1, t2, t3, t4):
    N = len(t1)

    # Se colocan los cuadrantes, primero t1 con t2
    for columna in range(N):
        for fila in range(N):
            t1[columna].append(t2[columna][fila])

    # Después t3 con t4
    for columna in range(N):
        for fila in range(N):
            t3[columna].append(t4[columna][fila])

   # Y por último se unen ambos resultados de t1 y t3 en una sola matriz
    for columna in range(N):
        t1.append(t3[columna])

    return t1

def transpuesta(matriz):
    # Caso base cuando la matriz es 2x2
    if len(matriz) == 2:
        tmp = matriz[0][1]
        matriz[0][1] = matriz[1][0]
        matriz[1][0] = tmp

        return matriz

    # Se divide en cuadrantes y se calcula su transpuesta
    m1, m2, m3, m4 = dividirEnCuadrantes(matriz)
    t1 = transpuesta(m1)
    t2 = transpuesta(m2)
    t3 = transpuesta(m3)
    t4 = transpuesta(m4)

    # Se colocan los cuadrantes para devolver la matriz completa y transpuesta
    t = colocarCuadrantes(t1, t2, t3, t4)

    return t

def esPotenciaDos(numero):
    # Para saber si un número es potencia de dos
    x = log(numero, 2)
    return 0 == (x - floor(x))

def mostrarMatriz(matriz):
    # Muestra la matriz como en el documento anexo
    N = len(matriz)

    for columna in range(N):
        for fila in range(N):
            print(matriz[columna][fila], '', end='')
        print()

def main(matriz):
    N = len(matriz)
    M = len(matriz)

    # Añadir filas y columnas de ceros hasta que N sea potencia de dos
    while not esPotenciaDos(M):
        matriz.append([0] * (M + 1))
        for columna in range(M):
            matriz[columna].append(0)

        M = len(matriz)

    # Se realiza la transpuesta de la matriz
    t = transpuesta(matriz)

    # Si se han añadido filas y columnas, se quitan para mostrarlo como originalmente era de NxN
    if N != M:
        resultado = []
        for columna in range(N):
            resultado.append([])
            for fila in range(N):
                resultado[columna].append(t[columna][fila])
    else:
        resultado = t

    mostrarMatriz(resultado)

# Caso de prueba de 2x2 para probar el caso base
matriz = [
    [0, 1],
    [0, 1]
]
print("Matriz original:")
mostrarMatriz(matriz)
print("Matriz tranpuesta:")
main(matriz)
print()

# Caso de prueba de 3x3 para probar cuando N es impar
matriz = [
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0]
]
print("Matriz original:")
mostrarMatriz(matriz)
print("Matriz tranpuesta:")
main(matriz)
print()

# Caso de prueba de 4x4 para probar cuando N es par
matriz = [
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 1, 1]
]
print("Matriz original:")
mostrarMatriz(matriz)
print("Matriz tranpuesta:")
main(matriz)
print()

# Primer caso del anexo: 5 calles
matriz = [
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0]
]
print("Matriz original:")
mostrarMatriz(matriz)
print("Matriz tranpuesta:")
main(matriz)
print()

# Segundo caso del anexo: 10 calles
matriz = [
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 1]
]
print("Matriz original:")
mostrarMatriz(matriz)
print("Matriz tranpuesta:")
main(matriz)
print()