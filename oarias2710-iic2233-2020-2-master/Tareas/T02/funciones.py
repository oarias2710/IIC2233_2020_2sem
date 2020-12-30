# Funciones varias utilizadas en el programa

from parametros import MIN_LARGO, MAX_LARGO

# 1) Entrega mejores puntajes


def funcion_puntaje(elemento):
    return int(elemento[1])


def entrega_lineas_texto_ptjes(ruta):
    puntajes = open(ruta, "rt")
    lista_puntajes = puntajes.readlines()
    lista_nueva = []
    for elemento in lista_puntajes:
        elemento2 = elemento.strip("\n").split(",")
        lista_nueva.append(elemento2)
    lista_nueva.sort(reverse=True, key=funcion_puntaje)
    lista_texto = [" ", " ", " ", " ", " "]
    largo = min(5, len(lista_nueva))
    for i in range(largo):
        texto = lista_nueva[i][0] + ": " + lista_nueva[i][1] + " pts"
        lista_texto.pop(i)
        lista_texto.insert(i, texto)

    return lista_texto

# 2) Valida nombre usuario


def nombre_valido(nombre):
    if len(nombre) < MIN_LARGO or len(nombre) > MAX_LARGO or nombre.isalnum() is False:
        return False
    else:
        return True
