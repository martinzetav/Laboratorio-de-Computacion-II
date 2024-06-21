from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TP3-Lab/ejercicio2/miventana.ui", self)
        self.btn_abajo.setEnabled(False)
        self.btn_derecha.setEnabled(False)
        self.btn_izquierda.setEnabled(False) 
        self.btn_arriba.clicked.connect(self.on_arriba)
        self.btn_derecha.clicked.connect(self.on_derecha)
        self.btn_abajo.clicked.connect(self.on_abajo)
        self.btn_izquierda.clicked.connect(self.on_izquierda)

    def on_arriba(self):
        self.btn_derecha.setEnabled(True)
        self.btn_arriba.setEnabled(False)

    def on_derecha(self):
        self.btn_abajo.setEnabled(True)
        self.btn_derecha.setEnabled(False)

    def on_abajo(self):
        self.btn_izquierda.setEnabled(True)
        self.btn_abajo.setEnabled(False)

    def on_izquierda(self):
        self.btn_arriba.setEnabled(True)
        self.btn_izquierda.setEnabled(False)

    

app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()