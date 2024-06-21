from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TP3-Lab/ejercicio5/temperatura.ui", self)
        self.btn_calcular.clicked.connect(self.on_calcular)

    def on_calcular(self):
        temp_inicial = float(self.lineEdit.text())
        temp_final = 0
        if self.centi_kelvin.isChecked():
            k = temp_inicial + 273.15
            temp_final = f"Temperatura: {k:.2f} K"
        if self.kelvin_centi.isChecked():
            c = temp_inicial - 273.15
            temp_final = f"Temperatura: {c:.2f} °C"
        if self.centi_fahr.isChecked():
            f = (temp_inicial * (9/5)) + 32
            temp_final = f"Temperatura: {f:.2f} °F"
        if self.fahr_centi.isChecked():
            c = (temp_inicial - 32) * (5/9)
            temp_final = f"Temperatura: {c:.2f} °C"
        self.lbl_temperatura.setText(temp_final)

            


app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()