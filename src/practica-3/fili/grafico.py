import sys
from PyQt4 import QtGui
from Automata_AFND import AFND
from Automata_AFND_e import AFND_e


class Ventana (QtGui.QMainWindow):

    ##
    # Constructor de la Ventana
    ##
    def __init__(self):
        super(Ventana, self).__init__()

        # Config Ventana
        self.setGeometry(350, 50, 550, 670)
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
        self.label_titulo = QtGui.QLabel( 'Automata Finito NO Determinista (AFND)', self )
        self.label_alfabeto = QtGui.QLabel( 'Lenguaje Sigma = { 0, 1 }', self )
        self.label_cadenaEvaluar = QtGui.QLabel( 'Proporcione una cadena a evaluar: ', self )
        self.label_selectAutomata = QtGui.QLabel( 'Selecciona el tipo de automata: ', self )
        self.label_resultadoEvaluar = QtGui.QLabel ( 'Resultado de la evaluacion: ', self )
        self.label_imagen = QtGui.QLabel( self )

        # TextFields
        self.textField_cadenaEvaluar = QtGui.QLineEdit( self )
        self.textArea_resultadoEvaluar = QtGui.QTextEdit( self )

        # ComboBox
        self.cb_selectAutomata = QtGui.QComboBox( self )
        self.cb_selectAutomata.addItems( ['', 'AFND', 'AFND-e'] )

        # Buttons
        self.btn_comenzar = QtGui.QPushButton( 'Comenzar', self )

    # Diseno de Componentes en la Ventana

        self.label_titulo.setFont(QtGui.QFont('SansSerif', 14))
        self.label_titulo.setGeometry( 80, 65, 350, 50 )

        self.label_imagen.setGeometry( 120, 90, 500, 190 )
        self.label_imagen.setPixmap(QtGui.QPixmap(""))

        self.label_alfabeto.setGeometry( 50, 250, 150, 50 )

        self.label_cadenaEvaluar.setGeometry( 50, 270, 200, 50 )
        self.textField_cadenaEvaluar.setGeometry( 230, 285, 290, 20 )

        self.label_selectAutomata.setGeometry( 50, 315, 150, 30 )
        self.cb_selectAutomata.setGeometry( 210, 320, 290, 20 )
        self.cb_selectAutomata.currentIndexChanged.connect( self.cambiaImagen )

        self.btn_comenzar.setGeometry( 50, 345, 150, 30 )
        self.btn_comenzar.clicked.connect( self.verResultado )

        self.label_resultadoEvaluar.setGeometry( 50, 370, 150, 50 )
        self.textArea_resultadoEvaluar.setGeometry( 190, 387, 290, 200 )
        
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
    # del automata en la aplicacion
    ##
    def verResultado( self ):

        cadAutomata = self.cb_selectAutomata.currentText()
        cadena = self.textField_cadenaEvaluar.text()

        if cadAutomata == '':
            QtGui.QMessageBox.critical( self, "NO VALIDO", "Error: Selecciona un automata")
        
        elif cadAutomata == "AFND":
            self.validaAFND( cadena )

        elif cadAutomata == "AFND-e":
            self.validaAFND_e( cadena )

    ##
    # Metodo para Validar la logica del
    # Automata tipo AFND
    # @Param: String
    # con la cadena a evaluar en el automata
    ##
    def validaAFND( self, cadena ):
        contador = 0

        # Se valida que la cadena solo sean 1 y 0
        for letra in cadena:
            if letra != "1" and letra != "0":
                contador = contador + 1
        
        # Se muestra error en caso de haber caracteres distintos de 0 y 1
        if contador > 0:
            QtGui.QMessageBox.critical( self , "Error", "Cadena Invalida")
            contador = 0
            self.textArea_resultadoEvaluar.setText("")

        # Se muestra error en caso de cadena vacia
        elif cadena == '':
            QtGui.QMessageBox.critical( self , "Error", "Cadena Vacia")
            contador = 0
            self.textArea_resultadoEvaluar.setText("")

        # Se inicia el Automata
        else:
            afnd = AFND()
            lista = []
            
            afnd.vueltaAtras( cadena )

            mensaje = ""

            for lista in afnd.Listas:
                mensaje = mensaje + " ".join(lista).replace(" ", "->").replace("Camino->Invalido", "Camino Invalido").replace("Camino->VALIDO", "Camino VALIDO") + "\n\n"

            self.textArea_resultadoEvaluar.setText(str(mensaje))
    
    ##
    # Metodo para Validar la logica del
    # Automata tipo AFND-e
    # @Param: String
    # con la cadena a evaluar en el automata
    ##
    def validaAFND_e( self, cadena ):
        contador = 0

        # Se valida que la cadena solo sean 1, 0 y espacio vacio
        for letra in cadena:
            if letra != "1" and letra != "0" and letra != "":
                contador = contador + 1
        
        # Se muestra error en caso de haber caracteres distintos de 0 y 1
        if contador > 0:
            QtGui.QMessageBox.critical( self , "Error", "Cadena Invalida")
            contador = 0
            self.textArea_resultadoEvaluar.setText("")

        # Se inicia el Automata
        else:
            contador = 0
            afnd_e = AFND_e()
            res = afnd_e.edo_Q0( cadena )
            afnd_e.Listas

            mensaje = ""

            for lista in afnd_e.Listas:
                mensaje = mensaje + " ".join(lista).replace(" ", "->") + "\n\n"

            mensaje = res + "\n\n" + mensaje

            self.textArea_resultadoEvaluar.setText(str(mensaje))

    
    ##
    # Metodo para cambiar la imagen 
    # del automata en la aplicacion
    ##
    def cambiaImagen( self ):

        cadAutomata = self.cb_selectAutomata.currentText()

        # Sin imagen
        if cadAutomata == '':
            self.label_imagen.setPixmap(QtGui.QPixmap(""))
        
        # Imagen para el AFND
        elif cadAutomata == "AFND":
            self.label_imagen.setPixmap(QtGui.QPixmap("afnd.jpg"))
            self.label_imagen.setGeometry( 120, 90, 500, 190 )

            self.label_alfabeto.setGeometry( 50, 250, 150, 50 )

            self.label_cadenaEvaluar.setGeometry( 50, 270, 200, 50 )
            self.textField_cadenaEvaluar.setGeometry( 230, 285, 290, 20 )

            self.label_selectAutomata.setGeometry( 50, 315, 150, 30 )
            self.cb_selectAutomata.setGeometry( 210, 320, 290, 20 )

            self.btn_comenzar.setGeometry( 50, 345, 150, 30 )

            self.label_resultadoEvaluar.setGeometry( 50, 370, 150, 50 )
            self.textArea_resultadoEvaluar.setGeometry( 190, 387, 290, 200 )

        # Imagen para el afnd-e
        elif cadAutomata == "AFND-e":

            self.label_imagen.setPixmap(QtGui.QPixmap("afnd-e.jpg"))
            self.label_imagen.setGeometry( 150, 120, 500, 200 )

            self.label_alfabeto.setGeometry( 50, 310, 150, 50 )

            self.label_cadenaEvaluar.setGeometry( 50, 330, 200, 50 )
            self.textField_cadenaEvaluar.setGeometry( 230, 345, 290, 20 )

            self.label_selectAutomata.setGeometry( 50, 375, 150, 30 )
            self.cb_selectAutomata.setGeometry( 210, 380, 290, 20 )

            self.btn_comenzar.setGeometry( 50, 405, 150, 30 )

            self.label_resultadoEvaluar.setGeometry( 50, 430, 150, 50 )
            self.textArea_resultadoEvaluar.setGeometry( 190, 447, 290, 200 )
        
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
