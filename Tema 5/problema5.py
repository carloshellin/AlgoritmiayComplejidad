# Tabla de sustitución
M = [
    ["b", "b", "a", "d"],
    ["c", "a", "d", "a"],
    ["b", "a", "c", "c"],
    ["d", "c", "d", "b"]
]


def pertenece(caracter):
    # Un carácter debe pertenecer a uno de la tabla M
    return "a" <= caracter <= "d"


def indice(caracter):
    # Se calcula el índice para poder acceder a M fácilmente con a = 0, b = 1, c = 2 y d = 3
    return ord(caracter) - ord("a")


def sustitucion(cadena, caracterFinal, solucion = []):
    # Obtenemos la longitud de la cadena
    n = len(cadena)

    if not solucion:
        # En la primera iteracción añadimos la cadena inicial como parte de la solución para mostrar el camino
        solucion.append(cadena)

    # Caso base si la lonitud es 1 y el primer carácter de cadena ya es el carácter que buscamos (el final)
    if n == 1 and cadena[0] == caracterFinal:
        # Mostrarmos esa solución por pantalla
        print(solucion)

    for i in range(n - 1):
        # Almacenamos el primer y segundo carácter de la cadena
        primerCaracter = cadena[i]
        segundoCaracter = cadena[i + 1]

        # Si los dos caracteres pertenecen a la tabla M
        if pertenece(primerCaracter) and pertenece(segundoCaracter):
            # Obtenemos el valor que aparece en la tabla
            valor = M[indice(primerCaracter)][indice(segundoCaracter)]

            # Realizamos la sustitución de los dos caracteres por el valor
            cadenaSustituida = "".join([cadena[:i], valor, cadena[i + 2:]])
            # Lo añadimos como posible solución
            solucion.append(cadenaSustituida)

            # Llamamos recursivamente con la cadena sustituida
            sustitucion(cadenaSustituida, caracterFinal, solucion)

            # Quitamos la última solución y probamos con los otros dos siguientes cáracteres para ver si llegamos a la solución
            solucion.pop()
        else:
            # En el caso de que el primer o segundo carácter no pertenezca a la tabla, se da un aviso y se termina el algoritmo
            print("El carácter", primerCaracter, "o", segundoCaracter, "de la cadena de texto no pertenece a la tabla de sustitución M")
            return

print("A continuación se muestran todas las posibles soluciones de sustituir acabada hasta llegar a d")
sustitucion("acabada", "d")