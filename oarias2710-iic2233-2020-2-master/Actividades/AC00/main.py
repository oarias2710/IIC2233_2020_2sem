from collections import namedtuple, defaultdict


# Para esta parte necesitarás los contenidos de la semana 0
# LISTO
def cargar_datos(path):
    # Para esta función te puede servir el cuaderno 3 de la semana 0
    datos = open(path, "rt")
    datos_lista = datos.readlines()
    return datos_lista


# De aquí en adelante necesitarás los contenidos de la semana 1
# LISTO
def crear_ayudantes(datos):
    # Completar función
    lista = []
    for elem in datos:
        elem_temp = elem.strip("\n")
        lista_temp = elem_temp.rsplit(",")
        lista_temp2 = []
        for elem2 in lista_temp:
            unidad = elem2.strip(" ")
            lista_temp2.append(unidad)
        lista.append(lista_temp2)
    InfoAyudante = namedtuple('InfoAyudante_type', ['nombre', 'cargo', 'usuario'])
    lista_tuplas = []
    ndatos = len(lista)
    for i in range(1, ndatos):
        tupla = InfoAyudante(lista[i][0], lista[i][1], lista[i][2])
        lista_tuplas.append(tupla)
    return lista_tuplas


# LISTO
def encontrar_cargos(ayudantes):
    # Completar función
    lista = []
    for elem in ayudantes:
        lista.append(elem.cargo)
    return set(lista)


# LISTO
def ayudantes_por_cargo(ayudantes):
    # Completar función
    lista_ft = []
    lista_fd = []
    lista_hd = []
    lista_ht = []
    for elem in ayudantes:
        if elem.cargo == 'Full Tareas':
            lista_ft.append(elem.nombre)
        elif elem.cargo == 'Full Docencia':
            lista_fd.append(elem.nombre)
        elif elem.cargo == 'Híbrido Docencia':
            lista_hd.append(elem.nombre)
        elif elem.cargo == 'Híbrido Tareas':
            lista_ht.append(elem.nombre)
    diccionario = {'Full Tareas': lista_ft,
                   'Full Docencia': lista_fd,
                   'Híbrido Docencia': lista_hd,
                   'Híbrido Tareas': lista_ht}
    return diccionario


if __name__ == '__main__':
    datos = cargar_datos('ayudantes.csv')
    if datos is not None:
        print('Se lograron leer los datos')
    else:
        print('Debes completar la carga de datos')

    ayudantes = crear_ayudantes(datos)
    if ayudantes is not None:
        print('\nLos ayudantes son:')
        for ayudante in ayudantes:
            print(ayudante)
    else:
        print('\nDebes completar la creación de Ayudantes')

    cargos = encontrar_cargos(ayudantes)
    if cargos is not None:
        print('\nLos cargos son:')
        for cargo in cargos:
            print(cargo)
    else:
        print('\nDebes completar la búsqueda de Cargos')

    clasificados = ayudantes_por_cargo(ayudantes)
    if clasificados is not None:
        print('\nLos ayudantes por cargos son:')
        for cargo in clasificados:
            print(f'\n{cargo}')
            for ayudante in clasificados[cargo]:
                print(ayudante)
    else:
        print('\nDebes completar la clasificación de Ayudantes')
