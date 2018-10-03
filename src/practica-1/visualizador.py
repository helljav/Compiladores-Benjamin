
# coding=utf-8

# importa el módulo sys
import sys

# Libreria de expresiones regulares
import re

# importa el sub-módulo QtGui del módulo PyQt4
from PyQt4 import QtGui

cCadena = 0
cEntero = 0
cChar = 0
cFloat = 0
cBoolean = 0

# Metodo que verifica si el termino es un digito (0-9)
def esDigito(termino):    
    # Exp. Regular de entre 0 y 9
    numeros = re.compile('[0-9]')
    
    # si el termino es un digito
    # search regresa el numero de ocurrencias en la Exp. Regular
    if numeros.search(termino) > 0:
            return True
    return False

# Metodo que verifica si el termino es un numero Flotante
def esFlotante(termino):
    
    # Exp. Regular de entre 0 y 9 fija un punto y entre 0-9
    flotantes = re.compile('[0-9].[0-9]')
    
    # si el termino es un flotante
    # search regresa el numero de ocurrencias en la Exp. Regular
    if flotantes.search(termino) > 0:
            return True
    return False

def esCadena(termino):

    # Expresion regular tipo estrella de klean a la z min y A a la Z
    letras = re.compile('[a-zA-Z]')

    if letras.search(termino) > 0:
            return True
    else:
        return False

# Metodo pra saber los tipos
def tipoVariable(termino):

    # Determinar si es el termino tiene longitud 1
    # y no es un digito
    if len(termino) == 1 and esDigito(termino) == False:
        
        global cChar
        cChar = cChar + 1

    else:
        # Compara si el termino corresponde a un boolean
        if termino == 'True' or termino == 'False':
            
            global cBoolean
            cBoolean = cBoolean + 1

        else:
            # Verifica si es un numero 
            if esDigito(termino) == True:
                # Verifica si es flotante (que haya un punto)
                if esFlotante(termino) == True:
                    
                    global cFloat
                    cFloat = cFloat + 1
                else:
                    # Si no hay punto es un entero
                    global cEntero
                    cEntero = cEntero + 1
            else:
                # Si no es todo lo anterior es cadena
                if esCadena(termino) == True:
                    
                    global cCadena
                    cCadena = cCadena + 1

    
       
# Clase Ventana que hereda de QtGui.QMainWindow
class Ventana (QtGui.QMainWindow):

    # Constructor de la Ventana
    def __init__(self):

        # Se ejecuta el Constructor de la clase Padre
        super(Ventana, self).__init__()

        # Se Define la posicion y tamaño para el Grafico
        self.setGeometry(50, 50, 700, 500)
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
        self.openfile = QtGui.QAction(QtGui.QIcon("open.png"), '&Abrir Archivo', self)
        self.openfile.setShortcut("Ctrl+O")
        self.openfile.setStatusTip('Abrir Archivo')
        # Desencadenador de Evento
        self.openfile.triggered.connect(self.abrir_archivo)

        # Se agrega un evento para salir
        self.EventoSalir = QtGui.QAction(QtGui.QIcon("salir.png"), "&Salir", self)
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
        #boton para poder desplegar el numero de tokens
        self.btn_tokens = QtGui.QPushButton("Contar tokens",self)
        # Area de texto para el archivo
        self.Resultados = QtGui.QTextEdit(self)
        #labels
        self.lbl_ints = QtGui.QLabel('Numero de tokens tipo int ',self)
        self.lbl_float = QtGui.QLabel('Numero de tokens tipo float',self)
        self.lbl_string = QtGui.QLabel('Numero de tokens tipo String',self)
        self.lbl_char = QtGui.QLabel('Numero de tokens tipo char',self)
        self.lbl_boolean = QtGui.QLabel('Numero de tokens tipo booleans',self)

        #Area de  para las cajas de texto (numero de tokens)
        self.box_int  = QtGui.QLineEdit(self)
        self.box_float  = QtGui.QLineEdit(self)
        self.box_boolean  = QtGui.QLineEdit(self)
        self.box_char  = QtGui.QLineEdit(self)
        self.box_string  = QtGui.QLineEdit(self)


        

        # creamos una barra de opciones para salir
        # Lo que va en comillas simples es lo que queremos que se despliegue
        # al poner el raton sobre la barra

        EventoAbrirLocal = QtGui.QAction(QtGui.QIcon("open.png"), 'Abrir un Archivo', self)
        EventoAbrirLocal.triggered.connect(self.abrir_archivo)

        self.BarraOpciones = self.addToolBar("Archivo")
        self.BarraOpciones.addAction(EventoAbrirLocal)

        self.EventoSalirLocal = QtGui.QAction(
            QtGui.QIcon('salir.png'), 'Salir del Programa', self)
        self.EventoSalirLocal.triggered.connect(self.cierra_aplicacion)
        self.BarraOpciones.addAction(self.EventoSalirLocal)
        
        #Evento para el boton
        self.btn_tokens.clicked.connect(self.despliegaContadores)

        # Lo que va en el parentesis es (eje x, eje y)
        # Configuracion de tamaño y ubicacion de los elementos en el Grafico
        self.btn_tokens.resize(120,40)
        self.btn_tokens.move(450,66)

        self.Resultados.resize(400, 420)
        self.Resultados.move(10, 65)

        self.lbl_ints.resize(420,20)
        self.lbl_float.resize(420,20)
        self.lbl_boolean.resize(420,20)
        self.lbl_char.resize(420,20)
        self.lbl_string.resize(420,20)

        self.lbl_ints.move(450,120)
        self.lbl_float.move(450,190)
        self.lbl_boolean.move(450,260)
        self.lbl_char.move(450,330)
        self.lbl_string.move(450,400)

        self.box_int.resize(250,25)
        self.box_float.resize(250,25)
        self.box_boolean.resize(250,25)
        self.box_char.resize(250,25)
        self.box_string.resize(250,25)


        self.box_int.move(420,155)
        self.box_float.move(420,225)
        self.box_boolean.move(420,295)
        self.box_char.move(420,365)
        self.box_string.move(420,435)

        # Hace Visible el Grafico
        self.show()
    #

    def despliegaContadores(self):
        self.box_int.setText(str(cEntero) )
        self.box_float.setText(str(cFloat))
        self.box_boolean.setText(str(cBoolean))
        self.box_char.setText(str(cChar))
        self.box_string.setText(str(cCadena))



    def abrir_archivo(self):
        vOpenfilename = QtGui.QFileDialog.getOpenFileName(
            self, 'Open File', filter="*.txt")

        if(vOpenfilename == ""):
            return

        f = open(vOpenfilename, "r")
        vTextstring = f.read()
        self.Resultados.setText(vTextstring)
        #en ñla variable vTextstring almacena toda la cadena del arcchivo de texto
        #Con la funcion split se dividimos las palablas apartir de un espacio y se almacena
        #en un arreglo (palabras)

        vTextstring = vTextstring.replace('\n',' ')
        self.palabras = vTextstring.split(" ")
        
        for termino in self.palabras:
            tipoVariable(termino)
        #se declaran estas variables de esta forma para poder utilizarlos en este metodo
        global cCadena
        global cEntero
        global cChar
        global cFloat
        global cBoolean

        f.close() #cierra el archivo
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
