from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TP3-Lab/ejercicio7/miventana.ui", self)
        self.btn_editar.setEnabled(False)
        self.btn_quitar.setEnabled(False)
        self.btn_quitar_todos.setEnabled(False)
        self.comboBox.currentIndexChanged.connect(self.on_combobox)
        self.btn_agregar.clicked.connect(self.on_agregar)
        self.btn_editar.clicked.connect(self.on_editar)
        self.btn_quitar.clicked.connect(self.on_quitar)
        self.btn_quitar_todos.clicked.connect(self.on_quitar_todos)


    def on_agregar(self):
        texto, ok = QInputDialog.getText(self, "Ingresar", "Ingrese el texto")
        if ok:
            self.comboBox.addItem(texto)

    def on_combobox(self):
        if self.comboBox.count() > 0:
            self.btn_editar.setEnabled(True)
            self.btn_quitar.setEnabled(True)
            self.btn_quitar_todos.setEnabled(True)
        else:
            self.btn_editar.setEnabled(False)
            self.btn_quitar.setEnabled(False)
            self.btn_quitar_todos.setEnabled(False)

    def on_editar(self):
        texto, ok= QInputDialog.getText(self, "Editar", "Edite el texto", text=self.comboBox.currentText())
        if ok:
            index = self.comboBox.currentIndex()
            self.comboBox.setItemText(index, texto)

    def on_quitar(self):
        msg = QMessageBox()
        msg.setWindowTitle("Advertencia")
        msg.setText("¿Desea eliminar el texto seleccionado?")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        respuesta = msg.exec()
        
        if respuesta == QMessageBox.StandardButton.Yes:
            index = self.comboBox.currentIndex()
            self.comboBox.removeItem(index)

    def on_quitar_todos(self):
        msg = QMessageBox()
        msg.setWindowTitle("Advertencia")
        msg.setText("¿Desea eliminar todo?")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        respuesta = msg.exec()
        
        if respuesta == QMessageBox.StandardButton.Yes:
            self.comboBox.clear()
       


app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()