from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class MiVentana(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("2023-10-30/00-lista.ui", self)

    self.lista.itemSelectionChanged.connect(self.on_item_selection_changed)
    #self.lista.currentItemChanged.connect(self.on_current_item_changed)

    # Agregar item a la lista
    #self.lista.addItem('Texto')

    # Obtener fila del item actualmente elegido
    #self.lista.currentRow()

    # Obtener item a partir de fila
    #self.lista.item(fila)

    # Editar item de la lista
    #item.setText('nuevo texto')

    # Quitar item de la lista
    #self.lista.takeItem(fila)

    # Quitar todos los item de la lista
    #self.lista.clear()

  def on_item_selection_changed(self):
    item = self.lista.currentItem()
    self.seleccion.setText(item.text())
  
  def on_current_item_changed(self, item):
    self.seleccion.setText(item.text())

  

app = QApplication([])

win = MiVentana()
win.show()

app.exec()