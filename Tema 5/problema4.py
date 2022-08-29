
def esMovValido(i, j, p, q):
    # Un movimiento entre las casillas i,j y p,q es válido solamente si se cumple lo siguiente
    return (abs(p - i) == 1 and abs(q - j) == 2) or (abs(p - i) == 2 and abs(q - j) == 1)

def mostrarTablero(M):
    # Muestra el tablero con que movimiento ha realizado el caballo a cada casilla
    F = len(M)
    C = len(M[0])

    for fila in range(F):
        for columna in range(C):
            print(str(M[columna][fila]) + ", ", end='')
        print()

def recorrer(M, posx, posy, movimiento = 1):
    # Recorre todo el tablero moviendo al caballo en todas las casillas posibles
    F = len(M)
    C = len(M[0])

    # Se almacenamiento el número de movmiento que ha producido ir a la casilla
    M[posx][posy] = movimiento

    # El caso base es si movmiento es mayor o igual que el número total de casillas (F * C)
    if movimiento >= F * C:
        print("Solución encontrada: se muestra el tablero y en que movimiento se ha movido a cada casilla")
        mostrarTablero(M)
        return True

    for fila in range(F):
        for columna in range(C):
            # Si el movmiento es válido y la casilla no se ha visitado todavía
            if esMovValido(posx, posy, fila, columna) and M[fila][columna] == 0:
                # La casilla ya ha sido visitada
                #M[fila][columna] = 1

                # Se llama recursivamente para el siguiente movimiento
                if recorrer(M, fila, columna, movimiento + 1):
                    return True

    # Se pone a 0 la casilla para que el caballo pueda pasar por esta casilla en las siguientes llamadas
    M[posx][posy] = 0

    return False

def caballo(F, C, posx, posy):
    # Se crea un tablero M de F * C rellenados con 0
    M = [[0 for columna in range(C)] for fila in range(F)]

    if not recorrer(M, posx, posy):
        # En el caso de no poder recorrer todo el tablero con el caballo se muestra que no hay solución
        print("No se ha encontrado solución para que el caballo recorra todo el tablero de", F, "x", C)
        print("con el caballo en la posición inicial de (" + str(posx) + ", " + str(posy) + ")")

    print()

# Caso de prueba para comprobar cuando no se pueda recorrer todo el tablero
caballo(4, 4, 0, 0)

# Caso de prueba que el caballo sí va a poder recorrer todo el tablero
caballo(5, 5, 0, 0)

# Caso de prueba de 8x8 que pone como ejemplo el enunciando. Siempre tiene solución independientemente de dónde comience el caballo.
caballo(8, 8, 0, 0)