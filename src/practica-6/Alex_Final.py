import sys
from PyQt4 import QtGui
from UAMI import Uami


class Ventana(QtGui.QMainWindow):


    ##
    # Constructor de la Ventana
    ##
    def __init__(self):
        super(Ventana, self).__init__()

        # Direccion Url del archivo fuente
        self.fuenteUrl = ""

        # Config Ventana
        self.setGeometry(350, 50, 630, 570)
        self.setWindowTitle("Practica5 Analizador Lexicgrafico")
        self.setWindowIcon(QtGui.QIcon("img/logo.png"))

        # Evento para abrir los archivos
        self.EventoAbrirLocal = QtGui.QAction(QtGui.QIcon("img/open.png"), 'Abrir un Archivo', self )
        self.EventoAbrirLocal.setShortcut("Ctrl+O")
        self.EventoAbrirLocal.triggered.connect(self.abrirArchivo)

        # Evento Salir
        self.EventoSalir = QtGui.QAction(QtGui.QIcon(
            "img/salir.png"), "Salir del Programa", self)
        self.EventoSalir.setShortcut("Ctrl+Q")
        self.EventoSalir.setStatusTip('Salir de la aplicacion')
        self.EventoSalir.triggered.connect(self.cierraAplicacion)

        # Evento para compilar
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
    # LLenado y ubicacion de los componentes
    # en la ventana
    ##
   
    def diseno(self):
        
        # Cajas de texto (text Areas)
        self.txtAreaFuente = QtGui.QTextEdit(self)
        self.txtAreaFuente.setGeometry(120,60,500,220)

        self.txtAreaResultado  = QtGui.QTextEdit(self)
        self.txtAreaResultado.setGeometry(120,334,500,220)

        # etiquetas (Labels)
        self.lbl_Fuente = QtGui.QLabel("Contenido del \narchivo fuente: ",self)
        self.lbl_Fuente.setGeometry(20,100,100,60)
        self.lbl_Fuente.setFont(QtGui.QFont('SansSerif', 11))
       
        self.lbl_Resultado = QtGui.QLabel("Resultados de \ncompilacion: ",self)
        self.lbl_Resultado.setGeometry(20,400,100,60)
        self.lbl_Resultado.setFont(QtGui.QFont('SansSerif', 11))
        self.show()

    ##
    # Metodo para salir de la aplicacion
    # ya sea por el toolbar, menu o shortcut
    ##
    def cierraAplicacion( self ):
        opcion = QtGui.QMessageBox.question(
            self, 'Salir de la Aplicacion', 'Estas seguro de salir', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if opcion == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
    
    ##
    # Metodo para abrir el archivo fuente
    # mediante el dialogo de python
    # #    
    def abrirArchivo( self ):
    
            # Direccion del archivo Seleccionado en el Dialogo de python
            self.fuenteUrl = QtGui.QFileDialog.getOpenFileName(self, 'Open File', filter="*.fte")    
            
            # Si se selecciono algun archivo en el dialogo
            # se imprime el contenido en la caja de texto
            # del archivo fuente
            if self.fuenteUrl:
                archivo = open(self.fuenteUrl, "r")
                self.txtAreaFuente.setText( archivo.read() )
                archivo.close()
    
    ##
    # Metodo que inicia la compilacion
    # en la ventana
    ##
    def iniciarCompilacion( self ):
        
        # Inicia la compilacion del objeto uami
        uami = Uami()
        uami.iniciaCompilacion( self.fuenteUrl, self.txtAreaFuente )

        # Lee el archivo tupla generado por el analizador lexicografico
        # y los imprime en la caja de texto del resultado
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
