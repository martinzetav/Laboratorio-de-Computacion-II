from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TP3-Lab/ejercicio6/ventana.ui", self)
        self.btn_mostrar.clicked.connect(self.on_mostrar)

    def on_mostrar(self):
        #Creo la ventana de dialogo
        mensaje = QMessageBox()
        mensaje.setWindowTitle(self.titulo.text())
        mensaje.setText(self.mensaje.text())

        #Evaluo lo radio bottons
        if self.rb_info.isChecked():
            mensaje.setIcon(QMessageBox.Icon.Information)
        if self.rb_pregunta.isChecked():
            mensaje.setIcon(QMessageBox.Icon.Question)
        if self.rb_precaucion.isChecked():
            mensaje.setIcon(QMessageBox.Icon.Warning)
        if self.rb_critico.isChecked():
            mensaje.setIcon(QMessageBox.Icon.Critical)

        #Evaluo los check buttons
        boton = QMessageBox.StandardButton.NoButton

        if self.si.isChecked():
            boton|=QMessageBox.StandardButton.Yes
        if self.no.isChecked():
            boton|=QMessageBox.StandardButton.No
        if self.abrir.isChecked():
            boton|=QMessageBox.StandardButton.Open
        if self.cerrar.isChecked():
            boton|=QMessageBox.StandardButton.Close
        if self.cancelar.isChecked():
            boton|=QMessageBox.StandardButton.Cancel
        if self.ok.isChecked():
            boton|=QMessageBox.StandardButton.Ok
        if self.guardar.isChecked():
            boton|=QMessageBox.StandardButton.Save
        if self.guardar_todo.isChecked():
            boton|=QMessageBox.StandardButton.SaveAll
        if self.reintentar.isChecked():
            boton|=QMessageBox.StandardButton.Retry
        if self.abortar.isChecked():
            boton|=QMessageBox.StandardButton.Abort
        if self.ignorar.isChecked():
            boton|=QMessageBox.StandardButton.Ignore 
       
        mensaje.setStandardButtons(boton)
        mensaje.exec()
         

app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()