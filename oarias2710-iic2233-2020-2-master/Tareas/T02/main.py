import sys
import os
import time

from PyQt5 import uic
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimedia import QSound

from funciones import entrega_lineas_texto_ptjes, nombre_valido
from parametros import (RUTA_FILE_PTJES, RUTA_WIN_INICIO, RUTA_WIN_RANKING,
                        RUTA_WIN_JUEGO, mensaje_advertencia, RUTA_CANCION_1,
                        RUTA_CANCION_2, DINERO_INICIAL, PRECIO_PINGUIRIN)

from clases_auxiliares import FlechaPrincipiante, Temporizador

win_inicio, base_class_inicio = uic.loadUiType(RUTA_WIN_INICIO)
win_ranking, base_class_ranking = uic.loadUiType(RUTA_WIN_RANKING)
win_juego, base_class_juego = uic.loadUiType(RUTA_WIN_JUEGO)


class MisSenales(QObject):
    senal_ir_a_rank = pyqtSignal()  # Señal simple
    senal_ir_a_ini = pyqtSignal()  # Señal simple
    senal_ir_a_juego = pyqtSignal()  # Señal simple
    senal_nombre_usuario = pyqtSignal(str)  # Señal que permite enviar texto
    senal_terminar = pyqtSignal()


class WinJuego(win_juego, base_class_juego):

    def __init__(self, senal_ir_a_juego, senal_ir_a_ini, senal_nombre_usuario, senal_terminar):
        super().__init__()
        self.setupUi(self)
        self.cancion1 = QSound(RUTA_CANCION_1, self)
        self.cancion2 = QSound(RUTA_CANCION_2, self)
        self.LabelDinero.setText(f"$ {DINERO_INICIAL}")
        self.LabelValorPing.setText(f"$ {PRECIO_PINGUIRIN}")
        self.elPrimeroGratis.setText("(el primero es gratis!)")
        # señales
        self.senal_open_juego = senal_ir_a_juego
        self.senal_open_juego.connect(self.run_ventana_juego)
        self.senal_open_ini = senal_ir_a_ini
        self.senal_nombre_usuario = senal_nombre_usuario
        self.senal_nombre_usuario.connect(self.edita_label_usuario)
        self.senal_terminar = senal_terminar
        self.senal_terminar.connect(self.terminar_principiante)
        # botones
        self.BotonSalir.clicked.connect(self.boton_salir_clickeado)
        self.BotonComenzar.clicked.connect(self.boton_comenzar_clickeado)

    def boton_salir_clickeado(self):
        self.close()
        self.senal_open_ini.emit()

    def run_ventana_juego(self):
        self.show()

    def edita_label_usuario(self, usuario):
        self.Usuario.setText(usuario)
        self.Usuario.repaint()

    def boton_comenzar_clickeado(self):
        self.SelectCancion.setEnabled(False)
        self.SelectCancion.repaint()
        self.SelectDificultad.setEnabled(False)
        self.SelectDificultad.repaint()
        self.BotonComenzar.setEnabled(False)
        self.BotonComenzar.repaint()
        self.BotonSalir.setEnabled(False)
        self.BotonSalir.repaint()
        cancion = self.SelectCancion.currentText()
        dificultad = self.SelectDificultad.currentText()
        self.cancion.setText(cancion)
        self.cancion.repaint()
        self.dificultad.setText(dificultad)
        self.dificultad.repaint()

        if dificultad == "Principiante":
            # Genera las flechas
            self.timer_crea_flecha = QTimer(self)
            self.timer_crea_flecha.setInterval(1000)
            self.timer_crea_flecha.timeout.connect(self.creador_de_flechas_principiante)
            self.timer_crea_flecha.start()
            self.flechas = []
            if cancion == "Canción 1":
                self.cancion1.play()
            elif cancion == "Canción 2":
                self.cancion2.play()
            # Timer para terminar las flechas
            temporizador = Temporizador("principiante", 30, self.senal_terminar)
            temporizador.start()

    def terminar_principiante(self):
        self.timer_crea_flecha.stop()
        self.SelectCancion.setEnabled(True)
        self.SelectCancion.repaint()
        self.SelectDificultad.setEnabled(True)
        self.SelectDificultad.repaint()
        self.BotonComenzar.setEnabled(True)
        self.BotonComenzar.repaint()
        self.BotonSalir.setEnabled(True)
        self.BotonSalir.repaint()
        if self.cancion1.isFinished() is False:
            self.cancion1.stop()
        if self.cancion2.isFinished() is False:
            self.cancion2.stop()

    def creador_de_flechas_principiante(self):
        nueva_flecha = FlechaPrincipiante(self, 585)
        nueva_flecha.actualizar.connect(self.actualizar_label)
        self.flechas.append(nueva_flecha)

    def actualizar_label(self, label, x, y):
        label.move(x, y)


class WinInicio(win_inicio, base_class_inicio):

    def __init__(self, senal_ir_a_rank, senal_ir_a_ini, senal_ir_a_juego, senal_nombre_usuario):
        super().__init__()
        self.setupUi(self)
        # señales
        self.senal_open_rank = senal_ir_a_rank
        self.senal_open_ini = senal_ir_a_ini
        self.senal_open_ini.connect(self.run_ventana_ini)
        self.senal_open_juego = senal_ir_a_juego
        self.senal_nombre_usuario = senal_nombre_usuario
        # botones
        self.BotonRanking.clicked.connect(self.boton_ranking_clickeado)
        self.BotonComenzar.clicked.connect(self.boton_comenzar_clickeado)

    def run_ventana_ini(self):
        self.Advertencia.setText("")
        self.Advertencia.repaint()
        self.CajaNombre.clear()
        self.CajaNombre.repaint()
        self.show()

    def boton_ranking_clickeado(self):
        self.close()
        self.senal_open_rank.emit()

    def boton_comenzar_clickeado(self):
        nombre = self.CajaNombre.text()
        validacion = nombre_valido(nombre)
        if validacion is True:
            self.senal_nombre_usuario.emit(nombre)
            self.senal_open_juego.emit()
            self.close()
        else:
            self.Advertencia.setText(mensaje_advertencia)
            self.Advertencia.repaint()


class WinRanking(win_ranking, base_class_ranking):

    def __init__(self, senal_ir_a_rank, senal_ir_a_ini):
        super().__init__()
        self.setupUi(self)
        # señales
        self.senal_open_rank = senal_ir_a_rank
        self.senal_open_rank.connect(self.run_ventana_ranking)
        self.senal_open_ini = senal_ir_a_ini
        # botones
        self.BotonBorrar.clicked.connect(self.borrar_puntajes)
        self.BotonVolver.clicked.connect(self.volver_ini)

    def run_ventana_ranking(self):
        self.show()
        puntajes = entrega_lineas_texto_ptjes(RUTA_FILE_PTJES)
        self.ptje01.setText(puntajes[0])
        self.ptje01.repaint()
        self.ptje02.setText(puntajes[1])
        self.ptje02.repaint()
        self.ptje03.setText(puntajes[2])
        self.ptje03.repaint()
        self.ptje04.setText(puntajes[3])
        self.ptje04.repaint()
        self.ptje05.setText(puntajes[4])
        self.ptje05.repaint()
        if puntajes[0] == " ":
            self.ptje01.setText("No existen puntajes registrados")
            self.ptje01.repaint()

    def borrar_puntajes(self):
        os.remove(RUTA_FILE_PTJES)
        open(RUTA_FILE_PTJES, "w+")
        self.show()
        self.ptje01.setText("")
        self.ptje01.repaint()
        self.ptje02.setText("")
        self.ptje02.repaint()
        self.ptje03.setText("")
        self.ptje03.repaint()
        self.ptje04.setText("")
        self.ptje04.repaint()
        self.ptje05.setText("")
        self.ptje05.repaint()
        self.ptje01.setText("No existen puntajes registrados")
        self.ptje01.repaint()

    def volver_ini(self):
        self.close()
        self.senal_open_ini.emit()


if __name__ == '__main__':
    app = QApplication([])
    senales = MisSenales()
    ini = WinInicio(senales.senal_ir_a_rank, senales.senal_ir_a_ini,
                    senales.senal_ir_a_juego, senales.senal_nombre_usuario)
    rank = WinRanking(senales.senal_ir_a_rank, senales.senal_ir_a_ini)
    juego = WinJuego(senales.senal_ir_a_juego, senales.senal_ir_a_ini,
                     senales.senal_nombre_usuario, senales.senal_terminar)
    ini.show()
    sys.exit(app.exec_())
