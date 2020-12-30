from abc import ABC, abstractmethod
import parametros as p


class Deporte(ABC):  # LISTO
    def __init__(self, delegacion1, delegacion2):
        self.implemento = False  # bool
        self.riesgo = 0  # float

    def validez_competencia(self, jug1, delegacion1, jug2, delegacion2):
        if self.implemento is True:
            if jug1.lesionado is True and jug2.lesionado is True:
                print(f"{self.deporte}: Ambos jugadores están lesionados, no pueden competir")
                print(f"{self.deporte}: La competencia no es válida, se declara empate")
                return False, False
            elif (delegacion1.imp_deportivos < p.NIVEL_IMPLEMENTOS_COMPETIR
                  and delegacion2.imp_deportivos < p.NIVEL_IMPLEMENTOS_COMPETIR):
                print(f"{self.deporte}: Ambas delegaciones no tienen implementos",
                      "suficientes para competir")
                print(f"{self.deporte}: La competencia no es válida, se declara empate")
                return False, False
            elif jug1.lesionado is True and jug2.lesionado is False:
                print(f"{self.deporte}: Jugador {jug1.nombre} de {delegacion1.delegacion}",
                      "está lesionado, no puede competir")
                print(f"{self.deporte}: La competencia no es válida,",
                      f"victoria de {delegacion2.delegacion}")
                return False, delegacion2
            elif jug2.lesionado is True and jug1.lesionado is False:
                print(f"{self.deporte}: Jugador {jug2.nombre} de {delegacion2.delegacion}",
                      "está lesionado, no puede competir")
                print(f"{self.deporte}: La competencia no es válida,",
                      f"victoria de {delegacion1.delegacion}")
                return False, delegacion1
            elif (delegacion1.imp_deportivos < p.NIVEL_IMPLEMENTOS_COMPETIR
                  and delegacion2.imp_deportivos >= p.NIVEL_IMPLEMENTOS_COMPETIR):
                print(f"{self.deporte}: Equipo {delegacion1.delegacion} no tiene",
                      "implementos suficientes para competir")
                print(f"{self.deporte}: La competencia no es válida,",
                      f"victoria de {delegacion2.delegacion}")
                return False, delegacion2
            elif (delegacion2.imp_deportivos < p.NIVEL_IMPLEMENTOS_COMPETIR
                  and delegacion1.imp_deportivos >= p.NIVEL_IMPLEMENTOS_COMPETIR):
                print(f"{self.deporte}: Equipo {delegacion2.delegacion} no tiene",
                      "implementos suficientes para competir")
                print(f"{self.deporte}: La competencia no es válida,",
                      f"victoria de {delegacion1.delegacion}")
                return False, delegacion1
            else:
                print(f"{self.deporte}: La competencia es válida")
                return True
        elif self.implemento is False:
            if jug1.lesionado is True and jug2.lesionado is True:
                print(f"{self.deporte}: Ambos jugadores están lesionados, no pueden competir")
                print(f"{self.deporte}: La competencia no es válida, se declara empate")
                return False, False
            elif jug1.lesionado is True and jug2.lesionado is False:
                print(f"{self.deporte}: Jugador {jug1.nombre} de {delegacion1.delegacion}",
                      "está lesionado, no puede competir")
                print(f"{self.deporte}: La competencia no es válida,",
                      f"victoria de {delegacion2.delegacion}")
                return False, delegacion2
            elif jug2.lesionado is True and jug1.lesionado is False:
                print(f"{self.deporte}: Jugador {jug2.nombre} de {delegacion2.delegacion}",
                      "está lesionado, no puede competir")
                print(f"{self.deporte}: La competencia no es válida,",
                      f"victoria de {delegacion1.delegacion}")
                return False, delegacion1
            else:
                print(f"{self.deporte}: La competencia es válida")
                return True


class DeporteAtletismo(Deporte):  # LISTO
    def __init__(self, delegacion1, delegacion2):
        self.deporte = "Atletismo"
        self.delegacion1 = delegacion1
        self.delegacion2 = delegacion2
        self.implemento = p.IMP_ATLETISMO  # bool
        self.riesgo = p.RIESGO_ATLETISMO  # float

    def calcular_ganador(self, jug1, jug2):
        jug1.lesionarse(self.riesgo)
        jug2.lesionarse(self.riesgo)
        if jug1.lesionado is True and jug2.lesionado is True:
            print(f"{self.deporte}: Auch! Empate por lesión de ambos jugadores")
            return None
        elif jug1.lesionado is False and jug2.lesionado is True:
            print(f"{self.deporte}: {jug2.nombre} de la delegación",
                  f"{self.delegacion2.delegacion} se lesiona!")
            print(f"{self.deporte}: Gana {jug1.nombre}",
                  f"de la delegación {self.delegacion1.delegacion}")
            return jug1
        elif jug1.lesionado is True and jug2.lesionado is False:
            print(f"{self.deporte}: {jug1.nombre} de la delegación",
                  f"{self.delegacion1.delegacion} se lesiona!")
            print(f"{self.deporte}: Gana {jug2.nombre}",
                  f"de la delegación {self.delegacion2.delegacion}")
            return jug2
        else:
            arg1 = (p.ATLETISMO_POND_VEL * jug1.velocidad
                    + p.ATLETISMO_POND_RES * jug1.resistencia
                    + p.ATLETISMO_POND_MOR * jug1.moral)
            ptos1 = max(p.PUNTAJE_MINIMO_DEPORTE, arg1)
            arg2 = (p.ATLETISMO_POND_VEL * jug2.velocidad
                    + p.ATLETISMO_POND_RES * jug2.resistencia
                    + p.ATLETISMO_POND_MOR * jug2.moral)
            ptos2 = max(p.PUNTAJE_MINIMO_DEPORTE, arg2)
            if ptos1 > ptos2:
                print(f"{self.deporte}: Gana {jug1.nombre}",
                      f"de la delegación {self.delegacion1.delegacion}")
                return jug1
            elif ptos1 == ptos2:
                print(f"{self.deporte}: Empate")
                return None
            else:
                print(f"{self.deporte}: Gana {jug2.nombre}",
                      f"de la delegación {self.delegacion2.delegacion}")
                return jug2


class DeporteCiclismo(Deporte):  # LISTO
    def __init__(self, delegacion1, delegacion2):
        self.deporte = "Ciclismo"
        self.delegacion1 = delegacion1
        self.delegacion2 = delegacion2
        self.implemento = p.IMP_CICLISMO  # bool
        self.riesgo = p.RIESGO_CICLISMO  # float

    def calcular_ganador(self, jug1, jug2):
        jug1.lesionarse(self.riesgo)
        jug2.lesionarse(self.riesgo)
        if jug1.lesionado is True and jug2.lesionado is True:
            print(f"{self.deporte}: Auch! Empate por lesión de ambos jugadores")
            return None
        elif jug1.lesionado is False and jug2.lesionado is True:
            print(f"{self.deporte}: {jug2.nombre} de la delegación",
                  f"{self.delegacion2.delegacion} se lesiona!")
            print(f"{self.deporte}: Gana {jug1.nombre}",
                  f"de la delegación {self.delegacion1.delegacion}")
            return jug1
        elif jug1.lesionado is True and jug2.lesionado is False:
            print(f"{self.deporte}: {jug1.nombre} de la delegación",
                  f"{self.delegacion1.delegacion} se lesiona!")
            print(f"{self.deporte}: Gana {jug2.nombre}",
                  f"de la delegación {self.delegacion2.delegacion}")
            return jug2
        else:
            arg1 = (p.CICLISMO_POND_VEL * jug1.velocidad
                    + p.CICLISMO_POND_RES * jug1.resistencia
                    + p.CICLISMO_POND_FLE * jug1.flexibilidad)
            ptos1 = max(p.PUNTAJE_MINIMO_DEPORTE, arg1)
            arg2 = (p.CICLISMO_POND_VEL * jug2.velocidad
                    + p.CICLISMO_POND_RES * jug2.resistencia
                    + p.CICLISMO_POND_FLE * jug2.flexibilidad)
            ptos2 = max(p.PUNTAJE_MINIMO_DEPORTE, arg2)
            if ptos1 > ptos2:
                print(f"{self.deporte}: Gana {jug1.nombre}",
                      f"de la delegación {self.delegacion1.delegacion}")
                return jug1
            elif ptos1 == ptos2:
                print(f"{self.deporte}: Empate")
                return None
            else:
                print(f"{self.deporte}: Gana {jug2.nombre}",
                      f"de la delegación {self.delegacion2.delegacion}")
                return jug2


class DeporteGimnasia(Deporte):  # LISTO
    def __init__(self, delegacion1, delegacion2):
        self.deporte = "Gimnasia"
        self.delegacion1 = delegacion1
        self.delegacion2 = delegacion2
        self.implemento = p.IMP_GIMNASIA  # bool
        self.riesgo = p.RIESGO_GIMNASIA  # float

    def calcular_ganador(self, jug1, jug2):
        jug1.lesionarse(self.riesgo)
        jug2.lesionarse(self.riesgo)
        if jug1.lesionado is True and jug2.lesionado is True:
            print(f"{self.deporte}: Auch! Empate por lesión de ambos jugadores")
            return None
        elif jug1.lesionado is False and jug2.lesionado is True:
            print(f"{self.deporte}: {jug2.nombre} de la delegación",
                  f"{self.delegacion2.delegacion} se lesiona!")
            print(f"{self.deporte}: Gana {jug1.nombre}",
                  f"de la delegación {self.delegacion1.delegacion}")
            return jug1
        elif jug1.lesionado is True and jug2.lesionado is False:
            print(f"{self.deporte}: {jug1.nombre} de la delegación",
                  f"{self.delegacion1.delegacion} se lesiona!")
            print(f"{self.deporte}: Gana {jug2.nombre}",
                  f"de la delegación {self.delegacion2.delegacion}")
            return jug2
        else:
            arg1 = (p.GIMNASIA_POND_FLE * jug1.flexibilidad
                    + p.GIMNASIA_POND_RES * jug1.resistencia
                    + p.GIMNASIA_POND_MOR * jug1.moral)
            ptos1 = max(p.PUNTAJE_MINIMO_DEPORTE, arg1)
            arg2 = (p.GIMNASIA_POND_FLE * jug2.flexibilidad
                    + p.GIMNASIA_POND_RES * jug2.resistencia
                    + p.GIMNASIA_POND_MOR * jug2.moral)
            ptos2 = max(p.PUNTAJE_MINIMO_DEPORTE, arg2)
            if ptos1 > ptos2:
                print(f"{self.deporte}: Gana {jug1.nombre}",
                      f"de la delegación {self.delegacion1.delegacion}")
                return jug1
            elif ptos1 == ptos2:
                print(f"{self.deporte}: Empate")
                return None
            else:
                print(f"{self.deporte}: Gana {jug2.nombre}",
                      f"de la delegación {self.delegacion2.delegacion}")
                return jug2


class DeporteNatacion(Deporte):  # LISTO
    def __init__(self, delegacion1, delegacion2):
        self.deporte = "Natación"
        self.delegacion1 = delegacion1
        self.delegacion2 = delegacion2
        self.implemento = p.IMP_NATACION  # bool
        self.riesgo = p.RIESGO_NATACION  # float

    def calcular_ganador(self, jug1, jug2):
        jug1.lesionarse(self.riesgo)
        jug2.lesionarse(self.riesgo)
        if jug1.lesionado is True and jug2.lesionado is True:
            print(f"{self.deporte}: Auch! Empate por lesión de ambos jugadores")
            return None
        elif jug1.lesionado is False and jug2.lesionado is True:
            print(f"{self.deporte}: {jug2.nombre} de la delegación",
                  f"{self.delegacion2.delegacion} se lesiona!")
            print(f"{self.deporte}: Gana {jug1.nombre}",
                  f"de la delegación {self.delegacion1.delegacion}")
            return jug1
        elif jug1.lesionado is True and jug2.lesionado is False:
            print(f"{self.deporte}: {jug1.nombre} de la delegación",
                  f"{self.delegacion1.delegacion} se lesiona!")
            print(f"{self.deporte}: Gana {jug2.nombre}",
                  f"de la delegación {self.delegacion2.delegacion}")
            return jug2
        else:
            arg1 = (p.NATACION_POND_VEL * jug1.velocidad
                    + p.NATACION_POND_RES * jug1.resistencia
                    + p.NATACION_POND_FLE * jug1.flexibilidad)
            ptos1 = max(p.PUNTAJE_MINIMO_DEPORTE, arg1)
            arg2 = (p.NATACION_POND_VEL * jug2.velocidad
                    + p.NATACION_POND_RES * jug2.resistencia
                    + p.NATACION_POND_FLE * jug2.flexibilidad)
            ptos2 = max(p.PUNTAJE_MINIMO_DEPORTE, arg2)
            if ptos1 > ptos2:
                print(f"{self.deporte}: Gana {jug1.nombre}",
                      f"de la delegación {self.delegacion1.delegacion}")
                return jug1
            elif ptos1 == ptos2:
                print(f"{self.deporte}: Empate")
                return None
            else:
                print(f"{self.deporte}: Gana {jug2.nombre}",
                      f"de la delegación {self.delegacion2.delegacion}")
                return jug2
