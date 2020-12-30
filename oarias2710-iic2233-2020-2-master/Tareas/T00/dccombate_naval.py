# Este archivo ejecuta el juego DCCombate Naval completo
import os
import random

from tablero import print_tablero
from parametros import NUM_BARCOS
from parametros import RADIO_EXP

from funciones import puntaje
from funciones import respuesta_valida
from funciones import respuesta_valida_letra
from funciones import lanzar_bomba
from funciones import lanzar_bomba_regular
from funciones import dimensiones_tablero
from funciones import crea_tableros

# Archivo donde se guardan los puntajes
archivo_puntajes = "puntajes.txt"

condicion_menu_inicio = True
salida_desde_menu_juego = False
salida_desde_apodo = False

while condicion_menu_inicio is True:
    # Presenta el menú de inicio del juego
    print("\n" + '*' * 5, "Menú de Inicio", '*' * 5, "\n")
    print("Seleciona una opción:", "\n")
    print("[0] Iniciar una Partida")
    print("[1] Ver Ranking de Puntajes")
    print("[2] Salir", "\n")
    resp_menu_inicio = respuesta_valida(2)

    if resp_menu_inicio == 0:
        # AQUI EMPIEZA EL CÓDIGO DEL MENU DE JUEGO
        # nombre = apodo_valido()
        apodo = ""
        cond = False
        while cond is False:
            apodo = input("Ingresa un apodo (al menos 5 letras y/o números): ")
            if len(apodo) < 5 or apodo.isalnum() is False:
                print("Apodo debe tener al menos 5 letras y/o números")
                print("¿Deseas intentarlo de nuevo o volver al Menú de Inicio?" + "\n")
                print("[0] Ingresar apodo ")
                print("[1] Volver al Menú de Inicio", "\n")
                resp_apodo = respuesta_valida(1)
                if resp_apodo == 1:
                    salida_desde_apodo = True
                    break
            elif len(apodo) >= 5 and apodo.isalnum() is True:
                cond = True
        if salida_desde_apodo is False:
            dimensiones = dimensiones_tablero()
            N = dimensiones[0]
            M = dimensiones[1]
            print(f"Tu apodo es {apodo} y elegiste un tablero de {N} filas por {M} columnas")
            tableros = crea_tableros(N, M)
            col_posibles = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
            esp_cruz = 0
            esp_x = 0
            esp_diamante = 0
            coord_jugador = []
            coord_oponente = []
            barcos_jugador = NUM_BARCOS
            barcos_oponente = NUM_BARCOS

            condicion_menu_juego = False
            while condicion_menu_juego is False:
                print("\n" + '*' * 5, "Menú de Juego", '*' * 5, "\n")
                print_tablero(tableros[0], tableros[1])
                print("\n" + "[0] Rendirse")
                print("[1] Lanzar una bomba")
                print("[2] Salir del programa" + "\n")
                resp_partida = respuesta_valida(2)

                condicion_partida = False
                while condicion_partida is False:
                    if resp_partida == 0:
                        condicion_partida = True
                    elif resp_partida == 1:
                        condicion_turno_jugador = False
                        while condicion_turno_jugador is False:
                            # Juega el usuario
                            resultado_jugador = lanzar_bomba(tableros[0], coord_jugador,
                                                             esp_cruz, esp_x, esp_diamante)
                            coord_jugador.append(resultado_jugador[0])
                            esp_cruz += resultado_jugador[2]
                            esp_x += resultado_jugador[3]
                            esp_diamante += resultado_jugador[4]
                            if resultado_jugador[5] > 0:
                                barcos_oponente = barcos_oponente - resultado_jugador[5]
                                if barcos_oponente == 0:
                                    condicion_turno_jugador = True
                                    print_tablero(tableros[0], tableros[1])
                                    break
                                print("\n" + "¡Diste en el blanco! Tienes otro disparo")
                                print_tablero(tableros[0], tableros[1])
                            elif resultado_jugador[5] == 0:
                                condicion_turno_jugador = True
                        if barcos_oponente > 0:
                            condicion_turno_oponente = False
                        elif barcos_oponente == 0:
                            condicion_turno_oponente = True
                        while condicion_turno_oponente is False:
                            # Juega el programa
                            resultado_oponente = lanzar_bomba_regular(tableros[1], coord_oponente)
                            coord_oponente.append(resultado_oponente[0])
                            disparo_oponente = str(resultado_oponente[0][0]) + \
                                col_posibles[resultado_oponente[0][1]]
                            string_corto = "** ¡Tu oponente disparó a la coordenada "
                            print("\n" + string_corto + f"{disparo_oponente}!" + "\n")
                            if resultado_oponente[2] > 0:
                                barcos_jugador = barcos_jugador - resultado_oponente[2]
                                if barcos_jugador == 0:
                                    condicion_turno_oponente = True
                                    print_tablero(tableros[0], tableros[1])
                                    break
                                print("** ¡Tu oponente dio en el blanco! Tiene un nuevo disparo")
                            elif resultado_oponente[2] == 0:
                                condicion_turno_oponente = True
                        print(f"** Jugador tiene {barcos_jugador} barcos")
                        print(f"** Oponente tiene {barcos_oponente} barcos")
                        condicion_partida = True
                    elif resp_partida == 2:
                        print("\n" + "Saliendo del juego...")
                        print("¡Hasta la próxima!" + "\n")
                        condicion_partida = True

                enemigos_descubiertos = NUM_BARCOS - barcos_oponente
                aliados_descubiertos = NUM_BARCOS - barcos_jugador
                delta_descubiertos = enemigos_descubiertos - aliados_descubiertos
                formula = N * M * NUM_BARCOS * delta_descubiertos
                puntaje_jugador = max(0, formula)

                if resp_partida == 0:
                    print("¡Te rendiste!")
                    print("Volverás al Menú de Inicio")
                    print("\n" + f"Puntaje de {apodo}: {puntaje_jugador}")
                    # copiar el puntaje en el archivo
                    puntajes = open(archivo_puntajes, "a")
                    puntajes.write("\n" + apodo + "," + str(puntaje_jugador))
                    puntajes.close()
                    condicion_menu_juego = True
                elif resp_partida == 1:
                    if barcos_jugador == 0:
                        print("Lo siento, ha ganado tu Oponente")
                        print("\n" + f"Puntaje de {apodo}: {puntaje_jugador}")
                        # copiar el puntaje en el archivo
                        puntajes = open(archivo_puntajes, "a")
                        puntajes.write("\n" + apodo + "," + str(puntaje_jugador))
                        puntajes.close()
                        condicion_menu_juego = True
                    elif barcos_oponente == 0:
                        print("¡Felicitaciones, ganaste!")
                        print("\n" + f"Puntaje de {apodo}: {puntaje_jugador}")
                        # copiar el puntaje en el archivo
                        puntajes = open(archivo_puntajes, "a")
                        puntajes.write("\n" + apodo + "," + str(puntaje_jugador))
                        puntajes.close()
                        condicion_menu_juego = True
                elif resp_partida == 2:
                    condicion_menu_juego = True
                    salida_desde_menu_juego = True
            # AQUI TERMINA EL CODIGO DEL MENU DE JUEGO

    elif resp_menu_inicio == 1:
        puntajes = open(archivo_puntajes, "rt")
        lista_puntajes = puntajes.readlines()
        puntajes.close()
        lista_nueva = []
        for elemento in lista_puntajes:
            elemento2 = elemento.strip("\n").split(",")
            lista_nueva.append(elemento2)
        lista_nueva.sort(reverse=True, key=puntaje)
        print("\n" + '*' * 5, "Ranking de Puntajes", '*' * 5, "\n")
        if len(lista_nueva) >= 5:
            for i in range(5):
                print(f"{i + 1}) {lista_nueva[i][0]}: {lista_nueva[i][1]} Pts")
            print("\n")
            print("[0] Volver", "\n")
            resp_menu_inicio = respuesta_valida(0)
        elif len(lista_nueva) > 0 and len(lista_nueva) < 5:
            for i in range(len(lista_nueva)):
                print(f"{i + 1}) {lista_nueva[i][0]}: {lista_nueva[i][1]} Pts")
            print("\n")
            print("[0] Volver", "\n")
            resp_menu_inicio = respuesta_valida(0)
        elif len(lista_nueva) == 0:
            print("No existen puntajes registrados.")
            print("Volviendo al Menú de Inicio...")
            resp_menu_inicio = 0
    elif resp_menu_inicio == 2:
        print("\n" + "Saliendo del juego...")
        print("¡Hasta la próxima!" + "\n")
        condicion_menu_inicio = False
    if salida_desde_menu_juego is True:
        condicion_menu_inicio = False
