import sys
from PyQt4 import QtGui
from UAMI import Uami
#from Automata_AFND_e import AFND_e


class Ventana (QtGui.QMainWindow):
    ##
    # Constructor de la Ventana
    ##
    def __init__(self):
        super(Ventana, self).__init__()
        self.URL =""

        # Config Ventana
        self.setGeometry(350, 50, 630, 570)
        self.setWindowTitle("Practica4 Analizador Lexicgrafico")
        self.setWindowIcon(QtGui.QIcon("logo.png"))

        # Config del Menu
        self.MenuPrincipal = self.menuBar()
        self.hearth = QtGui.QAction(QtGui.QIcon("comp.jpg"), '&Compilar', self)
        self.hearth.setShortcut("Crtl+P")
        self.MenuArchivo = self.MenuPrincipal.addMenu('&Archivo')
        self.MenuCompilar = self.MenuPrincipal.addMenu('&Compilar')

        # Barra de opciones
        self.BarraOpciones = self.addToolBar("Archivo")
        #Evento para abrir los archivos
        self.EventoAbrirLocal = QtGui.QAction(QtGui.QIcon("open.png"), 'Abrir un Archivo', self)
        self.EventoAbrirLocal.triggered.connect(self.abrir_archivo)

        # Evento Salir
        self.EventoSalir = QtGui.QAction(QtGui.QIcon(
            "salir.png"), "Salir del Programa", self)
        self.EventoSalir.setShortcut("Ctrl+Q")
        self.EventoSalir.setStatusTip('Salir de la aplicacion')
        self.EventoSalir.triggered.connect(self.cierra_aplicacion)

        #Evento para compilar
        self.EventoCompilar = QtGui.QAction(QtGui.QIcon("comp.png"), 'compilar',self)
        self.EventoCompilar.setStatusTip('Inicia la compilacion')
        self.EventoCompilar.triggered.connect(self.iniciarCompilacion)

        # Se agrega el listener del evento "EventoSalir" al menu
        self.MenuArchivo.addAction(self.EventoSalir)
        # Se agrega el listener de los eventos a la Barra de Opciones
        self.BarraOpciones.addAction(self.EventoAbrirLocal)
        self.BarraOpciones.addAction(self.EventoSalir)
        self.BarraOpciones.addAction(self.EventoCompilar)
        
        self.diseno()

    ##
    # LLenado de la Ventana
    ##
    def diseno(self):
        ##
        #  Componentes
        #
        #Cajas de texto
        self.txb_AF = QtGui.QTextEdit(self)
        self.txb_AG  = QtGui.QTextEdit(self)
        self.txb_AF.setGeometry(120,60,500,220)
        self.txb_AG.setGeometry(120,334,500,220)
        #Labels
        self.lbl_AF = QtGui.QLabel("Contenido del \narchivo fuente: ",self)
        self.lbl_AF.setGeometry(20,100,100,60)
        self.lbl_AF.setFont(QtGui.QFont('SansSerif', 11))
       
        self.lbl_AG = QtGui.QLabel("Resultados de \ncompilacion: ",self)
        self.lbl_AG.setGeometry(20,400,100,60)
        self.lbl_AG.setFont(QtGui.QFont('SansSerif', 11))
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
    # Metodo para abrir el archivo
    # #    
    def abrir_archivo(self):
            self.txb_AF.setText("")
            self.txb_AG.setText("")
            archivo = QtGui.QFileDialog
            self.URL = archivo.getOpenFileName(self, 'Open File', filter="*.fte")
            # print archivo       
            f = open(self.URL, "r")
            self.vTextstring = f.read()
            self.txb_AF.setText(self.vTextstring)
    
    ##
    #Metodo para el compilador
    ##
    def iniciarCompilacion(self):
        
        uami = Uami()
        uami.iniciaCompilacion( self.URL, self.txb_AF )

        
        # Eliminar nombre de archivo abierto y guararlo en lista
        lista = str(self.URL).split("/")
        lista = lista[0:len(lista)-1]
        
        # Generar la url a nivel de la carpeta origen del archivo abierto
        self.URL = '/'.join(str(e) for e in lista) + "/tupla.tpl"

        tupla = open(self.URL, "r")
        contenido_t = tupla.read()

        self.txb_AG.setText( contenido_t )
    
    
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
