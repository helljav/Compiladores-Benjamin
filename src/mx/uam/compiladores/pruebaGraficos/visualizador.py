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
        self.setGeometry(50, 50, 520, 500)
        # Se agrega un titulo al Grafico
        self.setWindowTitle("Visualizador de Archivos")
        # Se Agrega un Icono al Grafico
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        #########################################################################
        ###########  Construccion de un Menu en el Grafico  #####################
        ###########                 y                       #####################
        ##########  Construccion de Aperturador de Archivos  ####################
        #########################################################################

        # Aperturador de Archivos
        # Se agrega un evento
        self.openfile = QtGui.QAction(
            QtGui.QIcon("open.png"), '&Abrir Archivo', self)
        self.openfile.setShortcut("Ctrl+O")
        self.openfile.setStatusTip('Abrir Archivo')
        # Desencadenador de Evento
        self.openfile.triggered.connect(self.abrir_archivo)

        # Se agrega un evento para salir
        self.EventoSalir = QtGui.QAction(
            QtGui.QIcon("salir.png"), "&Salir", self)
        self.EventoSalir.setShortcut("Ctrl+Q")
        self.EventoSalir.setStatusTip('Salir de la aplicacion')
        # Desencadenador de Evento
        self.EventoSalir.triggered.connect(self.cierra_aplicacion)

        # Menu
        self.MenuPrincipal = self.menuBar()
        # elementos del Menu
        self.MenuArchivo = self.MenuPrincipal.addMenu('&Archivo')

        # Se agrega un listener o escuchador de evento, recibe el evento "openfile"
        self.MenuArchivo.addAction(self.openfile)

        # Separador
        self.MenuArchivo.addSeparator()

        # Se agrega un listener o escuchador de evento, recibe el evento "EventoSalir"
        self.MenuArchivo.addAction(self.EventoSalir)

        # Se crea el contenifo del Grafico
        self.home()

    #########################################################################
    ##################  Contenido en el Grafico  ############################
    #########################################################################

    def home(self):

        # Bandera para saber que ya abrimos un archivo
        self.bandera_abrir = False

        # Area de texto para el archivo
        self.Resultados = QtGui.QTextEdit(self)

        # creamos una barra de opciones para salir
        # Lo que va en comillas simples es lo que queremos que se despliegue
        # al poner el raton sobre la barra

        EventoAbrirLocal = QtGui.QAction(
            QtGui.QIcon("open.png"), 'Abrir un Archivo', self)
        EventoAbrirLocal.triggered.connect(self.abrir_archivo)

        self.BarraOpciones = self.addToolBar("Archivo")
        self.BarraOpciones.addAction(EventoAbrirLocal)

        self.EventoSalirLocal = QtGui.QAction(
            QtGui.QIcon('salir.png'), 'Salir del Programa', self)
        self.EventoSalirLocal.triggered.connect(self.cierra_aplicacion)
        self.BarraOpciones.addAction(self.EventoSalirLocal)

        # Lo que va en el parentesis es (eje x, eje y)
        self.Resultados.resize(500, 420)
        self.Resultados.move(10, 65)

        # Hace Visible el Grafico
        self.show()
    #

    def abrir_archivo(self):
        vOpenfilename = QtGui.QFileDialog.getOpenFileName(
            self, 'Open File', filter="*.txt")

        if(vOpenfilename == ""):
            return

        f = open(vOpenfilename, "r")
        vTextstring = f.read()
        self.Resultados.setText(vTextstring)
        f.close()
        self.bandera_abrir = True

    # Metodo que cierra el Grafico
    def cierra_aplicacion(self):
        opcion = QtGui.QMessageBox.question(self, 'Salir de la Aplicacion',
                                            'Estas seguro de salir', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if opcion == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            # Opcion Para no hacer nada
            pass

# Metodo main que correr la aplicacion
def main():

    # Comandos para iniciar la ventana grafica

    app = QtGui.QApplication(sys.argv)
    # Creacion de un objeto de la clase ventana
    GUI = Ventana()
    sys.exit(app.exec_())


# Se corre el main
main()
