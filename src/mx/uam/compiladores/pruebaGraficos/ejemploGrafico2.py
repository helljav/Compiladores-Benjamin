# coding=utf-8

# importa el módulo sys
import sys

# importa el sub-módulo QtGui del módulo PyQt4
from PyQt4 import QtGui

class Ventana (QtGui.QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Segunda Ventana de prueba")
        
        EventoSalir = QtGui.QAction(QtGui.QIcon("salir.jpg"),"salir",self) 
        EventoSalir.setShortcut("Ctrl + Q")
        EventoSalir.setStatusTip('Sali de la aplicacion')
        EventoSalir.triggered.connect(self.cierra_aplicacion)

        MenuPrincipal = self.menuBar()
        MenuArchivo = MenuPrincipal.addMenu('&Archivo')
        MenuArchivo.addAction(EventoSalir)
        self.home()
    
    def home(self):
        self.btn_Salir = QtGui.QPushButton("Salir",self)
        self.btn_Saludo = QtGui.QPushButton("Despliega Nombre",self)
        self.entrada_texto = QtGui.QLineEdit(self)
        self.salida_texto  = QtGui.QLineEdit(self)
        self.solicita_lbl = QtGui.QLabel('Ingresa tu nombre',self)
        self.resultado_lbl = QtGui.QLabel('Resultado : ',self)
        
        self.entrada_texto.resize(200,30)
        self.entrada_texto.move(200,100)
        self.solicita_lbl.move(105,100)
        self.resultado_lbl.move(145,145)
        self.salida_texto.resize(200,30)
        self.salida_texto.move(200,150)
        
        self.btn_Salir.clicked.connect(self.cierra_aplicacion)
        self.btn_Saludo.clicked.connect(self.despliega)
        
        self.btn_Saludo.resize(100,40)
        self.btn_Saludo.move(200,40)

        self.btn_Salir.resize(100,40)
        self.btn_Salir.move(200,200)
        self.show()

    def despliega(self):
        mensaje = "Hola python grafico: " + self.entrada_texto.text()
        self.salida_texto.setText(mensaje)

    def cierra_aplicacion(self):
        sys.exit()

def main():
    app = QtGui.QApplication(sys.argv)

    GUI = Ventana()
    sys.exit(app.exec_())

main()