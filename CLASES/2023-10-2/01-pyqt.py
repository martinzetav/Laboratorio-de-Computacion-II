from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication([]) #Crea la aplicacion

window = QMainWindow() #Crea una ventana

window.setWindowTitle("Mi Ventana") #Le da el nombre a la ventana

label = QLabel("Hola Mundo") #Incorpora una etiqueta (Se crea un objeto QLabel y se le pasa un texto)

window.setCentralWidget(label)
window.show() #Muestra una ventana


app.exec() #Ejecuta la aplicacion