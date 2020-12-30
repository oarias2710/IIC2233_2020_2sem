import os
import random
from entidades import DelegacionIEEEsparta, DelegacionDCCrotona, Deportista
from deportes import DeporteAtletismo, DeporteCiclismo, DeporteGimnasia, DeporteNatacion
from campeonato import Campeonato

# Archivo donde se guardan los deportistas
archivo = os.path.join("Tareas", "T01", "deportistas.csv")

archivo_depor = open(archivo, "rt")
lista = archivo_depor.readlines()
archivo_depor.close()
base_deportistas = []
for elemento in lista:
    elemento2 = elemento.strip("\n").split(",")
    base_deportistas.append(elemento2)

# Archivo donde se guardan las delegaciones
archivo = os.path.join("Tareas", "T01", "delegaciones.csv")

archivo_deleg = open(archivo, "rt")
lista = archivo_deleg.readlines()
archivo_deleg.close()
base_delegaciones = []
for elemento in lista:
    elemento2 = elemento.strip("\n").split(",")
    base_delegaciones.append(elemento2)
for elemento in base_delegaciones:
    lista = elemento[2].strip("\n").split(";")
    elemento.pop(2)
    elemento.insert(2, lista)

# Generamos las instacias de la clase deportistas y
# los guardamos en una lista.
# nombre, velo, resistencia, flexi, moral, lesionado, precio
# nombre,flexibilidad,moral,precio,velocidad,lesionado,resistencia
deportistas = []
base_deportistas2 = base_deportistas[1:]
for elem in base_deportistas2:
    nombre = elem[0]
    velo = int(elem[4])
    resistencia = int(elem[6])
    flexi = int(elem[1])
    moral = int(elem[2])
    lesionado = elem[5]
    precio = int(elem[3])
    instancia = Deportista(nombre, velo, resistencia, flexi, moral, lesionado, precio)
    deportistas.append(instancia)

# Una lista que identifica a los deportistas que están en una delegación
deportistas_usados = []

deportistas_ieee = []
contador = 0
for elem in deportistas:
    if elem.nombre in base_delegaciones[1][2]:
        deportistas_ieee.append(elem)
        deportistas_usados.append(contador)
    contador += 1

deportistas_dcc = []
contador = 0
for elem in deportistas:
    if elem.nombre in base_delegaciones[2][2]:
        deportistas_dcc.append(elem)
        deportistas_usados.append(contador)
    contador += 1

print(deportistas_usados)


# Generamos las delegaciones
# entrenador, equipo, medallas, dinero

# random.seed(666)
ieee = DelegacionIEEEsparta("Jorge Sampaoli",
                            deportistas_ieee,
                            int(base_delegaciones[1][-2]),
                            int(base_delegaciones[1][-1]))
dcc = DelegacionDCCrotona("Miguel Angel Russo",
                          deportistas_dcc,
                          int(base_delegaciones[2][-2]),
                          int(base_delegaciones[2][-1]))
print("IEEE:", ieee.moral, ieee.hab_especial_usadas,
      ieee.exce_respeto, ieee.imp_medicos, ieee.imp_deportivos)
print("DCC:", dcc.moral, dcc.hab_especial_usadas,
      dcc.exce_respeto, dcc.imp_medicos, dcc.imp_deportivos)

# Clase DelegacionIEEEsparta

# inicializacion
print(f"\nLa delegación IEEE es entrenada por {ieee.entrenador}.")
print(f"Tiene {len(ieee.equipo)} deportistas.")
print(f"Incluyendo a {ieee.equipo[0].nombre} y a {ieee.equipo[1].nombre}.")
print(f"Tiene {ieee.medallas} medallas y {ieee.dinero} dcc coins.")
print(f"Excelencia-respeto = {ieee.exce_respeto}.")
print(f"Implementos médicos = {ieee.imp_medicos}.")
print(f"Implementos deportivos = {ieee.imp_deportivos}.")
print(f"La moral de la delegación es {ieee.moral}.")
print(f"Ha usado {ieee.hab_especial_usadas} habilidad especial.")

# fichar deportista
print(ieee.dinero)
ieee.fichar_deportista(deportistas[0])
print(ieee.dinero)
ieee.fichar_deportista(deportistas[2])
print(ieee.dinero)
ieee.fichar_deportista(deportistas[4])
print(ieee.dinero)
ieee.fichar_deportista(deportistas[6])
print(ieee.dinero)

# sanar_lesiones
ieee.dinero = int(base_delegaciones[1][-1])
for elem in ieee.equipo:
    print(elem.nombre, elem.lesionado)
print(ieee.dinero)
ieee.sanar_lesiones(ieee.equipo[7])
print(ieee.dinero)
print(ieee.equipo[7].nombre, ieee.equipo[7].lesionado)
ieee.sanar_lesiones(ieee.equipo[7])
print(ieee.dinero)
print(ieee.equipo[7].nombre, ieee.equipo[7].lesionado)

# comprar_tecnologia
# ieee.dinero = 10
print("\n**********************************************")
print("*****  IEEE prueba comprar_tecnologia()  *****")
print("**********************************************\n")
print(ieee.dinero)
print(f"Implementos médicos = {ieee.imp_medicos}.")
print(f"Implementos deportivos = {ieee.imp_deportivos}.")
ieee.comprar_tecnologia()
print(ieee.dinero)
print(f"Implementos médicos = {ieee.imp_medicos}.")
print(f"Implementos deportivos = {ieee.imp_deportivos}.")

# entrenar deportista
print("\n***********************************************")
print("*****  IEEE prueba entrenar_deportista()  *****")
print("***********************************************\n")
print(f"Entrenar velocidad: {ieee.dinero} dinero disponible")
print(f"Deportista {ieee.equipo[0].nombre}")
vel_ini = ieee.equipo[0].velocidad
mor_ini = ieee.equipo[0].moral
# aumento = vel_ini + (vel_ini ** (1 / 3)) * 1.7
# print(f"Aumento esperado: {aumento}")
print(f"Antes de entrenamiento: VEL {ieee.equipo[0].velocidad} MORAL {ieee.equipo[0].moral}")
ieee.entrenar_deportista(ieee.equipo[0], "velocidad")
print(f"\nPosterior entrenamiento: {ieee.dinero} dinero disponible")
print(f"Post entrenamiento: VEL {ieee.equipo[0].velocidad} MORAL {ieee.equipo[0].moral}")
vel_fin = ieee.equipo[0].velocidad
mor_fin = ieee.equipo[0].moral
print(f"cambio: VEL {(vel_fin - vel_ini) * 100 / vel_ini}% MORAL {mor_fin - mor_ini} unid.")

print(f"\nEntrenar resistencia: {ieee.dinero} dinero disponible")
print(f"Deportista {ieee.equipo[0].nombre}")
res_ini = ieee.equipo[0].resistencia
mor_ini = ieee.equipo[0].moral
# aumento = res_ini + (res_ini ** (1 / 3)) * 1.7
# print(f"Aumento esperado: {aumento}")
print(f"Antes de entrenamiento: RES {ieee.equipo[0].resistencia} MORAL {ieee.equipo[0].moral}")
ieee.entrenar_deportista(ieee.equipo[0], "resistencia")
print(f"\nPosterior entrenamiento: {ieee.dinero} dinero disponible")
print(f"Post entrenamiento: RES {ieee.equipo[0].resistencia} MORAL {ieee.equipo[0].moral}")
res_fin = ieee.equipo[0].resistencia
mor_fin = ieee.equipo[0].moral
print(f"cambio: RES {(res_fin - res_ini) * 100 / res_ini}% MORAL {mor_fin - mor_ini} unid.")

print(f"\nEntrenar flexibilidad: {ieee.dinero} dinero disponible")
print(f"Deportista {ieee.equipo[0].nombre}")
fle_ini = ieee.equipo[0].flexibilidad
mor_ini = ieee.equipo[0].moral
# aumento = fle_ini + (fle_ini ** (1 / 3)) * 1.7
# print(f"Aumento esperado: {aumento}")
print(f"Antes de entrenamiento: FLE {ieee.equipo[0].flexibilidad} MORAL {ieee.equipo[0].moral}")
ieee.entrenar_deportista(ieee.equipo[0], "flexibilidad")
print(f"\nPosterior entrenamiento: {ieee.dinero} dinero disponible")
print(f"Post entrenamiento: FLE {ieee.equipo[0].flexibilidad} MORAl {ieee.equipo[0].moral}")
fle_fin = ieee.equipo[0].flexibilidad
mor_fin = ieee.equipo[0].moral
print(f"cambio: FLE {(fle_fin - fle_ini) * 100 / fle_ini}% MORAL {mor_fin - mor_ini} unid.")

# usar habilidad n_hab_especial
print("\n**********************************************")
print("*****  IEEE prueba utilizar_habilidad()  *****")
print("**********************************************\n")
print(f"IEEE tiene {ieee.dinero} dinero y ha usado {ieee.hab_especial_usadas} hab. especial")
for elem in ieee.equipo:
    print(f"{elem.nombre} tiene moral {elem.moral}.")
ieee.utilizar_habilidad()
print(f"\nIEEE tiene {ieee.dinero} dinero y ha usado {ieee.hab_especial_usadas} hab. especial")
for elem in ieee.equipo:
    print(f"{elem.nombre} tiene moral {elem.moral}.")

# Clase DelegacionDCCrotona

# inicializacion
print(f"\nLa delegación DCC es entrenada por {dcc.entrenador}.")
print(f"Tiene {len(dcc.equipo)} deportistas.")
print(f"Incluyendo a {dcc.equipo[0].nombre} y a {dcc.equipo[1].nombre}.")
print(f"Tiene {dcc.medallas} medallas y {dcc.dinero} dcc coins.")
print(f"Excelencia-respeto = {dcc.exce_respeto}.")
print(f"Implementos médicos = {dcc.imp_medicos}.")
print(f"Implementos deportivos = {dcc.imp_deportivos}.")
print(f"La moral de la delegación es {dcc.moral}.")
print(f"Ha usado {dcc.hab_especial_usadas} habilidad especial.")

# fichar deportista
print(dcc.dinero)
dcc.fichar_deportista(deportistas[46])
print(dcc.dinero)
dcc.fichar_deportista(deportistas[2])
print(dcc.dinero)
dcc.fichar_deportista(deportistas[4])
print(dcc.dinero)
dcc.fichar_deportista(deportistas[6])
print(dcc.dinero)
dcc.fichar_deportista(deportistas[8])
print(dcc.dinero)

# sanar_lesiones
dcc.dinero = int(base_delegaciones[2][-1])
for elem in dcc.equipo:
    print(elem.nombre, elem.lesionado)
print(dcc.dinero)
dcc.sanar_lesiones(dcc.equipo[5])
print(dcc.dinero)
print(dcc.equipo[5].nombre, dcc.equipo[5].lesionado)
dcc.sanar_lesiones(dcc.equipo[5])
print(dcc.dinero)
print(dcc.equipo[5].nombre, dcc.equipo[5].lesionado)

# comprar_tecnologia
print("\n*********************************************")
print("*****  DCC prueba comprar_tecnologia()  *****")
print("*********************************************\n")
print(dcc.dinero)
print(f"Implementos médicos = {dcc.imp_medicos}.")
print(f"Implementos deportivos = {dcc.imp_deportivos}.")
dcc.comprar_tecnologia()
print(dcc.dinero)
print(f"Implementos médicos = {dcc.imp_medicos}.")
print(f"Implementos deportivos = {dcc.imp_deportivos}.")

# entrenar deportista
print("\n**********************************************")
print("*****  DCC prueba entrenar_deportista()  *****")
print("**********************************************\n")
print(f"Entrenar velocidad: {dcc.dinero} dinero disponible")
print(f"Deportista {dcc.equipo[0].nombre}")
vel_ini = dcc.equipo[0].velocidad
mor_ini = dcc.equipo[0].moral
# aumento = vel_ini + (vel_ini ** (1 / 3))
# print(f"Aumento esperado: {aumento}")
print(f"Antes de entrenamiento: VEL {dcc.equipo[0].velocidad} MORAL {dcc.equipo[0].moral}")
dcc.entrenar_deportista(dcc.equipo[0], "velocidad")
print(f"\nPosterior entrenamiento: {dcc.dinero} dinero disponible")
print(f"Post entrenamiento: VEL {dcc.equipo[0].velocidad} MORAL {dcc.equipo[0].moral}")
vel_fin = dcc.equipo[0].velocidad
mor_fin = dcc.equipo[0].moral
print(f"cambio: VEL {(vel_fin - vel_ini) * 100 / vel_ini}% MORAL {mor_fin - mor_ini} unid.")

print(f"\nEntrenar resistencia: {dcc.dinero} dinero disponible")
print(f"Deportista {dcc.equipo[0].nombre}")
res_ini = dcc.equipo[0].resistencia
mor_ini = dcc.equipo[0].moral
# aumento = res_ini + (res_ini ** (1 / 3))
# print(f"Aumento esperado: {aumento}")
print(f"Antes de entrenamiento: RES {dcc.equipo[0].resistencia} MORAL {dcc.equipo[0].moral}")
dcc.entrenar_deportista(dcc.equipo[0], "resistencia")
print(f"\nPosterior entrenamiento: {dcc.dinero} dinero disponible")
print(f"Post entrenamiento: RES {dcc.equipo[0].resistencia} MORAL {dcc.equipo[0].moral}")
res_fin = dcc.equipo[0].resistencia
mor_fin = dcc.equipo[0].moral
print(f"cambio: RES {(res_fin - res_ini) * 100 / res_ini}% MORAL {mor_fin - mor_ini} unid.")

print(f"\nEntrenar flexibilidad: {dcc.dinero} dinero disponible")
print(f"Deportista {dcc.equipo[0].nombre}")
fle_ini = dcc.equipo[0].flexibilidad
mor_ini = dcc.equipo[0].moral
# aumento = fle_ini + (fle_ini ** (1 / 3))
# print(f"Aumento esperado: {aumento}")
print(f"Antes de entrenamiento: FLE {dcc.equipo[0].flexibilidad} MORAL {dcc.equipo[0].moral}")
dcc.entrenar_deportista(dcc.equipo[0], "flexibilidad")
print(f"\nPosterior entrenamiento: {dcc.dinero} dinero disponible")
print(f"Post entrenamiento: FLE {dcc.equipo[0].flexibilidad} MORAl {dcc.equipo[0].moral}")
fle_fin = dcc.equipo[0].flexibilidad
mor_fin = dcc.equipo[0].moral
print(f"cambio: FLE {(fle_fin - fle_ini) * 100 / fle_ini}% MORAL {mor_fin - mor_ini} unid.")

# usar habilidad n_hab_especial
# PENDIENTE

# Clase Deportista

# inicialización
print("\n***********************************")
print("*****  __INIT__() DEPORTISTAS *****")
print("***********************************\n")
print(f"Nombre = {deportistas[44].nombre}")
print(f"Velocidad = {deportistas[44].velocidad}")
print(f"Resistencia = {deportistas[44].resistencia}")
print(f"Flexibilidad = {deportistas[44].flexibilidad}")
print(f"Moral = {deportistas[44].moral}")
print(f"Lesionado = {deportistas[44].lesionado}")
print(f"Precio = {deportistas[44].precio}")

deportistas[44].velocidad += 35
print(f"\nVelocidad = {deportistas[44].velocidad}")
deportistas[44].velocidad += 300
print(f"Velocidad = {deportistas[44].velocidad}")

deportistas[44].resistencia += 68
print(f"\nResistencia = {deportistas[44].resistencia}")
deportistas[44].resistencia += 300
print(f"Resistencia = {deportistas[44].resistencia}")

deportistas[44].flexibilidad += 52
print(f"\nFlexibilidad = {deportistas[44].flexibilidad}")
deportistas[44].flexibilidad += 300
print(f"Flexibilidad = {deportistas[44].flexibilidad}")

# entrenar dcc
# entrenar ieee
# los probamos más arriba, se usa este método en la clase delegación

# lesionarse
# la probamos más adelante

# Clases de deportes
print("\n***********************************")
print("*****  PROBANDO COMPETENCIAS  *****")
print("***********************************\n")

# # Clase DeporteXXXXX
# # inicializacion y calcular ganador
atletismo = DeporteAtletismo(ieee, dcc)
ciclismo = DeporteCiclismo(ieee, dcc)
gimnasia = DeporteGimnasia(ieee, dcc)
natacion = DeporteNatacion(ieee, dcc)

dupla1 = [ieee.equipo[0], dcc.equipo[5]]
dupla2 = [ieee.equipo[0], dcc.equipo[5]]
dupla3 = [ieee.equipo[0], dcc.equipo[5]]
dupla4 = [ieee.equipo[0], dcc.equipo[5]]

campeonato = Campeonato(1, atletismo, ciclismo, gimnasia, natacion, ieee, dcc)
campeonato.mostrar_estado()
resultados = campeonato.realizar_competencias(dupla1, dupla2, dupla3, dupla4, ieee, dcc)
campeonato.premiar(resultados[0], resultados[1], resultados[2])
campeonato.calcular_moral()
campeonato.mostrar_estado()
