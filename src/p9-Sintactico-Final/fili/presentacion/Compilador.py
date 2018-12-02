import sys
import os
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
        self.setGeometry(250, 50, 880, 670)
        self.setWindowTitle("Compilador Uami")
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
        # Evento Save
        self.EventoSave = QtGui.QAction(QtGui.QIcon(
            "img/save.png"), "Guardar", self)
        self.EventoSave.setShortcut("Ctrl+g")
        self.EventoSave.setStatusTip('Guardar archivo fuente')
        self.EventoSave.triggered.connect(self.guardarArchivo)
        # Evento SaveAS
        self.EventoSaveAs = QtGui.QAction(QtGui.QIcon(
            "img/saveAs.png"), "Guardar como", self)
        self.EventoSaveAs.setShortcut("Ctrl+s")
        self.EventoSaveAs.setStatusTip('Guardar como el archivo fuente')
        self.EventoSaveAs.triggered.connect(self.guardarArchivoAs)

        # Evento para compilar
        self.EventoCompilar = QtGui.QAction(QtGui.QIcon("img/comp.png"), 'Compilar',self)
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
        self.MenuArchivo.addAction(self.EventoSave)
        self.MenuArchivo.addAction(self.EventoSaveAs)


        # Se crea el Toolbar y se agregan los eventos
        self.Toolbar = self.addToolBar("Archivo")
        self.Toolbar.addAction(self.EventoAbrirLocal)
        self.Toolbar.addAction(self.EventoSalir)
        self.Toolbar.addAction(self.EventoCompilar)
        self.Toolbar.addAction(self.EventoSave)
        self.Toolbar.addAction(self.EventoSaveAs)
        
        self.diseno()

    ##
    # LLenado y ubicacion de los componentes
    # en la ventana
    ##
   
    def diseno(self):
        
        # Cajas de texto (text Areas)
        self.txtAreaFuente = QtGui.QTextEdit(self)
        self.txtAreaFuente.setGeometry(10,85,425,270)

        self.txtAreaFileError = QtGui.QTextEdit(self)
        self.txtAreaFileError.setGeometry(10,380,425,270)

        self.txtAreaResultado  = QtGui.QTextEdit(self)
        self.txtAreaResultado.setGeometry(445,380,425,270)

        self.txtAreaFileTupla  = QtGui.QTextEdit(self)
        self.txtAreaFileTupla.setGeometry(445,85,425,270)

        # etiquetas (Labels)
        self.lbl_Fuente = QtGui.QLabel("CONTENIDO DEL ARCHIVO FUENTE: ",self)
        self.lbl_Fuente.setGeometry(80,40,300,60)
        self.lbl_Fuente.setFont(QtGui.QFont('SansSerif', 11))
       
        self.lbl_fileError = QtGui.QLabel("CONTENIDO DEL ARCHIVO ERROR: ",self)
        self.lbl_fileError.setGeometry(80,335,300,60)
        self.lbl_fileError.setFont(QtGui.QFont('SansSerif', 11))

        self.lbl_compilacion = QtGui.QLabel("RESULTADO DE LA COMPILACION: ",self)
        self.lbl_compilacion.setGeometry(550,335,300,60)
        self.lbl_compilacion.setFont(QtGui.QFont('SansSerif', 11))

        self.lbl_fileTupla = QtGui.QLabel("CONTENIDO DEL ARCHIVO TUPLA: ",self)
        self.lbl_fileTupla.setGeometry(550,40,300,60)
        self.lbl_fileTupla.setFont(QtGui.QFont('SansSerif', 11))
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
    # Metodo para guardar el archivo fuente
    # ya sea por el toolbar, menu o shortcut
    ##
    def guardarArchivo( self ):

        # Guarda archivosi ya existe
        if self.fuenteUrl:
            archivo = open(self.fuenteUrl, "w")
            texto = self.txtAreaFuente.toPlainText()
            archivo.write(texto)
            archivo.close()
        
        # Guardar como si no existe el archivo
        else:
            url = str( QtGui.QFileDialog.getSaveFileName(self, 'Guardar Archivo', filter="*.fte") )

            if url:
                    # Si no termina en .fte
                    if url.endswith(".fte") == False:
                        pos_ini = url.find(".")
                        pos_final = len(url)
                        url = url.replace( url[pos_ini:pos_final], ".fte" )
                        

                    archivo = open( url,'w')
                    texto = self.txtAreaFuente.toPlainText()
                    archivo.write(texto)
                    archivo.close()
                    self.fuenteUrl = url
            

    ##
    # Metodo para guardar el archivo fuente
    # ya sea por el toolbar, menu o shortcut
    ##
    def guardarArchivoAs( self ):
        
        # urlActual = self.fuenteUrl

        url = str( QtGui.QFileDialog.getSaveFileName(self, 'Guardar Archivo Como', filter="*.fte") )

        if url:
                # Si no termina en .fte
                if url.endswith(".fte") == False:
                    pos_ini = url.find(".")
                    pos_final = len(url)
                    url = url.replace( url[pos_ini:pos_final], ".fte" )
                    

                archivo = open( url,'w')
                texto = self.txtAreaFuente.toPlainText()
                archivo.write(texto)
                archivo.close()

                self.fuenteUrl = url

                # if urlActual:
                #     self.fuenteUrl = urlActual
                # else:
                #     self.fuenteUrl = url
        
        

    
    ##
    # Metodo para abrir el archivo fuente
    # mediante el dialogo de python
    # #    
    def abrirArchivo( self ):

            urlActual = self.fuenteUrl
            # Direccion del archivo Seleccionado en el Dialogo de python
            self.fuenteUrl = QtGui.QFileDialog.getOpenFileName(self, 'Abrir Archivo', filter="*.fte")    
            
            # Si se selecciono algun archivo en el dialogo
            # se imprime el contenido en la caja de texto
            # del archivo fuente
            if self.fuenteUrl:
                archivo = open(self.fuenteUrl, "r")
                self.escribirAreaFuente(archivo.read())
                self.escribirAreaErrores("")
                self.escribirAreaResultado("")
                self.escribirAreaTupla("")
                archivo.close()
            else:
                self.fuenteUrl = urlActual

    def escribirAreaFuente( self, texto ):
        self.txtAreaFuente.setText( texto )
    
    def getTextAreaFuente( self ):
        return self.txtAreaFuente.toPlainText()


    def escribirAreaResultado( self, texto ):
        self.txtAreaResultado.setText( texto )
    
    def getTextAreaResultado( self ):
        return self.txtAreaResultado.toPlainText()


    def escribirAreaErrores( self, texto ):
        self.txtAreaFileError.setText( texto )
    
    def getTextAreaErrores( self ):
        return self.txtAreaFileError.toPlainText()
        
    
    def escribirAreaTupla( self, texto ):
        self.txtAreaFileTupla.setText( texto )
    
    def getTextAreaTupla( self ):
        return self.txtAreaFileTupla.toPlainText()

    
    ##
    # Metodo que inicia la compilacion
    # en la ventana
    ##
    def iniciarCompilacion( self ):
        uami = Uami( self )
        uami.iniciaCompilacion()

