from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TP3-Lab/ejercicio8/miventana.ui", self)
        self.btn_IaD.clicked.connect(self.derecha_izquierda)
        self.btn_DaI.clicked.connect(self.izquierda_derecha)


    def izquierda_derecha(self):
        fila = self.listaI.currentRow()
        objeto = self.listaI.item(fila)
        self.listaI.takeItem(fila)
        self.listaD.addItem(objeto)

    def derecha_izquierda(self):
        fila = self.listaD.currentRow()
        objeto = self.listaD.item(fila)
        self.listaD.takeItem(fila)
        self.listaI.addItem(objeto)








app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()