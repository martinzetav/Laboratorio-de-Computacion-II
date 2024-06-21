from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("2023-10-23/ventana.ui", self)
        self.btn_mostrar.clicked.connect(self.on_mostrar)

    def on_mostrar(self):
        mensaje = QMessageBox() #Creamos la caja/dialogo de mensaje
        mensaje.setWindowTitle("Titulo del Mensaje") #Ponemos titulo a la ventana
        mensaje.setText("Cuerpo del Mensaje") #Ponemos un cuerpo

        # mensaje.setIcon(QMessageBox.Icon.Information)
        # mensaje.setIcon(QMessageBox.Icon.Question)
        # mensaje.setIcon(QMessageBox.Icon.Warning)
        # mensaje.setIcon(QMessageBox.Icon.Critical)

        #Tipos de botones
        # mensaje.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Yes |
        #                             QMessageBox.StandardButton.No | QMessageBox.StandardButton.Save | QMessageBox.StandardButton.SaveAll | 
        #                             QMessageBox.StandardButton.Open | QMessageBox.StandardButton.Close | QMessageBox.StandardButton.Abort |
        #                             QMessageBox.StandardButton.Retry | QMessageBox.StandardButton.Ignore)

        mensaje.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)

        resultado = mensaje.exec()

        if resultado == QMessageBox.StandardButton.Yes:
            print("Usuario eligio SI")
        if resultado == QMessageBox.StandardButton.No:
            print("Usuario eligio NO")
        if resultado == QMessageBox.StandardButton.Cancel:
            print("Usuario eligio CANCELAR")
        



            


app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()