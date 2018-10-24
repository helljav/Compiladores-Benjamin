from Alex import Alex
from PR import Palabras_Reservadas

class Uami(object):

    def __init__( self ):
        
        # un variable tipo fopen para abrir el archivo 
        self.f_tpl = ""
        # Cadena para crear el archivo Error (*.err)
        self.err = ""
        # Cadena para crear el archivo tupla (*.tpl)
        self.lineas = 0

    def crearArchivos( self, URL, contenido_GUI ):

        contenido = open( URL, "r").read()

        # Eliminar nombre de archivo abierto y guararlo en lista
        lista = str(URL).split("/")
        lista = lista[0:len(lista)-1]
        
        # Generar la url a nivel de la carpeta origen del archivo abierto
        URL = '/'.join(str(e) for e in lista) + "/"
        
        
        # Creacion de los Archivos
        self.f_tpl = open( URL + "/tupla.tpl", "w+")
        self.err = open( URL + "/error.err", "w+")

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

        self.f_tpl.writelines(textoTupla)

        textoError = [
                        "* Archivo Error *\n",
                        "En esta etapa del desarrollo del compilador este archivo solo\n",
                        "contiene una copia del archivo fuente",
                        "\n\n",
                        contenido
                     ]

        self.err.writelines(textoError)

        self.cierraArchivo()
        self.f_tpl = open( URL + "/tupla.tpl", "a+")
        self.err = open( URL + "/tupla.tpl", "a+")
    
    def cierraArchivo( self ):
        self.f_tpl.close()
        self.err.close()
    
    def iniciaCompilacion( self, URL, contenido_GUI ):
        
        alex = Alex(contenido_GUI)
        pr = Palabras_Reservadas()
        self.crearArchivos( URL, contenido_GUI )
        
        while self.lineas < len(alex.contenido_del_archivo):
            diccionario = alex.Alexico(self)
            if diccionario["token"] == pr.error:
                self.f_tpl.write("Linea: " + str(self.lineas) + "\t\t" +"<<<<< Error Caracter \"" + diccionario["lexema"] + "\" no permitido >>>>>")
                break

            # Cuando sea Fin de Archivo
            elif diccionario["token"] == pr.hecho:
                self.f_tpl.write( 
                                    "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t" + "Lexema: " + diccionario["lexema"] + "\n"
                                )
                break

            # Cuando sea Aceptado el token
            elif (diccionario["token"] == pr.incremento):

                self.f_tpl.write( 
                                   "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t" + "Lexema: " + diccionario["lexema"] + "\n" 
                                )

            elif (diccionario["token"] == pr.producto):

                self.f_tpl.write( 
                                   "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t" + "Lexema: " + diccionario["lexema"] + "\n" 
                                )
            
            elif (diccionario["token"] == pr.entero):
                self.f_tpl.write( 
                                "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t\t" + "Lexema: " + diccionario["lexema"] + "\n"
                            )

            elif (diccionario["token"] == pr.suma):
                self.f_tpl.write( 
                                "Linea: " + str(self.lineas) + "\t" + "Token: " + diccionario["token"] + "\t\t" + "Lexema: " + diccionario["lexema"] + "\n"
                            )
        
        
        self.cierraArchivo()