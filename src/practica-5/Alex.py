from PR import Palabras_Reservadas
from PyQt4 import QtGui,QtCore

class Alex(object):

    ##
    # Constructor
    #   
    #   @Param txtAreaFuente: 
    #       El componente Gui correspondiente a la Caja de texto
    #       del archivo fuente
    ##
    def __init__( self, txtAreaFuente ):
        self.contenidoFuente = str(txtAreaFuente.toPlainText())
        self.contador = 0
        self.buffer = {
                        "pos_leida":0,
                        "longitud": 0,
                        "cadena" :"" 
                      }
        self.init()
    
    ##
    # Metodo que Inicializa el contenido del archivo Fuente
    # por lineas en una lista
    # Crea las palabras Reservadas
    # y llena el buffer
    ##
    def init( self ):
        self.contenidoFuente = self.contenidoFuente.split("\n") 
        self.llenaBuffer()


    ##
    # Metodo que llena el buffer con el contenido 
    # de una linea de texto en el archivo fuente
    ##
    def llenaBuffer(self):

        if self.contador < len (self.contenidoFuente[:]):
            Cadena = str(self.contenidoFuente[self.contador])
            self.buffer["pos_leida"] = 0
            self.buffer["cadena"] = Cadena
            self.buffer["longitud"] = len(Cadena)
        else:
            self.buffer["pos_leida"] = 0
            self.buffer["cadena"] = "null"
            self.buffer["longitud"] = 0


    ##
    # Metodo que lee un caracter de la linea
    # de texto cargada en el buffer
    ##
    def leerCaracter( self ):

        if self.buffer["pos_leida"] == self.buffer["longitud"]:
            self.contador = self.contador + 1
            self.llenaBuffer()
        
        if self.buffer["longitud"] != 0:
            
            caracter = self.buffer["cadena"][self.buffer["pos_leida"]]
            self.buffer["pos_leida"] = self.buffer["pos_leida"] + 1

            return caracter

        else:
            return "\0"
    
    ##
    # Metodo que implementa el diagrama de transiciones
    # Para el analizador Lexicografico
    #
    #   @Param uami: 
    #       Un objeto de la clase Uami
    ##
    def alexico(self, uami):
        
        pr = Palabras_Reservadas()
        uami.lineas = self.contador
        lexema = self.leerCaracter()

        if lexema is '=':

            lexema = lexema + self.leerCaracter()

            if lexema[ 1 ] != '=':

                self.desleer()

                return {
                            "token": pr.asignacion,
                            "lexema": lexema
                        }
            else:
                return {
                            "token": pr.error,
                            "lexema": lexema
                        }

        elif lexema is '+':

            lexema = lexema + self.leerCaracter()

            if lexema[ 1 ] != '+':

                self.desleer()

                return {
                            "token": pr.suma,
                            "lexema": lexema[ 0 ]
                        }
            else:
                return {
                            "token": pr.error,
                            "lexema": lexema
                        }

        elif lexema is '-':

            lexema = lexema + self.leerCaracter()

            if lexema[ 1 ] != '-':

                self.desleer()

                return {
                            "token": pr.resta,
                            "lexema": lexema[ 0 ]
                        }
            else:
                return {
                            "token": pr.error,
                            "lexema": lexema
                        }

        # search regresa el numero de ocurrencias en la Exp. Regular
        elif self.esDigito( lexema ): 

            if lexema is "0":

                lexema = lexema + self.leerCaracter()

                # Cualquier cosa
                if self.esDigito( lexema[1] ) == False:

                    self.desleer()

                    return {
                            "token": pr.entero,
                            "lexema": lexema[ 0 ]
                        }

                # Otro Numero despues del 0
                else:

                    digito = self.leerCaracter()

                    while self.esDigito( digito ):
                        lexema = lexema + digito
                        digito = self.leerCaracter()
                    
                    return {
                            "token": pr.error,
                            "lexema": lexema
                        }
            else:

                digito = lexema
                lexema = ""

                while self.esDigito( digito ):
                    lexema = lexema + digito
                    digito = self.leerCaracter()
                    
                self.desleer()

                return {
                            "token": pr.entero,
                            "lexema": lexema
                        }
        
        elif lexema is "\0":

            return {
                        "token": pr.hecho,
                        "lexema": lexema
                    }

        elif lexema is " ":
            
            return{ 
                "token": "vacio",
                "lexema": lexema
            }
             
        else:
            
            return {
                        "token": pr.error,
                        "lexema": lexema
                    }
        
    ##
    # Metodo que retrocede una posicion en la linea
    # de texto cargada en el buffer
    # ( Simula el signo de pesos )
    ##
    def desleer(self):
        self.buffer["pos_leida"] = self.buffer["pos_leida"] - 1


    def esDigito( self, caracter ):

        digitos = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9"
        ]

        for digito in digitos:

            if caracter == digito:
                return True
        
        return False