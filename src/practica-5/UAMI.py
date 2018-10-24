import os
from Alex import Alex
from PR import Palabras_Reservadas

class Uami(object):

    ##
    # Constructor
    ##
    def __init__( self ):
        
        self.archivoTpl = ""
        self.archivoErr = ""
        self.lineas = 0

    ##
    # Metodo para crear los archivos de la tupla y error
    #
    #   @Param fuenteUrl: 
    #       Ruta del archivo fuente (el que se abre)
    #   @Param txtAreaFuente: 
    #       El componente Gui correspondiente a la Caja de texto
    #       del archivo fuente
    ##
    def crearArchivos( self, fuenteUrl, txtAreaFuente ):

        # Obtener nombre del archivo fuente
        lista = str(fuenteUrl).split("/")
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
                        "\t\t",
                        "Token",
                        "\t\t",
                        "Lexema",
                        "\n\n"
                     ]

        # Texto Default para el archivo error
        textoError = [
                        "* Archivo Error *\n",
                        "En esta etapa del desarrollo del compilador este archivo solo\n",
                        "contiene una copia del archivo fuente",
                        "\n\n"
                     ]
        
        # Se crean los archivos en las rutas correspondientes
        # y se escribe el texto default en ellos

        archivo = open( self.archivoTpl, "w+")
        archivo.writelines(textoTupla)
        self.cierraArchivo( archivo )

        archivo = open( self.archivoErr, "w+")
        archivo.writelines(textoError)
        self.cierraArchivo( archivo )
    
    ##
    # Metodo para cerrar un archivo
    #   @Param archivo:
    #       El archivo a cerrar
    ##
    def cierraArchivo( self, archivo ):
        archivo.close()
    
    ##
    # Metodo para inicial el analizador lexicografico
    #
    #   @Param fuenteUrl: 
    #       Ruta del archivo fuente (el que se abre)
    #   @Param txtAreaFuente: 
    #       El componente Gui correspondiente a la Caja de texto
    #       del archivo fuente
    ##
    def iniciaCompilacion( self, fuenteUrl, txtAreaFuente ):
        
        alex = Alex( txtAreaFuente )
        pr = Palabras_Reservadas()
        
        # Creacion de los Archivos
        self.crearArchivos( fuenteUrl, txtAreaFuente )
        
        # Se abren los archivos para el modo agregar texto
        archivo = open( self.archivoTpl, "a+")
        self.archivoErr = open( self.archivoErr, "a+")
        
        diccionario = alex.alexico(self)

        # Cuando sea Aceptado el token
        while diccionario["token"] != pr.tabla["hecho"] and diccionario["token"] != pr.tabla["error"]:

            if diccionario["token"] == "vacio":
                pass
                
            else: 

                texto = [
                        str(self.lineas),
                        "\t\t",
                        diccionario["token"],
                        "\t\t",
                        diccionario["lexema"],
                        "\n"
                     ]
                
                archivo.writelines( texto )

            diccionario = alex.alexico(self)

        # Cuando sea Error
        if diccionario["token"] == pr.tabla["error"]:

            texto = [
                        str(self.lineas),
                        "\t\t",
                        "<<<<< Error Caracter \"" + diccionario["lexema"] + "\" no permitido >>>>>",
                        "\n"
                     ]

            archivo.writelines( texto )

        # Cuando sea Fin de Archivo
        elif diccionario["token"] == pr.tabla["hecho"]:

            texto = [
                        str(self.lineas),
                        "\t\t",
                        diccionario["token"],
                        "\t\t",
                        diccionario["lexema"],
                        "\n"
                     ]
                     
            archivo.writelines( texto )
                 
        archivo.close()