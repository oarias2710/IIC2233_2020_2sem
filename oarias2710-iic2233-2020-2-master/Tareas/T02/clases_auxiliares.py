import os
import random
import time
import threading

from parametros import RUTA_FLECHAS

from PyQt5.QtCore import QThread, QTimer, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication


class Temporizador(threading.Thread):  # Hereda de Thread

    def __init__(self, nombre, tiempo, senal):
        super().__init__(name=nombre)
        self.tiempo = tiempo
        self.senal = senal

    def run(self):
        time.sleep(self.tiempo)
        self.senal.emit()


class FlechaPrincipiante(QThread):

    actualizar = pyqtSignal(QLabel, int, int)

    def __init__(self, parent, limite_y):
        super().__init__()
        flechas_rojas = ["down_3.png", "up_3.png", "left_3.png", "right_3.png"]
        flecha_aleatoria = random.choice(flechas_rojas)
        self.ruta_imagen = os.path.join(RUTA_FLECHAS, flecha_aleatoria)

        self.label = QLabel(parent)
        self.label.setGeometry(-50, -50, 30, 30)
        self.label.setPixmap(QPixmap(self.ruta_imagen))
        self.label.setScaledContents(True)
        self.label.setVisible(True)

        self.limite_y = limite_y

        self.__posicion = (0, 0)
        posiciones_x = [25, 70, 115, 160]
        self.posicion = (random.choice(posiciones_x), 175)

        self.label.show()
        self.start()

    @property
    def posicion(self):
        return self.__posicion

    @posicion.setter
    def posicion(self, valor):
        self.__posicion = valor
        self.actualizar.emit(self.label, *self.posicion)

    def run(self):
        while self.posicion[1] < self.limite_y:
            time.sleep(0.5)
            nuevo_x = self.posicion[0]
            nuevo_y = self.posicion[1] + 20
            self.posicion = (nuevo_x, nuevo_y)
        self.label.clear()
