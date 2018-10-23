import os
from Alex import Alex
from PR import Palabras_Reservadas

class Uami(object):

    def __init__( self ):
        
        self.archivoTpl = ""
        self.archivoErr = ""
        self.lineas = 0

    ##
    # @Param fuenteUrl: ruta del archivo fuente (el que se abre)
    # @Param txtAreaFuente: Componente Gui de la ventana donde se muestra el contenido
    #                       del archivo fuente
    ##
    def crearArchivos( self, fuenteUrl, txtAreaFuente ):

        contenido = open( fuenteUrl, "r").read()

        # Eliminar nombre de archivo abierto y guararlo en lista
        lista = str(fuenteUrl).split("/")
        nombreFuente = lista[len(lista)-1].replace(".fte", "")
        # print nombreFuente
        lista = lista[0:len(lista)-1]
        
        # Generar la Url a nivel de la carpeta origen del archivo abierto
        fuenteUrl = '/'.join(str(e) for e in lista) + "/dist"
        
        print fuenteUrl
        
        # Creacion de los Archivos
        self.archivoTpl = fuenteUrl + "/" + nombreFuente + ".tpl"
        self.archivoErr = fuenteUrl + "/" + nombreFuente + ".err"

        # Texto Default
        textoTupla = [
                        "En este archivo se encuentran los lexemas reconocidos\n",
                        "por el analizador lexicografico\n",
                        "\n\n",
                        "\t",
                        "Token",
                        "\t\t",
                        "Lexema",
                        "\n\n"
                     ]

        textoError = [
                        "* Archivo Error *\n",
                        "En esta etapa del desarrollo del compilador este archivo solo\n",
                        "contiene una copia del archivo fuente",
                        "\n\n",
                        contenido
                     ]

        archivo = open( self.archivoTpl, "w+")
        archivo.writelines(textoTupla)
        self.cierraArchivo( archivo )

        archivo = open( self.archivoErr, "w+")
        archivo.writelines(textoError)
        self.cierraArchivo( archivo )

        # Cerrar archivos modo w+
        # self.cierraArchivo()
    
    def cierraArchivo( self, archivo ):
        archivo.close()
    
    def iniciaCompilacion( self, fuenteUrl, txtAreaFuente ):
        
        alex = Alex( txtAreaFuente )

        pr = Palabras_Reservadas()
        self.crearArchivos( fuenteUrl, txtAreaFuente )
        # Creacion de los Archivos
        archivo = open( self.archivoTpl, "a+")
        self.archivoErr = open( self.archivoErr, "a+")
        
        while self.lineas < len( alex.contenidoFuente ):
            diccionario = alex.alexico(self)
            
            # Cuendo sea Error
            if diccionario["token"] == pr.error:
                archivo.write("Linea: " + str(self.lineas) + "\t\t" +"<<<<< Error Caracter \"" + diccionario["lexema"] + "\" no permitido >>>>>")
                break

            # Cuando sea Fin de Archivo
            elif diccionario["token"] == pr.hecho:
                archivo.write( 
                                    "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t" + "Lexema: " + diccionario["lexema"] + "\n"
                                )
                break

            # Cuando sea Aceptado el token
            elif (diccionario["token"] == pr.incremento):

                archivo.write( 
                                   "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t" + "Lexema: " + diccionario["lexema"] + "\n" 
                                )

            elif (diccionario["token"] == pr.producto):

                archivo.write( 
                                   "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t" + "Lexema: " + diccionario["lexema"] + "\n" 
                                )
            
            elif (diccionario["token"] == pr.entero):
                archivo.write( 
                                "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t\t" + "Lexema: " + diccionario["lexema"] + "\n"
                            )

            elif (diccionario["token"] == pr.suma):
                archivo.write( 
                                "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t\t" + "Lexema: " + diccionario["lexema"] + "\n"
                            )
        
        archivo.close()