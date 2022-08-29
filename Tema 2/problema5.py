import math

# Encuentra tanto el camino mínimo entre los nodos 1 y n como la longitud de dicho camino
def dijkstra(M, n):

    # Estructura de datos que almacena las distancias temporales conocidas
    # para los vértices no recorridos (inicialmente, todos salvo el 0).
    candidatos = [i for i in range(1, n)]

    distancias = []
    for i in range(1, n):
        distancias.append(M[0][i])

    predecesores = [0 for i in range(1, n)]

    # bucle voraz
    for i in range(n - 1):

        # Seleccionar como candidato el que tenga menor distancia temporal conocida
        menor_distancia = math.inf
        for d in range(len(distancias)):
            if distancias[d] < menor_distancia and (d + 1) in candidatos:
                menor_distancia = distancias[d]
                candidato = d + 1

        # Eliminar candiidato del conjunto de vértices no recorridos
        candidatos.remove(candidato)

        print("Paso:", i, "Selección:", candidato, "C:", candidatos, "D:", distancias)

        # actualizar el resto de distancias temporales si pueden ser mejoradas utilizando el vértice actual
        for w in range(1, len(distancias) + 1):
            alternativa = menor_distancia + M[candidato][w]
            if alternativa < distancias[w - 1]:
                distancias[w - 1] = alternativa
                predecesores[w - 1] = candidato

    # La longitud del camino hasta n
    longitud = distancias[-1]

    # Usando los predecesores se almacena la forma de recorrer el grafo desde el vértice 0 al vértice n
    i = n - 1
    camino = []
    while i != 0:
        camino.append(i + 1)
        i = predecesores[i - 1]

    camino.append(1)
    camino.reverse()

    return camino, longitud



# Matriz inicializada al coste de la arista del vértice 0 a cada vértice j, o +math.inf si no existe dicha arista

# Caso de prueba con el grafo de los apuntes de algoritmia
M = [
    [0, 50, 30, 100, 10],
    [math.inf, 0, math.inf, math.inf, math.inf],
    [math.inf, 5, 0, math.inf, math.inf],
    [math.inf, 20, 50, 0, math.inf],
    [math.inf, math.inf, math.inf, 10, 0]
]

n = len(M[0])
camino, longitud = dijkstra(M, n)
print("Camino mínimo entre los nodos 1 y", n, ":", camino, "con longitud", longitud)
print()

# Caso de prueba con el grafo de las diapositivas de Javier
M = [
    [0, 3, math.inf, math.inf, math.inf, math.inf, 4, math.inf],
    [math.inf, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf],
    [math.inf, math.inf, 0, 5, math.inf, math.inf, math.inf, math.inf],
    [math.inf, math.inf, math.inf, 0, 4, 2, math.inf, math.inf],
    [math.inf, 1, math.inf, math.inf, 0, math.inf, math.inf, math.inf],
    [math.inf, math.inf, math.inf, math.inf, 9, 0, 2, 3],
    [math.inf, math.inf, math.inf, math.inf, 7, math.inf, 0, math.inf],
    [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 2, 0]
]

n = len(M[0])
camino, longitud = dijkstra(M, n)
print("Camino mínimo entre los nodos 1 y", n, ":", camino, "con longitud", longitud)
print()

# Caso de prueba de la página web Baeldung
M = [
    [0, 10, 15, math.inf, math.inf, math.inf],
    [math.inf, 0, math.inf, 12, math.inf, 15],
    [math.inf, math.inf, 0, math.inf, 10, math.inf],
    [math.inf, math.inf, math.inf, 0, 2, 1],
    [math.inf, math.inf, math.inf, math.inf, 0, math.inf],
    [math.inf, math.inf, math.inf, math.inf, 5, 0],
]

n = len(M[0])
camino, longitud = dijkstra(M, n)
print("Camino mínimo entre los nodos 1 y", n, ":", camino, "con longitud", longitud)
print()
