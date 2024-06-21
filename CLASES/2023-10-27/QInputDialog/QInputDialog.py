from PyQt6.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt6 import uic

class MiVentana(QMainWindow):
  def  __init__(self):
    super().__init__()
    uic.loadUi("2023-10-27/QInputDialog/00-text-input.ui", self)

    self.ingresar_texto.clicked.connect(self.on_ingresar_texto)
    self.ingresar_entero.clicked.connect(self.on_ingresar_entero)
    self.ingresar_decimal.clicked.connect(self.on_ingresar_decimal)
    self.ingresar_item.clicked.connect(self.on_ingresar_item)

  def on_ingresar_texto(self):
    texto, ok = QInputDialog.getText(self, 'Ingresar', 'Ingrese texto', text='Texto por defecto')
    if ok==True:
      self.texto.setText(texto)

  def on_ingresar_entero(self):
    entero, ok = QInputDialog.getInt(self, 'Ingresar', 'Ingrese numero', value=15, min=0, max=100, step=10)
    if ok==True:
      self.entero.setText(f'{entero}')

  def on_ingresar_decimal(self):
    decimal, ok = QInputDialog.getDouble(self, 'Ingresar', 'Ingrese decimal', value=1.5, min=0, max=50, decimals=2, step=5)
    if ok==True:
      self.decimal.setText(f'{decimal:.3f}')

  def on_ingresar_item(self):
    items = ['Rojo', 'Verde', 'Amarillo', 'Azul']
    item, ok = QInputDialog.getItem(self, 'Ingresar', 'Elija item', items, 1, True)
    if ok==True:
      self.item.setText(item)

app = QApplication([])

win = MiVentana()
win.show()

app.exec()