import random
import json
from faker import Faker
import socket
from networking import Server
fake = Faker("es_MX")
Faker.seed(0)
random.seed(666)


class Mapa:
    def __init__(self, ruta_grafo, ruta_parametros, jugadores):
        # la lista de adyacencia es una lista de instancias de la clase Nodo
        self.lista_nodos = self.crear_nodos()
        with open(ruta_grafo, "rb") as file:
            datos_grafo = json.load(file)
        self.dim_mapa = datos_grafo['dimensiones_mapa']
        adyacencia_nodos = datos_grafo['nodos']
        self.nodos_en_hexagonos = datos_grafo['hexagonos']
        adyacencia_instancias_nodos = {}

        for elem in adyacencia_nodos:
            key = int(elem)
            nodo = self.lista_nodos[key]
            lista_adyacentes = []
            for elem2 in adyacencia_nodos[elem]:
                lista_adyacentes.append(self.lista_nodos[int(elem2)])
            adyacencia_instancias_nodos[nodo] = lista_adyacentes
        self.lista_adyacencia = adyacencia_instancias_nodos
        self.lista_caminos = self.crear_caminos()
        self.hexagonos = self.crear_hexagonos()
        self.jugadores = jugadores

        with open(ruta_parametros, "rb") as file:
            self.parametros = json.load(file)
        self.nodos_usados, self.lista_carreteras = self.prepara_juego()

    def vecinos(self, x):
        return self.lista_adyacencia[x]

    def crear_nodos(self):
        lista_nodos = []
        for i in range(0, 33):
            nodo = Nodo(str(i))
            lista_nodos.append(nodo)
        return lista_nodos

    def crear_caminos(self):
        lista_caminos = []
        lista_ids_caminos = []
        for elem in self.lista_adyacencia:
            for elem2 in self.lista_adyacencia[elem]:
                camino = Camino(elem, elem2)
                if camino.id not in lista_ids_caminos:
                    lista_caminos.append(camino)
                    lista_ids_caminos.append(camino.id)
        return lista_caminos

    def crear_hexagonos(self):
        hexagonos = []
        for elem in self.nodos_en_hexagonos:
            elementos_hexagono = []
            for elem2 in self.nodos_en_hexagonos[elem]:
                elementos_hexagono.append(self.lista_nodos[int(elem2)])
            hexagono = Hexagono(elementos_hexagono)
            hexagonos.append(hexagono)
        # Atributos de los Hexagonos
        # id de los hexagonos
        for i in range(0, 10):
            hexagonos[i].id = int(i)
        # numero de ficha de los hexagonos
        numeros = [2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
        numeros_usados = []
        for i in range(0, 10):
            cond = True
            while cond is True:
                ficha = random.choice(numeros)
                if ficha not in numeros_usados:
                    hexagonos[i].numero_ficha = ficha
                    numeros_usados.append(ficha)
                    cond = False
        # asignación materias primas de los hexagonos
        condicion = True
        materias_primas = ["madera", "arcilla", "trigo"]
        while condicion is True:
            lista_materias_primas = []
            for i in range(10):
                materia = random.choice(materias_primas)
                lista_materias_primas.append(materia)
            madera = lista_materias_primas.count("madera")
            arcilla = lista_materias_primas.count("arcilla")
            trigo = lista_materias_primas.count("trigo")
            if madera >= 3 and arcilla >= 3 and trigo >= 3:
                condicion = False
        for i in range(10):
            hexagonos[i].materia_prima = lista_materias_primas[i]
        return hexagonos

    def prepara_juego(self):
        # orden aleatorio de jugadores
        orden = []
        for i in range(1, len(self.jugadores) + 1):
            orden.append(i)
        orden_usado = []
        for i in range(len(self.jugadores)):
            cond = True
            while cond is True:
                valor = random.choice(orden)
                if valor not in orden_usado:
                    orden_usado.append(valor)
                    self.jugadores[i].turno = valor
                    cond = False
        # dos chozas al azar por jugador, respetando reglas
        nodos_usados = []
        for i in range(len(self.jugadores)):
            cond = 0
            while cond < 2:
                nodo = random.choice(self.lista_nodos)
                vecinos = self.vecinos(nodo)
                chozas_vecinas = 0
                for elem in vecinos:
                    if elem.choza is True:
                        chozas_vecinas += 1
                if chozas_vecinas == 0 and nodo not in nodos_usados:
                    nodo.choza = True
                    nodo.usuario = self.jugadores[i]
                    self.jugadores[i].chozas += 1
                    cond += 1
                    nodos_usados.append(nodo)
        # dos carreteras al azar por jugador, respetando reglas
        lista_carreteras = []
        for i in range(len(self.jugadores)):
            cond = 0
            while cond < 2:
                carr = random.choice(self.lista_caminos)
                contador = 0
                if carr.nodos[0].choza is True and carr.nodos[0].usuario == self.jugadores[i]:
                    contador += 1
                if carr.nodos[1].choza is True and carr.nodos[1].usuario == self.jugadores[i]:
                    contador += 1
                for elem in lista_carreteras:
                    if carr.nodos[0] in elem.nodos and elem.usuario == self.jugadores[i]:
                        contador += 1
                    if carr.nodos[1] in elem.nodos and elem.usuario == self.jugadores[i]:
                        contador += 1
                if contador != 0 and carr.id not in lista_carreteras:
                    carr.usuario = self.jugadores[i]
                    self.jugadores[i].carreteras += 1
                    carr.es_carretera = True
                    cond += 1
                    lista_carreteras.append(carr)
        # repartir cartas
        for elem in self.hexagonos:
            for nodo in elem.lista_nodos:
                if nodo.usuario is not None:
                    if elem.materia_prima == "madera":
                        nodo.usuario.madera += self.parametros["GANANCIA_MATERIA_PRIMA"]
                    elif elem.materia_prima == "arcilla":
                        nodo.usuario.arcilla += self.parametros["GANANCIA_MATERIA_PRIMA"]
                    elif elem.materia_prima == "trigo":
                        nodo.usuario.trigo += self.parametros["GANANCIA_MATERIA_PRIMA"]
        return nodos_usados, lista_carreteras

    def lanzamiento_dados(self, jugador):
        dado = [1, 2, 3, 4, 5, 6]
        resultado = random.choice(dado) + random.choice(dado)
        if resultado == 7:
            premio = random.choice(['arcilla', 'madera', 'trigo'])
            if premio == 'arcilla':
                jugador.arcilla += self.parametros['PREMIO_NUMERO_SIETE']
            elif premio == 'madera':
                jugador.madera += self.parametros['PREMIO_NUMERO_SIETE']
            elif premio == 'trigo':
                jugador.trigo += self.parametros['PREMIO_NUMERO_SIETE']
        else:
            for hexagono in self.hexagonos:
                for nodo in hexagono.lista_nodos:
                    if hexagono.numero_ficha == resultado:
                        if nodo.choza is True and nodo.usuario == jugador:
                            if hexagono.materia_prima == 'arcilla':
                                jugador.arcilla += self.parametros['GANANCIA_MATERIA_PRIMA']
                            elif hexagono.materia_prima == 'madera':
                                jugador.madera += self.parametros['GANANCIA_MATERIA_PRIMA']
                            elif hexagono.materia_prima == 'trigo':
                                jugador.trigo += self.parametros['GANANCIA_MATERIA_PRIMA']

    def asignacion_puntajes(self):
        contador = 0
        for jugador in self.jugadores:
            total = (jugador.carreteras * self.parametros['PTOS_CARRETERA']
                     + jugador.chozas * self.parametros['PTOS_CHOZA'])
            jugador.puntos = total
            if jugador.puntos >= self.parametros['PUNTOS_PARA_VICTORIA']:
                contador += 1
        return contador

    def construir_carretera(self, jugador, nodo1, nodo2):
        camino = Camino(nodo1, nodo2)
        nodos_carreteras_jugador = []
        for elem in self.lista_carreteras:
            if elem.usuario == jugador:
                nodo_a = elem.nodos[0]
                nodo_b = elem.nodos[1]
                if nodo_a not in nodos_carreteras_jugador:
                    nodos_carreteras_jugador.append(nodo_a)
                if nodo_b not in nodos_carreteras_jugador:
                    nodos_carreteras_jugador.append(nodo_b)
        contador_choza = 0
        if nodo1.usuario == jugador:
            contador_choza += 1
        if nodo2.usuario == jugador:
            contador_choza += 1
        contador_carre = 0
        if nodo1 in nodos_carreteras_jugador:
            contador_carre += 1
        if nodo2 in nodos_carreteras_jugador:
            contador_carre += 1
        lista_ids_caminos = []
        for elem in self.lista_caminos:
            lista_ids_caminos.append(elem.id)
        if camino.id not in lista_ids_caminos:
            return "No es camino válido"
        elif camino in self.lista_carreteras:
            return "Ya existe esa carretera"
        elif jugador.arcilla < self.parametros['CANTIDAD_ARCILLA_CARRETERA']:
            return "No tiene arcilla suficiente"
        elif jugador.madera < self.parametros['CANTIDAD_MADERA_CARRETERA']:
            return "No tiene madera suficiente"
        elif contador_choza == 0 and contador_carre == 0:
            return "No está adyacente a choza u otra carretera del jugador"
        else:
            self.lista_carreteras.append(camino)
            camino.es_carretera = True
            camino.usuario = jugador
            jugador.carreteras += 1
            jugador.arcilla -= self.parametros['CANTIDAD_ARCILLA_CARRETERA']
            jugador.madera -= self.parametros['CANTIDAD_MADERA_CARRETERA']
            return f"{jugador.nombre} completa carretera entre {nodo1.id_nodo} y {nodo2.id_nodo}"

    def construir_choza(self, jugador, nodo):
        vecinos = self.vecinos(nodo)
        chozas_vecinas = 0
        for elem in vecinos:
            if elem.choza is True:
                chozas_vecinas += 1
        if jugador.arcilla < self.parametros['CANTIDAD_ARCILLA_CHOZA']:
            return "No tiene arcilla suficiente"
        elif jugador.madera < self.parametros['CANTIDAD_MADERA_CHOZA']:
            return "No tiene madera suficiente"
        elif chozas_vecinas != 0:
            return "Hay una choza en nodo adyacente"
        elif chozas_vecinas == 0 and nodo not in self.nodos_usados:
            nodo.choza = True
            nodo.usuario = jugador
            jugador.chozas += 1
            self.nodos_usados.append(nodo)
            return f"{jugador.nombre} construye choza en nodo {nodo.id_nodo}"

    def __repr__(self):
        texto_nodos = []
        for nodo, vecinos in self.lista_adyacencia.items():
            texto_nodos.append(f"Nodos conectados con {nodo}: {vecinos}.")
        return "\n".join(texto_nodos)


class Nodo:
    def __init__(self, id):
        self.id_nodo = id
        self.choza = False
        self.usuario = None

    def __repr__(self):
        if self.choza is True:
            return (f"Nodo ID {self.id_nodo} tiene una choza y"
                    f" su usuario es {self.usuario.nombre}")
        elif self.choza is False:
            return (f"Nodo ID {self.id_nodo} no tiene choza y"
                    f" su usuario es {self.usuario}")


class Camino:
    def __init__(self, nodo1, nodo2):
        self.es_carretera = False
        self.nom_nodo1 = min(int(nodo1.id_nodo), int(nodo2.id_nodo))
        self.nom_nodo2 = max(int(nodo1.id_nodo), int(nodo2.id_nodo))
        self.nodos = [nodo1, nodo2]
        self.id = str(self.nom_nodo1 * 100 + self.nom_nodo2)
        self.usuario = None

    def __repr__(self):
        if self.es_carretera is False:
            return (f"Hay un CAMINO entre "
                    f"nodos {self.nom_nodo1} y {self.nom_nodo2}, "
                    f"perteneciente a {self.usuario}")
        elif self.es_carretera is True:
            return (f"Hay una CARRETERA entre "
                    f"nodos {self.nom_nodo1} y {self.nom_nodo2}, "
                    f"perteneciente a {self.usuario.nombre}")


class Hexagono:
    def __init__(self, lista):
        self.lista_nodos = lista
        self.id = None
        self.numero_ficha = None
        self.materia_prima = None

    def __repr__(self):
        return (f"Hexagono {self.id}, num. de ficha {self.numero_ficha}, "
                f"materia prima {self.materia_prima}, "
                f"tiene estos nodos: "
                f"{self.lista_nodos[0].id_nodo},{self.lista_nodos[1].id_nodo},"
                f"{self.lista_nodos[2].id_nodo},{self.lista_nodos[3].id_nodo},"
                f"{self.lista_nodos[4].id_nodo},{self.lista_nodos[5].id_nodo}.")


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.turno = None
        self.madera = 0
        self.arcilla = 0
        self.trigo = 0
        self.puntos = 0
        self.carreteras = 0
        self.chozas = 0

    def __repr__(self):
        return (f"{self.nombre}: turno {self.turno}, M={self.madera}, A={self.arcilla}, "
                f"T={self.trigo}, Carr={self.carreteras}, Chz={self.chozas}, Pts={self.puntos}")


# PREPARACIÓN DEL MAPA

# PARÁMETROS DE LA PARTIDA
with open("parametros.json", "rb") as file:
    dict_param = json.load(file)

# CREAMOS JUGADORES
jugadores = []
for i in range(dict_param["CANTIDAD_JUGADORES_PARTIDA"]):
    jugador = Jugador(fake.user_name())
    jugadores.append(jugador)

# CREAMOS EL MAPA
ruta_grafo = "grafo.json"
ruta_parametros = "parametros.json"
mapa = Mapa(ruta_grafo, ruta_parametros, jugadores)
# print(jugadores)
# mapa.lanzamiento_dados(jugadores[0])
# print(jugadores)
# accion = mapa.construir_carretera(jugadores[0], mapa.lista_nodos[0], mapa.lista_nodos[20])
# print(accion)
# print(jugadores)
# print(mapa.nodos_usados)
# print(mapa.lista_carreteras)
# accion = mapa.construir_carretera(jugadores[0], mapa.lista_nodos[13], mapa.lista_nodos[8])
# print(accion)
# print(jugadores)
# print(mapa.nodos_usados)
# print(mapa.lista_carreteras)
# accion = mapa.construir_carretera(jugadores[1], mapa.lista_nodos[3], mapa.lista_nodos[2])
# print(accion)
# print(jugadores)
# print(mapa.nodos_usados)
# print(mapa.lista_carreteras)
# accion = mapa.construir_choza(jugadores[1], mapa.lista_nodos[2])
# print(accion)
# print(jugadores)
# print(mapa.nodos_usados)
# print(mapa.lista_carreteras)

# NETWORKING
if __name__ == "__main__":
    port = dict_param["port"]
    host = dict_param["host"]

    server = Server(port, host)
