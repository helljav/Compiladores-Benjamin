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
    # y llena por primera vez el buffer
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
    # Metodo que retrocede una posicion en la linea
    # de texto cargada en el buffer
    # ( Simula el signo de pesos )
    ##
    def desleer(self):
        
        self.buffer["pos_leida"] = self.buffer["pos_leida"] - 1


    ##
    # Metodo para reconocer si un caracter es un digito
    #   @param: caracter a evaluar
    #   @Return: True si es digito, False si no
    ##
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

    ##
    # Metodo para reconocer si un caracter es una letra permitida
    #   @param: caracter a evaluar
    #   @Return: True si es una letra, False si no
    ##
    def esLetra( self, caracter ):

        letras = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]

        for letra in letras:
            if caracter == letra:
                return True
        
        return False
    
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

        # Asignacion
        if lexema is '=':

            lexema = lexema + self.leerCaracter()

            self.desleer()

            return {
                        "token": pr.asignacion,
                        "lexema": lexema[0]
                    }

        # Suma
        elif lexema is '+':

            lexema = lexema + self.leerCaracter()

            self.desleer()

            return {
                        "token": pr.suma,
                        "lexema": lexema[ 0 ]
                    }
            
        # Resta
        elif lexema is '-':

            lexema = lexema + self.leerCaracter()

            self.desleer()

            return {
                        "token": pr.resta,
                        "lexema": lexema[ 0 ]
                    }

        # Entero
        elif self.esDigito( lexema ): 

            # Empieza en cero
            if lexema is "0":

                lexema = lexema + self.leerCaracter()

                # Segundo caracter es "otro"
                # Return entero cero
                if self.esDigito( lexema[1] ) == False:

                    self.desleer()

                    return {
                            "token": pr.entero,
                            "lexema": lexema[ 0 ]
                        }

                # Segundo caracter es un digito
                else:

                    # Se lee todo el numero entero para regresarlo como error y lexema
                    digito = self.leerCaracter()

                    while self.esDigito( digito ):
                        lexema = lexema + digito
                        digito = self.leerCaracter()
                    
                    return {
                            "token": pr.error,
                            "lexema": lexema
                        }

            # No empieza en cero
            else:

                # lee todo el numero y lo regresa como entero
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

        # Fin de Archivo
        elif lexema is "\0":

            return {
                        "token": pr.hecho,
                        "lexema": lexema
                    }

        # Delimitador vacio
        elif lexema is " ":
            
            return{ 
                "token": "vacio",
                "lexema": lexema
            }
        
        # Letra
        elif self.esLetra(lexema):

            # lee toda la palabra

            caracter = lexema
            lexema = ""

            while self.esLetra( caracter ):
                lexema = lexema + caracter
                caracter = self.leerCaracter()
                
            self.desleer()

            # La palabra leida es reservada
            if lexema == "print":

                return {
                            "token": pr.imprimir,
                            "lexema": lexema
                        }

            # La palabra NO es reservada
            else:
                return {
                        "token": pr.letras,
                        "lexema": lexema
                    }

        # Error  
        else:
            
            return {
                        "token": pr.error,
                        "lexema": lexema
                    }