from abc import ABC, abstractmethod
import random
import parametros as p


class Delegaciones(ABC):  # LISTO
    def __init__(self, entrenador, equipo, medallas, dinero):  # OK
        self.entrenador = entrenador  # str
        self.equipo = equipo  # list
        self.medallas = medallas  # int
        len_equipo = len(self.equipo)
        sumatoria = 0
        for deportista in self.equipo:
            sumatoria += deportista.moral
        self.moral = sumatoria / len_equipo  # float
        self.dinero = dinero  # int
        self.hab_especial_usadas = 0

    def fichar_deportista(self, deportista):  # OK
        if self.dinero > deportista.precio:
            if self.moral > p.UMBRAL_MORAL_FICHAR:
                self.equipo.append(deportista)
                self.dinero = self.dinero - deportista.precio
                print(f"{self.entrenador} ha fichado a {deportista.nombre}!")
            else:
                print("Lo siento, moral de la delegación es muy baja")
        else:
            print("Lo siento, no tienes sufiente dinero")

    def sanar_lesiones(self, deportista):  # OK
        if deportista.lesionado is False:
            print("Este deportista no está lesionado")
        elif self.dinero < p.COSTO_SANAR:
            print("No tienes dinero suficiente")
        else:
            self.dinero -= p.COSTO_SANAR
            arg = (deportista.moral * (self.imp_medicos + self.exce_respeto)) / 200
            prob = round(min(1, max(0, arg)), 1)
            # print(f"Prob: {prob}")
            realizacion = random.uniform(0, 1)
            # print(f"Realización: {realizacion}")
            if realizacion <= prob:
                deportista.lesionado = False
                print(f"{deportista.nombre} ha superado su lesión y está listo para competir")
            else:
                print(f"Lamentablemente {deportista.nombre} no logró recuperse de su lesión")

    def comprar_tecnologia(self):  # OK
        if self.dinero >= p.COSTO_TECNOLOGIA:
            self.imp_deportivos += self.imp_deportivos * p.BONUS_TECNOLOGIA
            self.imp_medicos += self.imp_medicos * p.BONUS_TECNOLOGIA
            self.dinero -= p.COSTO_TECNOLOGIA
            print("Compraste tecnología, bien hecho!")
        else:
            print("No tienes dinero suficiente")


class DelegacionIEEEsparta(Delegaciones):  # LISTO
    def __init__(self, entrenador, equipo, medallas, dinero):  # OK
        super().__init__(entrenador, equipo, medallas, dinero)
        self.exce_respeto = random.uniform(p.MIN_IEEE_EXCE_RESPETO,
                                           p.MAX_IEEE_EXCE_RESPETO)
        self.imp_medicos = random.uniform(p.MIN_IEEE_IMP_MEDICOS,
                                          p.MAX_IEEE_IMP_MEDICOS)
        self.imp_deportivos = random.uniform(p.MIN_IEEE_IMP_DEPORTIVOS,
                                             p.MAX_IEEE_IMP_DEPORTIVOS)
        self.delegacion = "IEEEsparta"

    def entrenar_deportista(self, deportista, atributo):  # para cada delegacion  #  OK
        if self.dinero >= p.COSTO_ENTRENAMIENTO:
            self.dinero -= p.COSTO_ENTRENAMIENTO
            deportista.entrenar_ieee(atributo)
            deportista.moral += p.BONUS_MORAL_ENTRENAMIENTO
        else:
            print("No tienes dinero suficiente")

    def utilizar_habilidad(self):  # OK
        if self.hab_especial_usadas < p.MAX_HABILIDAD_ESPECIAL:
            for deportista in self.equipo:
                deportista.moral += p.MAX_MORAL
            len_equipo = len(self.equipo)
            sumatoria = 0
            for deportista in self.equipo:
                sumatoria += deportista.moral
            self.moral = sumatoria / len_equipo  # float
            self.hab_especial_usadas += 1
            self.dinero -= p.COSTO_HABILIDAD_ESPECIAL
        else:
            print("No te queda habilidad especial para usar")


class DelegacionDCCrotona(Delegaciones):
    def __init__(self, entrenador, equipo, medallas, dinero):  # OK
        super().__init__(entrenador, equipo, medallas, dinero)
        self.exce_respeto = random.uniform(p.MIN_DCC_EXCE_RESPETO,
                                           p.MAX_DCC_EXCE_RESPETO)
        self.imp_medicos = random.uniform(p.MIN_DCC_IMP_MEDICOS,
                                          p.MAX_DCC_IMP_MEDICOS)
        self.imp_deportivos = random.uniform(p.MIN_DCC_IMP_DEPORTIVOS,
                                             p.MAX_DCC_IMP_DEPORTIVOS)
        self.delegacion = "DCCrotona"

    def sanar_lesiones(self, deportista):  # OK
        if deportista.lesionado is False:
            print("Este deportista no está lesionado")
        elif self.dinero < p.MULT_COSTO_DCC_SANAR * p.COSTO_SANAR:
            print("No tienes dinero suficiente")
        else:
            self.dinero -= p.MULT_COSTO_DCC_SANAR * p.COSTO_SANAR
            arg = (deportista.moral * (self.imp_medicos + self.exce_respeto)) / 200
            # print(f"Arg: {arg}")
            prob = round(min(1, max(0, arg)), 1)
            # print(f"Prob: {prob}")
            realizacion = random.uniform(0, 1)
            # print(f"Realización: {realizacion}")
            if realizacion <= prob:
                deportista.lesionado = False
                print(f"{deportista.nombre} ha superado su lesión y está listo para competir")
            else:
                print(f"Lamentablemente {deportista.nombre} no logró recuperse de su lesión")

    def entrenar_deportista(self, deportista, atributo):  # para cada delegacion  #  OK
        if self.dinero >= p.COSTO_ENTRENAMIENTO:
            self.dinero -= p.COSTO_ENTRENAMIENTO
            deportista.entrenar_dcc(atributo)
            deportista.moral += p.BONUS_MORAL_ENTRENAMIENTO
        else:
            print("No tienes dinero suficiente")

    def utilizar_habilidad(self):  # para cada delegación  #  PENDIENTE ################## OJO
        if self.hab_especial_usadas < p.MAX_HABILIDAD_ESPECIAL:
            # completar esto con la función de premiación con medallas
            self.hab_especial_usadas += 1
            self.dinero -= p.COSTO_HABILIDAD_ESPECIAL
        else:
            print("No te queda habilidad especial para usar")


class Deportista:  # LISTO
    def __init__(self, nombre, velo, resistencia, flexi, moral, lesionado, precio):  # OK
        self.nombre = nombre
        self.__velocidad = velo
        self.__resistencia = resistencia
        self.__flexibilidad = flexi
        self.__moral = moral
        if lesionado == "True":
            self.lesionado = bool(1 == 1)
        elif lesionado == "False":
            self.lesionado = bool(1 == 0)
        self.precio = precio

    @property
    def velocidad(self):  # OK
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, puntos):  # OK
        if puntos > p.MAX_VELOCIDAD:
            self.__velocidad = p.MAX_VELOCIDAD
        elif puntos < p.MIN_VELOCIDAD:
            self.__velocidad = p.MIN_VELOCIDAD
        else:
            self.__velocidad = puntos

    @property
    def resistencia(self):  # OK
        return self.__resistencia

    @resistencia.setter
    def resistencia(self, puntos):  # OK
        if puntos > p.MAX_RESISTENCIA:
            self.__resistencia = p.MAX_RESISTENCIA
        elif puntos < p.MIN_VELOCIDAD:
            self.__resistencia = p.MIN_RESISTENCIA
        else:
            self.__resistencia = puntos

    @property
    def flexibilidad(self):  # OK
        return self.__flexibilidad

    @flexibilidad.setter
    def flexibilidad(self, puntos):  # OK
        if puntos > p.MAX_FLEXIBILIDAD:
            self.__flexibilidad = p.MAX_FLEXIBILIDAD
        elif puntos < p.MIN_VELOCIDAD:
            self.__flexibilidad = p.MIN_FLEXIBILIDAD
        else:
            self.__flexibilidad = puntos

    @property
    def moral(self):  # OK
        return self.__moral

    @moral.setter
    def moral(self, puntos):  # OK
        if puntos > p.MAX_MORAL:
            self.__moral = p.MAX_MORAL
        elif puntos < p.MIN_VELOCIDAD:
            self.__moral = p.MIN_MORAL
        else:
            self.__moral = puntos

    def entrenar_dcc(self, atributo):  # OK
        if atributo == "velocidad":
            self.velocidad += self.velocidad ** (1 / p.PUNTOS_ENTRENAMIENTO)
        elif atributo == "resistencia":
            self.resistencia += self.resistencia ** (1 / p.PUNTOS_ENTRENAMIENTO)
        elif atributo == "flexibilidad":
            self.flexibilidad += self.flexibilidad ** (1 / p.PUNTOS_ENTRENAMIENTO)

    def entrenar_ieee(self, atributo):  # OK
        if atributo == "velocidad":
            self.velocidad += ((self.velocidad ** (1 / p.PUNTOS_ENTRENAMIENTO)
                                ) * p.BONUS_IEEE_ENTRENAR)
        elif atributo == "resistencia":
            self.resistencia += ((self.resistencia ** (1 / p.PUNTOS_ENTRENAMIENTO)
                                  ) * p.BONUS_IEEE_ENTRENAR)
        elif atributo == "flexibilidad":
            self.flexibilidad += ((self.flexibilidad ** (1 / p.PUNTOS_ENTRENAMIENTO)
                                   ) * p.BONUS_IEEE_ENTRENAR)

    def lesionarse(self, riesgo):  # OK
        realizacion = random.uniform(0, 1)
        if realizacion <= riesgo:
            self.lesionado = True
        else:
            self.lesionado = False
