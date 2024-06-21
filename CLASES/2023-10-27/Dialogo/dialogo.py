from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication
from PyQt6 import uic

class Persona():
  def __init__(self, apellido, nombre):
    self.apellido = apellido
    self.nombre = nombre
  
  def __str__(self):
    return f'{self.apellido}, {self.nombre}'


class MiDialogo(QDialog):
  def __init__(self):
    super().__init__()
    uic.loadUi("2023-10-27/Dialogo/01-midialogo.ui", self)
  
  def getPersona(self):
    apellido = self.apellido.text()
    nombre = self.nombre.text()
    return Persona(apellido, nombre)


class MiVentana(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("2023-10-27/Dialogo/01-miventana.ui", self)

    self.personas = []

    self.verListado.clicked.connect(self.on_ver_listado)
    self.agregar.clicked.connect(self.on_agregar)

  def on_ver_listado(self):
    for persona in self.personas:
      print(persona)
  
  def on_agregar(self):
    dialogo = MiDialogo()
    if (dialogo.exec()):
      persona = dialogo.getPersona()
      self.personas.append(persona)


app = QApplication([])

win = MiVentana()
win.show()

app.exec()