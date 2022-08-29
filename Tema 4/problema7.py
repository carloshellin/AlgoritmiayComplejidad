

def esSubsecuencia(secuencia, subsecuencia):
    i = 0

    # Por cada bit de la subsencia
    for bit in subsecuencia:
        try:
            # Mientras que ese bit no este en la secuencia[i]
            while bit != secuencia[i]:
                # Se comprueba con el siguiente i
                i += 1
            i += 1
        except:
            # Si se pasa de rango en el índice i de secuencia, se devuelve False
            return False

    # Si es subsecuencia entonces devuelve True
    return True


def obtenerLongituxMax(A, B):
    N_A = len(A)
    N_B = len(B)

    # Se crea una matriz inicialmente a 0.
    matriz = [[0 for i in range(N_B)] for j in range(N_A)]

    # Se rellena la primera fila y primera columna
    for i in range(N_A):
        for j in range(N_B):
            # Para la primera fila y si el bit más significativo (MSB) de A está en B al menos una vez
            if i == 0 and A[0] in B[:j + 1]:
                # Se le pone un 1 a la matriz
                matriz[i][j] = 1
            # Para la primera columna y si el bit más significativo (MSB) de B está en A al menos una vez
            elif j == 0 and B[0] in A[:i + 1]:
                # Se le pone un 1 a la matriz
                matriz[i][j] = 1

    # Se empieza a rellenar la matriz sin necesidad de hacerlo para la primera fila y primera columna
    for i in range(1, N_A):
        for j in range(1, N_B):
            # Si la longitud no es la máxima posible y el bit de B[j] está en A[i]
            if matriz[i][j - 1] != i + 1 and B[j] == A[i]:
                # El tamaño máximo será el valor de la columna anterior más uno
                matriz[i][j] = matriz[i][j - 1] + 1
            # Sino el tamaño máximo será el valor de la columna anterior
            else:
                matriz[i][j] = matriz[i][j - 1]

    # Se muestra la matriz que se ha generado
    print("La matriz que se genera es:")
    for i in range(N_A):
        print("\t", matriz[i])

    # Se devuelve la longitud máxima posible que se situa en la última fila y última columna de la matriz
    return matriz[N_A - 1][N_B - 1]

def obtenerSecuenciaComun(A, B):
    # Se obtiene la longitud máxima posible con programación dinámica
    longitudMax = obtenerLongituxMax(A, B)

    resultados = []
    # Se recorre las X posibles secuencias comunes
    for i in range(2 ** longitudMax):
        X = "{0:b}".format(i)

        # Si la X longitud posible no es igual a la longitud máxima, se rellenan con ceros por la izquierda
        if len(X) != longitudMax:
            X = X.zfill(longitudMax)

        # Si la X posible secuencia es subsecuencia de A y subsecuencia de B, se denomina a X una subsecuencia común de A y B
        if esSubsecuencia(A, X) and esSubsecuencia(B, X):
            resultados.append(X)

    print("Todas las secuencias comunes de A", A, "y B", B, "de longitud máxima", longitudMax, "son las siguientes:")
    print(resultados)
    print()

# Primer caso del anexo
A = "011"
B = "1010"
obtenerSecuenciaComun(A, B)

# Segundo caso del anexo
A = "01101010"
B = "101001001"
obtenerSecuenciaComun(A, B)

# Tercero caso cuando A y B son del mismo tamaño
A = "1001"
B = "1100"
obtenerSecuenciaComun(A, B)

# Cuarto caso con longitud máxima 4
A = "1101101010"
B = "010110101"
obtenerSecuenciaComun(A, B)