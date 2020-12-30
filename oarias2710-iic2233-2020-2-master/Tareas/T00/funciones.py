from parametros import RADIO_EXP
from parametros import NUM_BARCOS
import random

# Funciones a usar en la Tarea 00
# (este archivo debe estar en la misma carpeta del código que ejecuta el juego)


def puntaje(elemento):
    return int(elemento[1])

# Esta funcion pide un input numérico al usuario
# y se asegura de que la respuesta sea un int en el intervalo [0,n]


def respuesta_valida(n):
    opcion = "algo que jamás será una respuesta a nada"
    respuestas = []
    for i in range(n + 1):
        respuestas.append(i)
    while opcion not in respuestas:
        condicion = False
        while condicion is False:
            opcion_str = input(f"Ingresa tu opción {respuestas}:")
            if opcion_str.isdigit() is True:
                condicion = True
            elif opcion_str.isdigit() is False:
                print(f"{opcion_str} no es una respuesta válida")
                print(f"Debes ingresar un valor en el rango {respuestas}")
        opcion = int(opcion_str)
        if opcion not in respuestas:
            print(f"{opcion} es un valor fuera de rango")
            print(f"Debes ingresar un valor en el rango {respuestas}")
    return opcion


# Esta función pide una letra al usuario en el rango definido, valida la respuesta
# y devuelve la posición de la letra (coordenada de columna)
def respuesta_valida_letra(m):
    resp_posibles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    resp_validas = resp_posibles[0:m]
    opcion = "algo que jamás será una respuesta a nada"
    while opcion not in resp_validas:
        opcion_raw = input(f"Ingresa tu opción ({resp_validas}):")
        opcion = opcion_raw.upper()
        if opcion not in resp_validas:
            print(f"{opcion} no es una respuesta válida")
            print(f"Debes ingresar un valor en el rango de columnas")
    coord = resp_validas.index(opcion)
    return coord


def lanzar_bomba(tablero_rival, coord, esp_cruz, esp_x, esp_diamante):
    col_posibles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    diccionario_bombas = {
        0: "Regular",
        1: "Cruz",
        2: "X",
        3: "Diamante"
    }
    filas = len(tablero_rival)
    columnas = len(tablero_rival[0])
    barcos_destruidos = 0
    print("\n" + "Selecciona el tipo de bomba y las coordenadas")
    print("\n" + '*' * 5, "Tipos de bombas", '*' * 5, "\n")
    print("[0] Bomba Regular")
    print("[1] Bomba Especial 'Cruz'")
    print("[2] Bomba Especial 'X'")
    print("[3] Bomba Especial 'Diamante'" + "\n")
    print("Selecciona el tipo de bomba:")
    cond = False
    while cond is False:
        tipo_bomba = respuesta_valida(3)
        if tipo_bomba == 0:
            print("** Seleccionaste Bomba Regular")
            cond = True
        elif tipo_bomba == 1:
            if esp_cruz == 0:
                print("** Seleccionaste Bomba Especial 'Cruz'")
                esp_cruz += 1
                cond = True
            else:
                print("Ya agotaste este tipo de bomba. Elige otra opción")
        elif tipo_bomba == 2:
            if esp_x == 0:
                print("** Seleccionaste Bomba Especial 'X'")
                esp_x += 1
                cond = True
            else:
                print("Ya agotaste este tipo de bomba. Elige otra opción")
        elif tipo_bomba == 3:
            if esp_diamante == 0:
                print("** Seleccionaste Bomba Especial 'Diamante'")
                esp_diamante += 1
                cond = True
            else:
                print("Ya agotaste este tipo de bomba. Elige otra opción")

    print("\n" + "Selecciona las coordenadas del ataque:")
    cond2 = False
    while cond2 is False:
        print("Fila (indica número):")
        coord_fil = respuesta_valida(filas - 1)
        print("Columna (indica letra):")
        coord_col = respuesta_valida_letra(columnas)
        if [coord_fil, coord_col] in coord:
            print("\n" + "Ya disparaste en ese lugar. Elige otras coordenadas.")
        elif [coord_fil, coord_col] not in coord:
            cond2 = True
    lanza_tipo = diccionario_bombas[tipo_bomba]
    lanza_coord = str(coord_fil) + col_posibles[coord_col]
    print("\n" + f"** Lanzaste una bomba de tipo {lanza_tipo} a la coordenada {lanza_coord}")
    if tipo_bomba == 0:
        if tablero_rival[coord_fil][coord_col] == 'B':
            barcos_destruidos += 1
            tablero_rival[coord_fil][coord_col] = 'F'
        elif tablero_rival[coord_fil][coord_col] == ' ':
            tablero_rival[coord_fil][coord_col] = 'X'
    elif tipo_bomba == 1:
        coords_impacto = {(coord_fil, coord_col)}
        for j in range(columnas):
            tupla = (coord_fil, j)
            coords_impacto.add(tupla)
        for i in range(filas):
            tupla = (i, coord_col)
            coords_impacto.add(tupla)
        # limitamos las coord al rango
        min_fil = coord_fil - RADIO_EXP + 1
        max_fil = coord_fil + RADIO_EXP - 1
        min_col = coord_col - RADIO_EXP + 1
        max_col = coord_col + RADIO_EXP - 1
        coords_impacto2 = {(coord_fil, coord_col)}
        for elemento in coords_impacto:
            if elemento[0] >= min_fil and elemento[0] <= max_fil and \
                    elemento[1] >= min_col and elemento[1] <= max_col:
                coords_impacto2.add(elemento)
        for elem in coords_impacto2:
            if tablero_rival[elem[0]][elem[1]] == 'B':
                barcos_destruidos += 1
                tablero_rival[elem[0]][elem[1]] = 'F'
            elif tablero_rival[elem[0]][elem[1]] == ' ':
                tablero_rival[elem[0]][elem[1]] = 'X'
    elif tipo_bomba == 2:
        coords_impacto = {(coord_fil, coord_col)}
        dimension = max(filas, columnas)
        for k in range(dimension):
            tupla1 = (coord_fil + k, coord_col + k)
            tupla2 = (coord_fil + k, coord_col - k)
            tupla3 = (coord_fil - k, coord_col + k)
            tupla4 = (coord_fil - k, coord_col - k)
            coords_impacto.add(tupla1)
            coords_impacto.add(tupla2)
            coords_impacto.add(tupla3)
            coords_impacto.add(tupla4)
        # limitamos las coord al rango
        min_fil = max(coord_fil - RADIO_EXP + 1, 0)
        max_fil = min(coord_fil + RADIO_EXP - 1, filas - 1)
        min_col = max(coord_col - RADIO_EXP + 1, 0)
        max_col = min(coord_col + RADIO_EXP - 1, columnas - 1)
        coords_impacto2 = {(coord_fil, coord_col)}
        for elemento in coords_impacto:
            if elemento[0] >= min_fil and elemento[0] <= max_fil and \
                    elemento[1] >= min_col and elemento[1] <= max_col:
                coords_impacto2.add(elemento)
        for elem in coords_impacto2:
            if tablero_rival[elem[0]][elem[1]] == 'B':
                barcos_destruidos += 1
                tablero_rival[elem[0]][elem[1]] = 'F'
            elif tablero_rival[elem[0]][elem[1]] == ' ':
                tablero_rival[elem[0]][elem[1]] = 'X'
    elif tipo_bomba == 3:
        coords_impacto = {(coord_fil, coord_col)}
        for j in range(columnas):
            tupla = (coord_fil, j)
            coords_impacto.add(tupla)
        for i in range(filas):
            tupla = (i, coord_col)
            coords_impacto.add(tupla)
        # limitamos las coord al rango
        min_fil = coord_fil - RADIO_EXP + 1
        max_fil = coord_fil + RADIO_EXP - 1
        min_col = coord_col - RADIO_EXP + 1
        max_col = coord_col + RADIO_EXP - 1
        coords_impacto2 = {(coord_fil, coord_col)}
        for elemento in coords_impacto:
            if elemento[0] >= min_fil and elemento[0] <= max_fil and \
                    elemento[1] >= min_col and elemento[1] <= max_col:
                coords_impacto2.add(elemento)
        all_coords = {(0, 0)}
        for i in range(filas):
            for j in range(columnas):
                tupla = (i, j)
                all_coords.add(tupla)
        for elem in all_coords:
            if elem[0] > min_fil and elem[0] < max_fil and \
                    elem[1] > min_col and elem[1] < max_col:
                coords_impacto2.add(elem)
        for elem in coords_impacto2:
            if tablero_rival[elem[0]][elem[1]] == 'B':
                barcos_destruidos += 1
                tablero_rival[elem[0]][elem[1]] = 'F'
            elif tablero_rival[elem[0]][elem[1]] == ' ':
                tablero_rival[elem[0]][elem[1]] = 'X'
    return [[coord_fil, coord_col], tablero_rival, esp_cruz, esp_x, esp_diamante, barcos_destruidos]


def lanzar_bomba_regular(tablero_humano, coord):
    filas = len(tablero_humano)
    columnas = len(tablero_humano[0])
    barcos_destruidos = 0
    # fijar al azar coordenadas de ataque
    cond = False
    while cond is False:
        coord_fil = random.randint(0, filas - 1)
        coord_col = random.randint(0, columnas - 1)
        if [coord_fil, coord_col] not in coord:
            cond = True
    if tablero_humano[coord_fil][coord_col] == 'B':
        barcos_destruidos += 1
        tablero_humano[coord_fil][coord_col] = 'F'
    elif tablero_humano[coord_fil][coord_col] == ' ':
        tablero_humano[coord_fil][coord_col] = 'X'
    return [[coord_fil, coord_col], tablero_humano, barcos_destruidos]


def dimensiones_tablero():
    print("Ingresa el número de filas y columnas del tablero de juego")
    print("Valores válidos entre 3 y 15 (inclusive)")
    N = 99
    while N < 3 or N > 15:
        condicion = False
        while condicion is False:
            N_str = input("Número de filas del tablero: ")
            if N_str.isdigit() is True:
                condicion = True
            elif N_str.isdigit() is False:
                print("Debes ingresar un valor NUMÉRICO entre 3 y 15 (inclusive)")
        N = int(N_str)
        if N < 3 or N > 15:
            print("Debes ingresar un valor entre 3 y 15 (inclusive)")
    M = 99
    while M < 3 or M > 15:
        condicion = False
        while condicion is False:
            M_str = input("Número de columnas del tablero: ")
            if M_str.isdigit() is True:
                condicion = True
            elif M_str.isdigit() is False:
                print("Debes ingresar un valor NUMÉRICO entre 3 y 15 (inclusive)")
        M = int(M_str)
        if M < 3 or M > 15:
            print("Debes ingresar un valor entre 3 y 15 (inclusive)")
    return [N, M]


def crea_tableros(N, M):
    tableros = []
    for k in range(2):
        elem = []
        for i in range(N):
            componente = []
            for j in range(M):
                componente.append(" ")
            elem.append(componente)
        fil_aleatoria = []
        col_aleatoria = []
        for fil in range(N):
            fil_aleatoria.append(fil)
        for col in range(M):
            col_aleatoria.append(col)
        random.shuffle(fil_aleatoria)
        random.shuffle(col_aleatoria)
        contador_fil = 0
        contador_col = 0
        for barco in range(NUM_BARCOS):
            elem[fil_aleatoria[contador_fil]][col_aleatoria[contador_col]] = "B"
            contador_fil += 1
            contador_col += 1
        tableros.append(elem)
    return tableros
