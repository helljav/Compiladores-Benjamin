import os
from Alex import Alex
from PR import Palabras_Reservadas
from tabla_simbolos import Tabla
from Parser import Parser

class Uami(object):

    ##
    # Constructor
    #   @Param ventana:
    #       referencia de memoria actual del obj ventana
    ##
    def __init__( self, ventana ):

        # Inyeccion de Dependencias
        self.ventana = ventana
        self.pr = Palabras_Reservadas()
        self.alex = Alex( self.pr, self )
        self.tabla = Tabla(self.pr)
        self.tabla.cargarPal_Res()

        # Atributos
        self.urlTpl = ""
        self.urlErr = ""
        self.lineas = 0
        self.errores = 0

    ##
    # Metodo para crear los archivos de la tupla y error
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
        self.urlTpl = urlDist +  nombreFuente + ".tpl"
        self.urlErr = urlDist +  nombreFuente + ".err"

        # Texto Default para el archivo tupla
        textoTupla = [
                        "En este archivo se encuentran los lexemas reconocidos\n",
                        "por el analizador lexicografico\n",
                        "\n\n",
                        "Linea",
                        "\t",
                        "Lexema",
                        "\t\t",
                        "Token",
                        "\n\n"
                     ]

        # Texto Default para el archivo error
        textoError = "* Detalles de Error de Compilacion*\n\n"
        
        # Se crean los archivos en las rutas correspondientes
        # y se escribe el texto default en ellos
        self.escribirArchivo( self.urlTpl, "w+", textoTupla )
        self.ventana.escribirAreaTupla( self.getArchivoTexto(self.urlTpl) )
        
        self.escribirArchivo( self.urlErr, "w+", textoError )
        self.ventana.escribirAreaErrores( self.getArchivoTexto(self.urlErr) )

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
        else:
            archivo.write( texto )
        
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
    # Metodo para iniciar el analizador lexicografico
    ##
    def iniciaCompilacion( self ):
        
        while self.ventana.fuenteUrl == "":
            self.ventana.guardarArchivo()

        cadRes = ""
        cadRes += "Inicia Compilacion: " + str(self.ventana.fuenteUrl) + "\n\n"
        self.ventana.escribirAreaResultado( cadRes )
        cadRes += "Creando Archivos Tupla y Error...\n"
        self.ventana.escribirAreaResultado( cadRes )
        self.crearArchivos()
        cadRes += "Espere un momento por favor...\n"
        self.ventana.escribirAreaResultado( cadRes )

        
        parser = Parser( self )
        parser.inicio()


        # Escribir Areas al finalizar programa

        if self.errores == 0:
            cadRes += "Compilacion Terminada\n\n"  + "NO SE ENCONTRARON ERRORES"
        else:
            cadRes += "Compilacion Terminada\n\n"  + "Errores: " +  str(self.errores)
            
        self.ventana.escribirAreaResultado( cadRes )

        self.ventana.escribirAreaErrores( self.getArchivoTexto(self.urlErr) )

        self.escribirArchivo( self.urlTpl, "a+", self.tabla.imprimirTabla() )
        self.ventana.escribirAreaTupla( self.getArchivoTexto(self.urlTpl) )


    # def iniciaCompilacion( self ):
        
    #     while self.ventana.fuenteUrl == "":
    #         self.ventana.guardarArchivo()

    #     cadRes = ""
    #     cadRes += "Inicia Compilacion: " + str(self.ventana.fuenteUrl) + "\n\n"
    #     self.ventana.escribirAreaResultado( cadRes )
    #     cadRes += "Creando Archivos Tupla y Error...\n"
    #     self.ventana.escribirAreaResultado( cadRes )
    #     self.crearArchivos()
    #     cadRes += "Espere un momento por favor...\n"
    #     self.ventana.escribirAreaResultado( cadRes )

    #     diccionario = self.alex.alexico()

    #     # Cuando sea Aceptado el token
    #     while diccionario["token"] != self.pr.HECHO:

    #         if diccionario["token"] == self.pr.DELIMITADOR or diccionario["token"] == self.pr.COMENTARIO:
    #             pass
                
    #         # Cuando sea Error Token invalido
    #         elif diccionario["token"] == self.pr.TOKEN_INV:

    #             texto = [
    #                         "Linea: ",
    #                         str(self.lineas),
    #                         "\t",
    #                         diccionario["token"],
    #                         "\n\t",
    #                         diccionario["lexema"] + " no Reconocido",
    #                         "\n\n"
    #                     ]

    #             self.errores += 1 

    #             cadRes += "<< Error Encontrado >>\n"
    #             self.ventana.escribirAreaResultado( cadRes )
    #             self.escribirArchivo( self.urlErr, "a+", texto )
            
    #         # Cuando sea Error lexicografico
    #         elif diccionario["token"] == self.pr.ERROR:

    #             texto = [
    #                         "Linea: ",
    #                         str(self.lineas),
    #                         "\n\t",
    #                         diccionario["token"],
    #                         "\n\t",
    #                         "\"" + diccionario["lexema"] + "\" NO PERMITIDO",
    #                         "\n\n"
    #                     ]

    #             self.errores += 1 
                
    #             cadRes += "<< Error Encontrado >>\n"
    #             self.ventana.escribirAreaResultado( cadRes )
    #             self.escribirArchivo( self.urlErr, "a+", texto )
                
    #         # Pertmitidos
    #         else:
    #             indice = int( diccionario["token"] )
    #             lexema = self.tabla.getLexema( indice )
    #             token = self.tabla.getToken( indice )


    #             texto = [
    #                     str(self.lineas),
    #                     "\t",
    #                     lexema,
    #                     "\t\t",
    #                     token,
    #                     "\n"
    #                 ]
                
    #             self.escribirArchivo( self.urlTpl, "a+", texto )

    #         diccionario = self.alex.alexico()

    #     # Cuando sea Fin de Archivo
    #     if diccionario["token"] == self.pr.HECHO:

    #         texto = [
    #                     str(self.lineas),
    #                     "\t",
    #                     diccionario["lexema"],
    #                     "\t\t",
    #                     diccionario["token"],
    #                     "\n"
    #                  ]
                     
    #         self.escribirArchivo( self.urlTpl, "a+", texto )


    #     # Escribir Areas al finalizar programa

    #     if self.errores == 0:
    #         cadRes += "Compilacion Terminada\n\n"  + "NO SE ENCONTRARON ERRORES"
    #     else:
    #         cadRes += "Compilacion Terminada\n\n"  + "Errores: " +  str(self.errores)
            
    #     self.ventana.escribirAreaResultado( cadRes )

    #     self.ventana.escribirAreaErrores( self.getArchivoTexto(self.urlErr) )

    #     self.escribirArchivo( self.urlTpl, "a+", self.tabla.imprimirTabla() )
    #     self.ventana.escribirAreaTupla( self.getArchivoTexto(self.urlTpl) )