import os
from Alex import Alex
from PR import Palabras_Reservadas

class Uami(object):

    ##
    # Constructor
    ##
    def __init__( self, ventana ):

        # Inyeccion de Dependencias
        self.ventana = ventana
        self.pr = Palabras_Reservadas()
        self.alex = Alex( self.ventana, self.pr, self )


        self.archivoTpl = ""
        self.archivoErr = ""
        self.lineas = 0
        self.errores = 0

    ##
    # Metodo para crear los archivos de la tupla y error
    #
    #   @Param self.ventana.fuenteUrl: 
    #       Ruta del archivo fuente (el que se abre)
    #   @Param self.ventana.txtAreaFuente: 
    #       El componente Gui correspondiente a la Caja de texto
    #       del archivo fuente
    ##
    def crearArchivos( self ):

        # Obtener nombre del archivo fuente
        lista = str(self.ventana.fuenteUrl).split("/")
        nombreFuente = lista[len(lista)-1].replace(".fte", "")

        # Si no se abre algun archivo fuente, se predefine un nombre
        if nombreFuente is "":
            nombreFuente = "untitle"
        
        #ruta para la carpeta de distribucion
        urlDist =  os.getcwd().replace("\\", "/") + "/dist/"

        # si no existe la carpera "dist", se crea
        if not os.path.exists(urlDist):
            os.makedirs(urlDist)
        
        # Creacion de las rutas para los archivos
        self.archivoTpl = urlDist +  nombreFuente + ".tpl"
        self.archivoErr = urlDist +  nombreFuente + ".err"

        # Texto Default para el archivo tupla
        textoTupla = [
                        "En este archivo se encuentran los lexemas reconocidos\n",
                        "por el analizador lexicografico\n",
                        "\n\n",
                        "Linea",
                        "\t",
                        "Token",
                        "\t\t",
                        "Lexema",
                        "\n\n"
                     ]

        # Texto Default para el archivo error
        textoError = "* Detalles de Error de Compilacion*\n\n"
        
        # Se crean los archivos en las rutas correspondientes
        # y se escribe el texto default en ellos
        self.escribirArchivo( self.archivoTpl, "w+", textoTupla )
        self.ventana.txtAreaFileTupla.setText( self.getArchivoTexto( self.archivoTpl ) )
        
        self.escribirArchivo( self.archivoErr, "w+", textoError )
        self.ventana.txtAreaFileError.setText( self.getArchivoTexto( self.archivoErr ) )

    ##
    # Metodo para escribir en un archivo
    # @Param ruta: ruta del archivo
    # @Param modo: tipo de escritura requerido
    # @Param texto: el texto a escribir
    ##
    def escribirArchivo( self, ruta, modo, texto ):

        archivo = open( ruta , modo)

        if type(texto) == type(list()):
            archivo.writelines(texto)
            return archivo
        else:
            archivo.write( texto )
            return archivo
        
        archivo.close()

    ##
    # Metodo para obtener el contenido de un archivo
    # @Param ruta: ruta del archivo
    # @Return texto: el texto del archivo
    ##
    def getArchivoTexto( self, ruta ):
        archivo = open( ruta , "r")
        texto = archivo.read()
        archivo.close()
        return str(texto)
    
    ##
    # Metodo para inicial el analizador lexicografico
    #
    #   @Param self.ventana.fuenteUrl: 
    #       Ruta del archivo fuente (el que se abre)
    #   @Param uami: 
    #       referencia de memoria de un objeto uami
    ##
    def iniciaCompilacion( self ):
        
        cadRes = ""

        while self.ventana.fuenteUrl == "":
            self.ventana.guardarArchivo()

        cadRes += "Inicia Compilacion: " + str(self.ventana.fuenteUrl) + "\n\n"
        self.ventana.txtAreaResultado.setText( cadRes )
        
        cadRes += "Creando Archivos Tupla y Error\n"
        self.ventana.txtAreaResultado.setText( cadRes )

        self.crearArchivos()
        
        cadRes += "Espere un momento por favor...\n"
        self.ventana.txtAreaResultado.setText( cadRes )

        diccionario = self.alex.alexico()

        # Cuando sea Aceptado el token
        while diccionario["token"] != self.pr.HECHO:

            if diccionario["token"] == "DELIMITADOR":
                pass
                
            # Cuando sea Error Token invalido
            if diccionario["token"] == self.pr.TOKEN_INV:

                texto = [
                            "Linea: ",
                            str(self.lineas),
                            "\t",
                            diccionario["token"],
                            "\n\t",
                            diccionario["lexema"] + " no Reconocido",
                            "\n\n"
                        ]

                self.errores += 1 
                cadRes += "<< Error Encontrado >>\n"
                self.ventana.txtAreaResultado.setText( cadRes )
                self.escribirArchivo( self.archivoErr, "a+", texto )
                self.ventana.txtAreaFileError.setText( self.getArchivoTexto( self.archivoErr ) )
            
            # Cuando sea Error lexicografico
            elif diccionario["token"] == self.pr.ERROR:

                texto = [
                            "Linea: ",
                            str(self.lineas),
                            "\t",
                            diccionario["token"],
                            "\n\t",
                            "\"" + diccionario["lexema"] + "\" NO PERMITIDO",
                            "\n\n"
                        ]

                self.errores += 1 
                cadRes += "<< Error Encontrado >>\n"
                self.ventana.txtAreaResultado.setText( cadRes )
                self.escribirArchivo( self.archivoErr, "a+", texto )
                self.ventana.txtAreaFileError.setText( self.getArchivoTexto( self.archivoErr ) )
                
            # Pertmitidos
            else: 

                texto = [
                        str(self.lineas),
                        "\t",
                        diccionario["token"],
                        "\t\t",
                        diccionario["lexema"],
                        "\n"
                     ]
                
                self.escribirArchivo( self.archivoTpl, "a+", texto )
                self.ventana.txtAreaFileTupla.setText( self.getArchivoTexto( self.archivoTpl ) )

            diccionario = self.alex.alexico()


        # Cuando sea Fin de Archivo
        if diccionario["token"] == self.pr.HECHO:

            texto = [
                        str(self.lineas),
                        "\t",
                        diccionario["token"],
                        "\t\t",
                        diccionario["lexema"],
                        "\n"
                     ]
                     
            self.escribirArchivo( self.archivoTpl, "a+", texto )
            self.ventana.txtAreaFileTupla.setText( self.getArchivoTexto( self.archivoTpl ) )

        cadRes += "Compilacion Terminada\n\n"  + "Errorres: " +  str(self.errores)
        self.ventana.txtAreaResultado.setText( cadRes )