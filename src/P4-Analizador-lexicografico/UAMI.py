from Alex import Alex
from PR import Palabras_Reservadas

class Uami(object):

    def __init__( self ):
        
        self.achivoTpl = ""
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
        lista = lista[0:len(lista)-1]
        
        # Generar la fuenteUrl a nivel de la carpeta origen del archivo abierto
        fuenteUrl = '/'.join(str(e) for e in lista) + "/"
        
        # Creacion de los Archivos
        self.achivoTpl = open( fuenteUrl + "/tupla.tpl", "w+")
        self.archivoErr = open( fuenteUrl + "/error.err", "w+")

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

        self.achivoTpl.writelines(textoTupla)

        textoError = [
                        "* Archivo Error *\n",
                        "En esta etapa del desarrollo del compilador este archivo solo\n",
                        "contiene una copia del archivo fuente",
                        "\n\n",
                        contenido
                     ]

        self.archivoErr.writelines(textoError)

        self.cierraArchivo()
        self.achivoTpl = open( fuenteUrl + "/tupla.tpl", "a+")
        self.archivoErr = open( fuenteUrl + "/tupla.tpl", "a+")
    
    def cierraArchivo( self ):
        self.achivoTpl.close()
        self.archivoErr.close()
    
    def iniciaCompilacion( self, fuenteUrl, txtAreaFuente ):
        
        alex = Alex( txtAreaFuente )

        pr = Palabras_Reservadas()
        self.crearArchivos( fuenteUrl, txtAreaFuente )
        
        while self.lineas < len( alex.contenidoFuente ):
            diccionario = alex.alexico(self)
            
            # Cuendo sea Error
            if diccionario["token"] == pr.error:
                self.achivoTpl.write("Linea: " + str(self.lineas) + "\t\t" +"<<<<< Error Caracter \"" + diccionario["lexema"] + "\" no permitido >>>>>")
                break

            # Cuando sea Fin de Archivo
            elif diccionario["token"] == pr.hecho:
                self.achivoTpl.write( 
                                    "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t" + "Lexema: " + diccionario["lexema"] + "\n"
                                )
                break

            # Cuando sea Aceptado el token
            elif (diccionario["token"] == pr.incremento):

                self.achivoTpl.write( 
                                   "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t" + "Lexema: " + diccionario["lexema"] + "\n" 
                                )

            elif (diccionario["token"] == pr.producto):

                self.achivoTpl.write( 
                                   "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t" + "Lexema: " + diccionario["lexema"] + "\n" 
                                )
            
            elif (diccionario["token"] == pr.entero):
                self.achivoTpl.write( 
                                "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t\t" + "Lexema: " + diccionario["lexema"] + "\n"
                            )

            elif (diccionario["token"] == pr.suma):
                self.achivoTpl.write( 
                                "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t\t" + "Lexema: " + diccionario["lexema"] + "\n"
                            )
        
        self.cierraArchivo()