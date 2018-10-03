import sys
from PyQt4 import QtGui
from Automata_AFD import Automata


class Ventana (QtGui.QMainWindow):

    ##
    # Constructor de la Ventana
    ##
    def __init__(self):
        super(Ventana, self).__init__()

        # Config Ventana
        self.setGeometry(350, 100, 700, 520)
        self.setWindowTitle("Practica2: Implementacion de un AFD")
        self.setWindowIcon(QtGui.QIcon("logo.png"))

        # Config del Menu
        self.MenuPrincipal = self.menuBar()
        self.MenuArchivo = self.MenuPrincipal.addMenu('&Archivo')

        # Barra de opciones
        self.BarraOpciones = self.addToolBar("Archivo")

        # Evento Salir
        self.EventoSalir = QtGui.QAction(QtGui.QIcon(
            "salir.png"), "Salir del Programa", self)
        self.EventoSalir.setShortcut("Ctrl+Q")
        self.EventoSalir.setStatusTip('Salir de la aplicacion')
        self.EventoSalir.triggered.connect(self.cierra_aplicacion)

        # Se agrega el listener del evento "EventoSalir" al menu
        self.MenuArchivo.addAction(self.EventoSalir)
        # Se agrega el listener del evento "EventoSalir" ala Barra de Opciones
        self.BarraOpciones.addAction(self.EventoSalir)

        self.init()

    ##
    # LLenado de la Ventana
    ##
    def init(self):
    
    # Componentes

        # Labels
        self.label_titulo = QtGui.QLabel( 'Automata Finito Determinista (AFD)', self )
        self.label_alfabeto = QtGui.QLabel( 'Lenguaje Sigma = { 0, 1 }', self )
        self.label_cadenaEvaluar = QtGui.QLabel( 'Proporcione una cadena a evaluar: ', self )
        self.label_resultadoEvaluar = QtGui.QLabel ( 'Resultado de la evaluacion: ', self )
        self.label_imagen = QtGui.QLabel( self )

        # TextFields
        self.textField_cadenaEvaluar = QtGui.QLineEdit( self )
        self.textField_resultadoEvaluar = QtGui.QLineEdit ( self )

        # Buttons
        self.btn_comenzar = QtGui.QPushButton( 'Comenzar', self )

    # Diseno de Componentes en la Ventana

        self.label_titulo.setFont(QtGui.QFont('SansSerif', 14))
        self.label_titulo.setGeometry( 190, 65, 300, 50 )

        self.label_imagen.setGeometry( 100, 120, 500, 190 )
        self.label_imagen.setPixmap(QtGui.QPixmap("captura.jpg"))

        self.label_alfabeto.setGeometry( 100, 320, 150, 50 )

        self.label_cadenaEvaluar.setGeometry( 100, 360, 200, 50 )
        self.textField_cadenaEvaluar.setGeometry( 280, 377, 290, 20 )

        self.btn_comenzar.setGeometry( 100, 420, 150, 30 )
        self.btn_comenzar.clicked.connect( self.verResultado )

        self.label_resultadoEvaluar.setGeometry( 100, 460, 150, 50 )
        self.textField_resultadoEvaluar.setGeometry( 240, 477, 290, 20 )
        
        self.show()

    ##
    # Metodo para salir de la aplicacion
    ##
    def cierra_aplicacion( self ):
        opcion = QtGui.QMessageBox.question(
            self, 'Salir de la Aplicacion', 'Estas seguro de salir', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if opcion == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            # Opcion Para no hacer nada
            pass
    
    def verResultado( self ):

        automata = Automata("Angel", "Rebollo")
        print "mi objeto con nombre ", automata.nombre, " y apellido ", automata.apellido
        automata.logica()

##
# Metodo Main
##
def main():

    # Comandos para iniciar la ventana grafica
    app = QtGui.QApplication(sys.argv)
    # Creacion de un objeto de la clase ventana
    GUI = Ventana()

    sys.exit(app.exec_())

main()
