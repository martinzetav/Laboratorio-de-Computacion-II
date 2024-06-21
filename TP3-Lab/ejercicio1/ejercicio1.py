from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TP3-Lab/ejercicio1/miventana.ui", self)
        self.cambiar.clicked.connect(self.on_cambiar_saludo)

    def on_cambiar_saludo(self):
        if self.etiqueta.text() == "Hola Mundo!":
            self.etiqueta.setText("Chau Mundo!")
        elif self.etiqueta.text() == "Chau Mundo!":
            self.etiqueta.setText("Hola Mundo!")
        
        # self.cambiar.setEnable(True)


app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()