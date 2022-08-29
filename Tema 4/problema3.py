import math

def pagar(v, c, D):
    print("Cantidad:", D)
    print("Valor:", v)
    print("Cantidad de monedas:", c)

    N = len(v)

    # Se crea una matriz inicialmente a 0.
    # Las filas son los valores de cada moneda
    # Las columnas son las posibles cantidades a pagar desde 0 hasta D + 1
    matriz = [[0 for i in range(D + 1)] for j in range(N + 1)]

    # En la primera fila y desde la segunda columna se llena de infinito
    for j in range(1, D + 1):
        matriz[0][j] = math.inf

    # Se empieza a rellenar la matriz
    for i in range(1, N + 1):
        for j in range(1, D + 1):
            minimo = matriz[i - 1][j]

            # Si la cantidad a pagar es menor que el valor de la moneda actual
            if j < v[i - 1]:
                # el número de monedas a devolver es lo que hay que devolver con la anterior moneda
                matriz[i][j] = minimo
            # Si el valor de la moneda actual por la cantidad de esa moneda es mayor o igual que la cantidad a pagar
            elif (v[i - 1] * c[i - 1]) >= j:
                # el mínimo sería entre lo que hay que devolver con la anterior moneda y la fila actual restando
                # a la columna el valor de la moneda actual. A esto último se le suma uno.
                minimo = min(minimo, matriz[i][j - v[i - 1]] + 1)
            # Sino
            else:
                # el mínimo sería entre lo que hay que devolver con la anterior moneda y la fila anterior restando
                # a la columna el valor de la moneda actual por la cantidad de monedas de ese valor.
                # A esto último se le suma la cantidad de monedas que hay de ese valor.
                minimo = min(minimo, matriz[i - 1][j - (v[i - 1] * c[i - 1])] + c[i - 1])

            # Se almacena el mínimo en i y j
            matriz[i][j] = minimo

    # Se muestra la matriz que se ha generado
    print("La matriz que se genera es:")
    for i in range(1, N + 1):
        print(v[i - 1], end=' ')
        print("\t", matriz[i])

    # Se obtiene el número de monedas a devolver usando la matriz
    devolver = 0 if matriz[N - 1][D - 1] == math.inf else matriz[N][D]

    # Se muestra si se puede devolver las monedas y de ser así, muestra cuántos billetes de cada tipo forman
    # la descomposición óptima
    if devolver != 0:
        print("Hay que devolver", devolver, "monedas")

        total = 0
        for i in range(N):
            monedas = 0
            posicion = - (i + 1)

            if (v[posicion] + total > D): continue

            while c[posicion] - (monedas + 1) >= 0 and (monedas + 1) * v[posicion] <= (D - total) and devolver > 0:
                monedas += 1
                devolver -= 1
            print(monedas, "monedas de", v[posicion])
            total += monedas * v[posicion]

            if (devolver <= 0):
                print()
                break
    else:
        print("No es posible devolver con las monedas que hay disponibles")

# Primer caso del anexo
v = [1, 3, 5]
c = [15, 5, 5]
D = 11
pagar(v, c, D)

# Segundo caso del anexo
v = [1, 3, 5]
c = [3, 5, 2]
D = 11
pagar(v, c, D)

# Tercero caso del anexo
v = [1, 20, 50, 100]
c = [1, 10, 5, 1]
D = 201
pagar(v, c, D)

# Caso de prueba con partes del enunciado
v = [1, 2, 5, 10, 20, 50, 100]
c = [1, 2, 6, 4, 2, 5, 1]
D = 105
pagar(v, c, D)