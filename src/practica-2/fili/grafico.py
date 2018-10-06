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
        self.setGeometry(350, 100, 550, 420)
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
        self.label_titulo.setGeometry( 120, 65, 300, 50 )

        self.label_imagen.setGeometry( 120, 90, 500, 190 )
        self.label_imagen.setPixmap(QtGui.QPixmap("captura.jpg"))

        self.label_alfabeto.setGeometry( 50, 250, 150, 50 )

        self.label_cadenaEvaluar.setGeometry( 50, 270, 200, 50 )
        self.textField_cadenaEvaluar.setGeometry( 230, 285, 290, 20 )

        self.btn_comenzar.setGeometry( 50, 315, 150, 30 )
        self.btn_comenzar.clicked.connect( self.verResultado )

        self.label_resultadoEvaluar.setGeometry( 50, 350, 150, 50 )
        self.textField_resultadoEvaluar.setGeometry( 190, 367, 290, 20 )
        
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
            pass
    
    ##
    # Metodo para mostrar resultado de la evaluacion 
    # en el field de la aplicacion
    ##
    def verResultado( self ):

        cadena = self.textField_cadenaEvaluar.text();
        contador = 0
        
        # Se valida que la cadena solo sean 1 y 0
        for letra in cadena:
            if letra != "1" and letra != "0":
                contador = contador + 1
        
        # Se muestra error en caso de haber caracteres distintos de 0 y 1
        if contador > 0:
            QtGui.QMessageBox.critical( self , "Error", "Cadena Invalida")
            contador = 0
            self.textField_resultadoEvaluar.setText("")

        # Se muestra error en caso de cadena vacia
        elif cadena == '':
            QtGui.QMessageBox.critical( self , "Error", "Cadena Vacia")
            contador = 0
            self.textField_resultadoEvaluar.setText("")

        # Se inicia el Automata
        else:
            contador = 0
            lista = []
            automata = Automata()

            # En caso de empezar con 0
            if cadena[ contador ] == "0":

                res = automata.edo_Q1( cadena, contador, lista )

                if res[0] == True:
                    self.textField_resultadoEvaluar.setText("La cadena: " + cadena + ", SI es Valida: "+ str( res[1] ) )
                else:
                    self.textField_resultadoEvaluar.setText("La cadena: " + cadena + ", NO es Valida: "+ str( res[1] ) )

            # En caso de empezar con 1
            elif cadena[ contador ] == "1":

                res = automata.edo_Q0( cadena, contador, lista )

                if res[0] == True:
                    QtGui.QMessageBox.information( self, "VALIDO", "La cadena: " + cadena + ", SI ES ACEPTADA ")
                    self.textField_resultadoEvaluar.setText( str( res[1] ) )
                else:
                    QtGui.QMessageBox.critical( self, "NO VALIDO", "La cadena: " + cadena + ", NO ES ACEPTADA")
                    self.textField_resultadoEvaluar.setText( str( res[1] ) )

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
