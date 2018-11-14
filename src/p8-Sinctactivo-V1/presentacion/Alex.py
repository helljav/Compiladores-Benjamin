# -*- coding: utf-8 -*-
from PR import Palabras_Reservadas
from DTs import DTS
from PyQt4 import QtGui,QtCore

class Alex(object):

    ##
    # Constructor
    #
    #   @Param ventana:
    #       referencia de memoria actual del obj ventana
    #   @Param pr:
    #       referencia de memoria actual del obj pr
    #   @Param uami:
    #      referencia de memoria actual del obj uami
    ##
    def __init__( self, pr, uami ):

        self.pr = pr
        self.uami = uami

        self.contenidoFuente = str(self.uami.ventana.txtAreaFuente.toPlainText())
        self.contador = 1
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

        if self.contador <= len (self.contenidoFuente[:]):
            Cadena = str(self.contenidoFuente[ self.contador - 1 ])

            if Cadena == "":
                Cadena = "\n"

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
            self.contador += 1
            self.llenaBuffer()

        if self.buffer["longitud"] != 0:
            caracter = self.buffer["cadena"][self.buffer["pos_leida"]]
            self.buffer["pos_leida"] += 1
            return caracter

        else:
            return "\0"

    ##
    # Metodo que retrocede una posicion en la linea
    # de texto cargada en el buffer
    # ( Simula el signo de pesos )
    ##
    def desleer(self):
            if self.buffer["pos_leida"] == 0:
                self.contador -= 1
                self.buffer["pos_leida"] = self.buffer["longitud"] 
            else:
                self.buffer["pos_leida"] -= 1  


    
    ##
    # Metodo que implementa los diagrama de transiciones
    # Para el analizador Lexicografico
    ##
    def alexico(self):

        lexema = self.leerCaracter()
        dts = DTS(self, self.pr)

        if dts.esAritmetico( lexema ):
            self.uami.lineas = self.contador
            return dts.aritmeticos( lexema )

        elif dts.esDigito( lexema ):
            self.uami.lineas = self.contador
            return dts.Num_Entero( lexema )

        elif dts.esRelacional( lexema ):
            self.uami.lineas = self.contador
            return dts.relacionales( lexema )
        
        elif dts.esLogico( lexema ):
            self.uami.lineas = self.contador
            return dts.logicos( lexema )
        
        elif dts.esDelimitador( lexema ):
            self.uami.lineas = self.contador
            return dts.delimitadores( lexema )

        elif dts.esRestoMundo( lexema ):
            self.uami.lineas = self.contador
            return dts.restoMundo( lexema)

        elif dts.esIdentificador( lexema ):
            self.uami.lineas = self.contador
            return dts.identificadores( lexema )
            
        elif dts.esCadena( lexema ):
            self.uami.lineas = self.contador
            return dts.cadenas( lexema )
        
        elif dts.esComentario( lexema ):
            self.uami.lineas = self.contador
            return dts.comentarios( lexema )

        # Fin de Archivo
        elif lexema is "\0":
            self.uami.lineas = self.contador
            return {
                        "token": self.pr.HECHO,
                        "lexema": self.pr.EOS
                    }

        # Todo lo no reconocido
        else:
            self.uami.lineas = self.contador
            return {
                "token": self.pr.TOKEN_INV,
                "lexema": lexema
            }

        