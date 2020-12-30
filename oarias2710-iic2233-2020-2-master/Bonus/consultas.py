# Actividad Bonus IIC2233 2020-2

import pyrematch as re

# -------------------------------------------------------------------
# DEFINIR AQUI LOS PATRONES PARA CONSTRUIR CADA EXPRESION REGULAR
# NO CAMBIAR LOS NOMBRES DE LAS VARIABLES
PATRON1 = "(\s==\s)!text{[^\n]+}(\s==\s)"
PATRON2 = "(\s===\s)!text{[^\n]+}(\s===\s)"
PATRON3 = "(\s====\s)!text{[^\n]+}(\s====\s)"
PATRON4 = "(\s==\s)!text{[^\n]+}(\s==\s)!contenido{(\n*\s*[^=]+\.*\n*\s*)|(\n)}($|\s==\s)"
PATRON5 = "(\s===\s)!text{[^\n]+}(\s===\s)!contenido{(\n*\s*[^=]+\.*\n*\s*((\s====\s)[^\n]+(\s====\s))?\n*\s*[^=]+\.*\n*\s*)|(\n)}($|\s===\s|\s==\s)"
PATRON6 = "(\s===\s)!text{[^\n]+}(\s===\s)!contenido1{\n*\s*[^=]+\.+\n+\s+}(\s====\s)[^\n]+(\s====\s)!contenido2{\n*\s*[^=]+\.+\n+\s+}(\s===\s)"


# -------------------------------------------------------------------
# Complete a continuación el código de cada consulta.
# Cada consulta recibe el patrón correspondiente para construir la expresión
# regular, y el texto sobre el cual se aplicará.
# Cada consulta debe retornar una lista de tuplas, donde cada tupla contiene
# el match encontrado, su posición de inicio y su posición de término.


# CONSULTA 1

def consulta1(texto, patron):
    pattern = patron
    regex = re.compile(pattern)
    lista = []
    for match in regex.finditer(texto):
        tupla = (match.group('text'), match.start('text'), match.end('text'))
        lista.append(tupla)
    return lista


# CONSULTA 2

def consulta2(texto, patron):
    pattern = patron
    regex = re.compile(pattern)
    lista = []
    for match in regex.finditer(texto):
        tupla = (match.group('text'), match.start('text'), match.end('text'))
        lista.append(tupla)
    return lista


# CONSULTA 3

def consulta3(texto, patron):
    pattern = patron
    regex = re.compile(pattern)
    lista = []
    for match in regex.finditer(texto):
        tupla = (match.group('text'), match.start('text'), match.end('text'))
        lista.append(tupla)
    return lista


# CONSULTA 4

def consulta4(texto, patron):
    pattern = patron
    regex = re.compile(pattern)
    lista = []
    for match in regex.finditer(texto):
        tupla = (match.group('text'), match.start('contenido'), match.end('contenido'))
        lista.append(tupla)
    return lista


# CONSULTA 5

def consulta5(texto, patron):
    pattern = patron
    regex = re.compile(pattern)
    lista = []
    for match in regex.finditer(texto):
        tupla = (match.group('text'), match.start('contenido'), match.end('contenido'))
        lista.append(tupla)
    return lista


# CONSULTA 6

def consulta6(texto, patron):
    pattern = patron
    regex = re.compile(pattern)
    lista = []
    for match in regex.finditer(texto):
        tupla = (match.group('text'), match.start('contenido1'), match.end('contenido2'))
        lista.append(tupla)
    return lista

