from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TP3-Lab/ejercicio3/miventana.ui", self)
        self.btn_mostrar.clicked.connect(self.on_mostrar)
        # self.nombre.textChanged.connect(self.on_cambio_nombre)

    def on_mostrar(self):
        nombre = self.nombre.text()
        apellido = self.apellido.text()
        self.nombre_completo.setText(nombre + " " + apellido)

    # def on_cambio_nombre(self):
    #     nombre = self.nombre.text()
    #     apellido = self.apellido.text()
    #     self.nombre_completo.setText(nombre + " " + apellido)

    # def on_cambio_nombre(self, texto1):
    #     self.nombre_completo.setText(texto1)




app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()