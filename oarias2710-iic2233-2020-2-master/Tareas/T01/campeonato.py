# en esta clase hay que poner la lista de jugadores que
# están siendo usados y no pueden ser fichados.

import os
from deportes import DeporteAtletismo, DeporteCiclismo, DeporteGimnasia, DeporteNatacion
from beautifultable import BeautifulTable


class Campeonato:
    def __init__(self, dia_actual,
                 atletismo, ciclismo, gimnasia, natacion,
                 delegacion1, delegacion2):
        self.dia_actual = dia_actual  # int
        self.medallero = {delegacion1.delegacion: 0,
                          delegacion2.delegacion: 0}  # dict
        self.medallero1 = {"atletismo1": 0,
                           "ciclismo1": 0,
                           "gimnasia1": 0,
                           "natacion1": 0}
        self.medallero2 = {"atletismo2": 0,
                           "ciclismo2": 0,
                           "gimnasia2": 0,
                           "natacion2": 0}
        self.atletismo = atletismo  # objeto de la clase DeporteAtletismo
        self.ciclismo = ciclismo  # objeto de la clase DeporteCiclismo
        self.gimnasia = gimnasia  # objeto de la clase DeporteGimnasia
        self.natacion = natacion  # objeto de la clase DeporteNatacion
        self.delegacion1 = delegacion1
        self.delegacion2 = delegacion2

        # Creamos archivo resultados.txt
        archivo = os.path.join("Tareas", "T01", "resultados.txt")
        archivo_resultados = open(archivo, "wt")
        archivo_resultados.write("**************************************************\n")
        archivo_resultados.write("****  RESULTADOS DÍA A DÍA DCCUMBRE OLÍMPICA  ****\n")
        archivo_resultados.write("**************************************************\n")
        archivo_resultados.close()

    def realizar_competencias(self, dupla1, dupla2, dupla3, dupla4, delegacion1, delegacion2):
        resultados = []
        ganadores = []
        perdedores = []
        # atletismo
        validez = self.atletismo.validez_competencia(dupla1[0], delegacion1,
                                                     dupla1[1], delegacion2)
        if validez == (False, False):
            resultados.append("Empate")
            ganadores.append("-")
            perdedores.append("-")
        elif validez == (False, delegacion1):
            resultados.append(delegacion1.delegacion)
            ganadores.append(dupla1[0].nombre)
            perdedores.append(dupla1[1].nombre)
        elif validez == (False, delegacion2):
            resultados.append(delegacion2.delegacion)
            ganadores.append(dupla1[1].nombre)
            perdedores.append(dupla1[0].nombre)
        elif validez is True:
            ganador = self.atletismo.calcular_ganador(dupla1[0], dupla1[1])
            if ganador == dupla1[0]:
                resultados.append(delegacion1.delegacion)
                ganadores.append(dupla1[0].nombre)
                perdedores.append(dupla1[1].nombre)
            elif ganador == dupla1[1]:
                resultados.append(delegacion2.delegacion)
                ganadores.append(dupla1[1].nombre)
                perdedores.append(dupla1[0].nombre)
            elif ganador is None:
                resultados.append("Empate")
                ganadores.append("-")
                perdedores.append("-")

        # ciclismo
        validez = self.ciclismo.validez_competencia(dupla2[0], delegacion1,
                                                    dupla2[1], delegacion2)
        if validez == (False, False):
            resultados.append("Empate")
            ganadores.append("-")
            perdedores.append("-")
        elif validez == (False, delegacion1):
            resultados.append(delegacion1.delegacion)
            ganadores.append(dupla2[0].nombre)
            perdedores.append(dupla2[1].nombre)
        elif validez == (False, delegacion2):
            resultados.append(delegacion2.delegacion)
            ganadores.append(dupla2[1].nombre)
            perdedores.append(dupla2[0].nombre)
        elif validez is True:
            ganador = self.ciclismo.calcular_ganador(dupla2[0], dupla2[1])
            if ganador == dupla2[0]:
                resultados.append(delegacion1.delegacion)
                ganadores.append(dupla2[0].nombre)
                perdedores.append(dupla2[1].nombre)
            elif ganador == dupla2[1]:
                resultados.append(delegacion2.delegacion)
                ganadores.append(dupla2[1].nombre)
                perdedores.append(dupla2[0].nombre)
            elif ganador is None:
                resultados.append("Empate")
                ganadores.append("-")
                perdedores.append("-")

        # gimnasia
        validez = self.gimnasia.validez_competencia(dupla3[0], delegacion1,
                                                    dupla3[1], delegacion2)
        if validez == (False, False):
            resultados.append("Empate")
            ganadores.append("-")
            perdedores.append("-")
        elif validez == (False, delegacion1):
            resultados.append(delegacion1.delegacion)
            ganadores.append(dupla3[0].nombre)
            perdedores.append(dupla3[1].nombre)
        elif validez == (False, delegacion2):
            resultados.append(delegacion2.delegacion)
            ganadores.append(dupla3[1].nombre)
            perdedores.append(dupla3[0].nombre)
        elif validez is True:
            ganador = self.gimnasia.calcular_ganador(dupla3[0], dupla3[1])
            if ganador == dupla3[0]:
                resultados.append(delegacion1.delegacion)
                ganadores.append(dupla3[0].nombre)
                perdedores.append(dupla3[1].nombre)
            elif ganador == dupla3[1]:
                resultados.append(delegacion2.delegacion)
                ganadores.append(dupla3[1].nombre)
                perdedores.append(dupla3[0].nombre)
            elif ganador is None:
                resultados.append("Empate")
                ganadores.append("-")
                perdedores.append("-")

        # natación
        validez = self.natacion.validez_competencia(dupla4[0], delegacion1,
                                                    dupla4[1], delegacion2)
        if validez == (False, False):
            resultados.append("Empate")
            ganadores.append("-")
            perdedores.append("-")
        elif validez == (False, delegacion1):
            resultados.append(delegacion1.delegacion)
            ganadores.append(dupla4[0].nombre)
            perdedores.append(dupla4[1].nombre)
        elif validez == (False, delegacion2):
            resultados.append(delegacion2.delegacion)
            ganadores.append(dupla4[1].nombre)
            perdedores.append(dupla4[0].nombre)
        elif validez is True:
            ganador = self.natacion.calcular_ganador(dupla4[0], dupla4[1])
            if ganador == dupla4[0]:
                resultados.append(delegacion1.delegacion)
                ganadores.append(dupla4[0].nombre)
                perdedores.append(dupla4[1].nombre)
            elif ganador == dupla4[1]:
                resultados.append(delegacion2.delegacion)
                ganadores.append(dupla4[1].nombre)
                perdedores.append(dupla4[0].nombre)
            elif ganador is None:
                resultados.append("Empate")
                ganadores.append("-")
                perdedores.append("-")

        archivo = os.path.join("Tareas", "T01", "resultados.txt")
        archivo_resultados = open(archivo, "at")
        archivo_resultados.write(f"\nDía {self.dia_actual}:\n")
        archivo_resultados.write("\nCompetencia: Atletismo\n")
        archivo_resultados.write(f"Delegación Ganadora: {resultados[0]}\n")
        archivo_resultados.write(f"Deportista Ganador(a): {ganadores[0]}\n")
        archivo_resultados.write("\nCompetencia: Ciclismo\n")
        archivo_resultados.write(f"Delegación Ganadora: {resultados[1]}\n")
        archivo_resultados.write(f"Deportista Ganador(a): {ganadores[1]}\n")
        archivo_resultados.write("\nCompetencia: Gimnasia\n")
        archivo_resultados.write(f"Delegación Ganadora: {resultados[2]}\n")
        archivo_resultados.write(f"Deportista Ganador(a): {ganadores[2]}\n")
        archivo_resultados.write("\nCompetencia: Natación\n")
        archivo_resultados.write(f"Delegación Ganadora: {resultados[3]}\n")
        archivo_resultados.write(f"Deportista Ganador(a): {ganadores[3]}\n")
        archivo_resultados.write("\n**************************************************\n")
        archivo_resultados.close()
        self.dia_actual += 1
        return resultados, ganadores, perdedores

    def premiar(self, resultados, ganadores, perdedores):
        # premios delegaciones
        if resultados[0] == self.delegacion1.delegacion:
            self.medallero[self.delegacion1.delegacion] += 1
            self.medallero1["atletismo1"] += 1
            self.delegacion1.dinero += 100
        elif resultados[0] == self.delegacion2.delegacion:
            self.medallero[self.delegacion2.delegacion] += 1
            self.medallero2["atletismo2"] += 1
            self.delegacion2.dinero += 100

        if resultados[1] == self.delegacion1.delegacion:
            self.medallero[self.delegacion1.delegacion] += 1
            self.medallero1["ciclismo1"] += 1
            self.delegacion1.dinero += 100
        elif resultados[1] == self.delegacion2.delegacion:
            self.medallero[self.delegacion2.delegacion] += 1
            self.medallero2["ciclismo2"] += 1
            self.delegacion2.dinero += 100

        if resultados[2] == self.delegacion1.delegacion:
            self.medallero[self.delegacion1.delegacion] += 1
            self.medallero1["gimnasia1"] += 1
            self.delegacion1.dinero += 100
        elif resultados[2] == self.delegacion2.delegacion:
            self.medallero[self.delegacion2.delegacion] += 1
            self.medallero2["gimnasia2"] += 1
            self.delegacion2.dinero += 100

        if resultados[3] == self.delegacion1.delegacion:
            self.medallero[self.delegacion1.delegacion] += 1
            self.medallero1["natacion1"] += 1
            self.delegacion1.dinero += 100
        elif resultados[3] == self.delegacion2.delegacion:
            self.medallero[self.delegacion2.delegacion] += 1
            self.medallero2["natacion2"] += 1
            self.delegacion2.dinero += 100

        # bonus y penalizaciones deportistas ganadores
        for elem in self.delegacion1.equipo:
            if elem.nombre in ganadores:
                elem.moral += 20
            if elem.nombre in perdedores:
                elem.moral -= 10
                self.delegacion1.exce_respeto -= 0.02

        for elem in self.delegacion2.equipo:
            if elem.nombre in ganadores:
                elem.moral += 20
            if elem.nombre in perdedores:
                elem.moral -= 10
                self.delegacion2.exce_respeto -= 0.02

    def calcular_moral(self):
        len_equipo = len(self.delegacion1.equipo)
        sumatoria = 0
        for deportista in self.delegacion1.equipo:
            sumatoria += deportista.moral
        self.delegacion1.moral = sumatoria / len_equipo  # float

        len_equipo = len(self.delegacion2.equipo)
        sumatoria = 0
        for deportista in self.delegacion2.equipo:
            sumatoria += deportista.moral
        self.delegacion2.moral = sumatoria / len_equipo  # float

    def mostrar_estado(self):
        print("\n****************************************************")
        print("****  ESTADO DE LAS DELEGACIONES Y DEPORTISTAS  ****")
        print("****************************************************\n")
        print(self.delegacion1.delegacion)
        print(f"Entrenador: {self.delegacion1.entrenador}")
        print(f"Moral del equipo: {round(self.delegacion1.moral, 2)}")
        print(f"Medallas: {self.medallero[self.delegacion1.delegacion]}")
        print(f"Dinero: {self.delegacion1.dinero}")

        print(f"\nExcelencia y respeto: {round(self.delegacion1.exce_respeto, 3)}")
        print(f"Implementos deportivos: {round(self.delegacion1.imp_deportivos, 3)}")
        print(f"Implementos médicos: {round(self.delegacion1.imp_medicos, 3)}\n")

        print("Equipo deportivo")
        table = BeautifulTable()
        for deportista in self.delegacion1.equipo:
            table.rows.append([deportista.nombre,
                               deportista.velocidad, deportista.resistencia,
                               deportista.flexibilidad, deportista.lesionado])
        table.columns.header = (["Nombre deportista", "Velocidad",
                                 "Resistencia", "Flexibilidad", "Lesión"])
        table.set_style(BeautifulTable.STYLE_COMPACT)
        table.columns.alignment['Nombre deportista'] = BeautifulTable.ALIGN_LEFT
        print(table)

        print("\n" + self.delegacion2.delegacion)
        print(f"Entrenador: {self.delegacion2.entrenador}")
        print(f"Moral del equipo: {round(self.delegacion2.moral, 2)}")
        print(f"Medallas: {self.medallero[self.delegacion2.delegacion]}")
        print(f"Dinero: {self.delegacion2.dinero}")

        print(f"\nExcelencia y respeto: {round(self.delegacion2.exce_respeto, 3)}")
        print(f"Implementos deportivos: {round(self.delegacion2.imp_deportivos, 3)}")
        print(f"Implementos médicos: {round(self.delegacion2.imp_medicos, 3)}\n")

        print("Equipo deportivo")
        table = BeautifulTable()
        for deportista in self.delegacion2.equipo:
            table.rows.append([deportista.nombre,
                               deportista.velocidad, deportista.resistencia,
                               deportista.flexibilidad, deportista.lesionado])
        table.columns.header = (["Nombre deportista", "Velocidad",
                                 "Resistencia", "Flexibilidad", "Lesión"])
        table.set_style(BeautifulTable.STYLE_COMPACT)
        table.columns.alignment['Nombre deportista'] = BeautifulTable.ALIGN_LEFT
        print(table)

        print("\n****************************************************")
        print(f"Día: {self.dia_actual}")
        print("\nMedallero")
        table = BeautifulTable()
        table.rows.append(["Atletismo", self.medallero1["atletismo1"],
                           self.medallero2["atletismo2"]])
        table.rows.append(["Ciclismo", self.medallero1["ciclismo1"], self.medallero2["ciclismo2"]])
        table.rows.append(["Gimnasia", self.medallero1["gimnasia1"], self.medallero2["gimnasia2"]])
        table.rows.append(["Natación", self.medallero1["natacion1"],
                           self.medallero2["natacion2"]])
        table.columns.header = (["Deporte", self.delegacion1.delegacion,
                                 self.delegacion2.delegacion])
        table.set_style(BeautifulTable.STYLE_COMPACT)
        table.columns.alignment['Deporte'] = BeautifulTable.ALIGN_LEFT
        print(table)
