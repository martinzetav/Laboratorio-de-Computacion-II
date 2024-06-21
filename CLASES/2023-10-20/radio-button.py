from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("2023-10-20/miventana.ui", self)
        self.opcion1.toggled.connect(self.on_opcion)
        self.opcion2.toggled.connect(self.on_opcion)
        self.opcion3.toggled.connect(self.on_opcion)

    #Este metodo al ejecutarse por primera vez, imprime una vez "en opcion" y luego imprime dos veces,
    # ya que se ejecuta una vez cuando sacamos la seleccion y otra ves cuando seleccionamos otra opcion
    def on_opcion(self):
        print("en opcion")
        if self.opcion1.isChecked():
            self.etiqueta.setText("opcion 1 elegida")
        if self.opcion2.isChecked():
            self.etiqueta.setText("opcion 2 elegida")
        if self.opcion3.isChecked():
            self.etiqueta.setText("opcion 3 elegida")


    # def on_opcion(self):
    #     if self.opcion1.isChecked():
    #         self.etiqueta.setText("opcion 1 elegida")
    #     else:
    #         self.etiqueta.setText("opcion 1 no elegida")

app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()

#clicked()
#toggled(): se dispara cuando se elige el radio boton o cuando no se elige
#isChecked(): devuelve True o False segun se haya hecho click en el radio boton

#toggled reacciona cuando se cambia de radio boton, mientras que clicked reacciona cuando se hace click en el boton
#clicked: si usamos un print, este se imprime las veces que hagamos click en el mismo radio boton
#toggled: si usamos un print, este se imprime una vez la primera vez al ejecutarse, y se imprime dos veces al cambiar de radio boton y seleccionar otro