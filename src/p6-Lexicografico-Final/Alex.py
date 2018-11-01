# -*- coding: utf-8 -*-
from PR import Palabras_Reservadas
from DTs import DTS
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
        
        dts = DTS(self, pr)

        # print dts.esLetra("a")

        if dts.esAritmetico( lexema ):
            return dts.aritmeticos( lexema )

        elif dts.esDigito( lexema ):
            return dts.Num_Entero(lexema)

        elif dts.esRelacional( lexema ):
            return dts.relacionales(lexema)
        
        elif dts.esLogico( lexema ):
            return dts.logicos(lexema)

        # Fin de Archivo
        elif lexema is "\0":

            return {
                        "token": pr.HECHO,
                        "lexema": lexema
                    }

        # Delimitador vacio
        elif lexema is " ":

            return{
                "token": "vacio",
                "lexema": lexema
            }

        