import sys
from PyQt4 import QtGui
from UAMI import Uami
#from Automata_AFND_e import AFND_e


class Ventana(QtGui.QMainWindow):
    ##
    # Constructor de la Ventana
    ##
    def __init__(self):
        super(Ventana, self).__init__()
        self.fuenteUrl = ""

        # Config Ventana
        self.setGeometry(350, 50, 630, 570)
        self.setWindowTitle("Practica4 Analizador Lexicgrafico")
        self.setWindowIcon(QtGui.QIcon("img/logo.png"))

        #Evento para abrir los archivos
        self.EventoAbrirLocal = QtGui.QAction(QtGui.QIcon("img/open.png"), 'Abrir un Archivo', self )
        self.EventoAbrirLocal.setShortcut("Ctrl+O")
        self.EventoAbrirLocal.triggered.connect(self.abrirArchivo)

        # Evento Salir
        self.EventoSalir = QtGui.QAction(QtGui.QIcon(
            "img/salir.png"), "Salir del Programa", self)
        self.EventoSalir.setShortcut("Ctrl+Q")
        self.EventoSalir.setStatusTip('Salir de la aplicacion')
        self.EventoSalir.triggered.connect(self.cierraAplicacion)

        #Evento para compilar
        self.EventoCompilar = QtGui.QAction(QtGui.QIcon("img/comp.png"), 'compilar',self)
        self.EventoCompilar.setShortcut("Ctrl+R")
        self.EventoCompilar.setStatusTip('Inicia la compilacion')
        self.EventoCompilar.triggered.connect(self.iniciarCompilacion)

        # Config del Menu Principal
        self.MenuPrincipal = self.menuBar()

        # Se crea el menu archivo y se agregan los eventos
        self.MenuArchivo = self.MenuPrincipal.addMenu('&Archivo')
        self.MenuArchivo.addAction(self.EventoSalir)
        self.MenuArchivo.addAction(self.EventoCompilar)
        self.MenuArchivo.addAction(self.EventoAbrirLocal)

        # Se crea el Toolbar y se agregan los eventos
        self.Toolbar = self.addToolBar("Archivo")
        self.Toolbar.addAction(self.EventoAbrirLocal)
        self.Toolbar.addAction(self.EventoSalir)
        self.Toolbar.addAction(self.EventoCompilar)
        
        self.diseno()

    ##
    # LLenado de la Ventana
    ##
    def diseno(self):
        ##
        #  Componentes
        ###

        #Cajas de texto
        self.txtAreaFuente = QtGui.QTextEdit(self)
        self.txtAreaResultado  = QtGui.QTextEdit(self)
        self.txtAreaFuente.setGeometry(120,60,500,220)
        self.txtAreaResultado.setGeometry(120,334,500,220)

        #Labels
        self.lbl_Fuente = QtGui.QLabel("Contenido del \narchivo fuente: ",self)
        self.lbl_Fuente.setGeometry(20,100,100,60)
        self.lbl_Fuente.setFont(QtGui.QFont('SansSerif', 11))
       
        self.lbl_Resultado = QtGui.QLabel("Resultados de \ncompilacion: ",self)
        self.lbl_Resultado.setGeometry(20,400,100,60)
        self.lbl_Resultado.setFont(QtGui.QFont('SansSerif', 11))
        self.show()

    ##
    # Metodo para salir de la aplicacion
    ##
    def cierraAplicacion( self ):
        opcion = QtGui.QMessageBox.question(
            self, 'Salir de la Aplicacion', 'Estas seguro de salir', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if opcion == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
    
    ##
    # Metodo para abrir el archivo
    # #    
    def abrirArchivo(self):
            self.txtAreaFuente.setText("")
            self.txtAreaResultado.setText("")
            self.fuenteUrl = QtGui.QFileDialog.getOpenFileName(self, 'Open File', filter="*.fte")     
            f = open(self.fuenteUrl, "r")
            self.vTextstring = f.read()
            self.txtAreaFuente.setText(self.vTextstring)
    
    ##
    #Metodo para el compilador
    ##
    def iniciarCompilacion(self):
        
        uami = Uami()
        uami.iniciaCompilacion( self.fuenteUrl, self.txtAreaFuente )

        archivo = open( uami.archivoTpl, "r")
        contenido_t = archivo.read()

        uami.cierraArchivo( archivo )
        self.txtAreaResultado.setText( contenido_t )
    
    
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
