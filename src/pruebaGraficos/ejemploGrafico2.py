# coding=utf-8

# importa el módulo sys
import sys

# importa el sub-módulo QtGui del módulo PyQt4
from PyQt4 import QtGui

# Clase Ventana que hereda de QtGui.QMainWindow
class Ventana (QtGui.QMainWindow):

    # Constructor de la Ventana
    def __init__(self):

        # Se ejecuta el Constructor de la clase Padre
        super(Ventana, self).__init__()

        # Se Define la posicion y tamaño para el Grafico
        self.setGeometry(50,50,500,300)

        # Se agrega un titulo al Grafico
        self.setWindowTitle("Segunda Ventana de prueba")

        # Se Agrega un Icono al Grafico
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        
        #########################################################################
        ###########  Construccion de un Menu en el Grafico  #####################
        #########################################################################

        # Se agrega un evento
        EventoSalir = QtGui.QAction(QtGui.QIcon("salir.png"),"salir",self) 

        # Se agrega un atajo, debe ir junto la cadena
        EventoSalir.setShortcut("Ctrl+Q")

        #
        EventoSalir.setStatusTip('Sali de la aplicacion')

        #
        EventoSalir.triggered.connect(self.cierra_aplicacion)

        # Menu
        MenuPrincipal = self.menuBar()

        # elemento Archivo del menu
        MenuArchivo = MenuPrincipal.addMenu('&Archivo')

        # Se agrega un listener o escuchador de evento, recibe el evento "EventoSalir"
        MenuArchivo.addAction(EventoSalir)

        # Se crea el contenifo del Grafico
        self.home()
    
    #########################################################################
    ##################  Contenido en el Grafico  ############################
    #########################################################################

    def home(self):

        # Configuracion de el Contenido

        # Declaracion de componentes
        self.btn_Saludo = QtGui.QPushButton("Despliega Nombre",self)
        self.solicita_lbl = QtGui.QLabel('Ingresa tu nombre: ',self)
        self.entrada_texto = QtGui.QLineEdit(self)
        self.resultado_lbl = QtGui.QLabel('Resultado: ',self)
        self.salida_texto  = QtGui.QLineEdit(self)
        self.btn_Salir = QtGui.QPushButton("Salir",self)
        
        # Configuracion de tamaño y ubicacion de los elementos en el Grafico
        self.entrada_texto.resize(200,30)
        self.entrada_texto.move(200,100)
        self.solicita_lbl.move(105,100)
        self.resultado_lbl.move(145,145)
        self.salida_texto.resize(200,30)
        self.salida_texto.move(200,150)
        
        self.btn_Saludo.resize(100,40)
        self.btn_Saludo.move(200,40)

        self.btn_Salir.resize(100,40)
        self.btn_Salir.move(200,200)

        # Al hacer click en los botones ejecuta los metodos correspondientes
        self.btn_Salir.clicked.connect(self.cierra_aplicacion)
        self.btn_Saludo.clicked.connect(self.despliega)
        
        # Hace Visible el Grafico
        self.show()

    # Metodo que despliega el mensaje "Hola python grafico: + entrada de texto" 
    # en el field "salida_texto"
    def despliega(self):
        mensaje = "Hola python grafico: " + self.entrada_texto.text()
        # Coloca texto en el field
        self.salida_texto.setText(mensaje)

    # Metodo que cierra el Grafico
    def cierra_aplicacion(self):
        sys.exit()

# Metodo main que correr la aplicacion
def main():
    
    app = QtGui.QApplication(sys.argv)

    GUI = Ventana()
    sys.exit(app.exec_())

# Se corre el main
main()