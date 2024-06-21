from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TP3-Lab/ejercicio4/lomiteria.ui", self)
        self.btn_calcular.clicked.connect(self.on_calcular)

    def on_calcular(self):
        precio_total = 0
        if self.rb_carne.isChecked():
            precio_total=500
        if self.rb_pollo.isChecked():
            precio_total=450
        if self.rb_cerdo.isChecked():
            precio_total=400

        if self.cb_huevo.isChecked():
            precio_total+=100
        if self.cb_papas.isChecked():
            precio_total+=200
        if self.cb_gaseosa.isChecked():
            precio_total+=100
        if self.cb_delivery.isChecked():
            precio_total+=200

        self.label.setText(f"Precio Total: {precio_total}")


app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()