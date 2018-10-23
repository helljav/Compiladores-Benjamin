# Libreria de expresiones regulares
import re
from PR import Palabras_Reservadas
from PyQt4 import QtGui,QtCore
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Alex(object):

    ##
    # Constructor de la clase
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
    # Inicializa el contenido del archivo,
    # Crear las palabras Reservadas
    # y llena el buffer
    ##
    def init( self ):
        self.pr = Palabras_Reservadas()
        self.contenidoFuente = self.contenidoFuente.split("\n") 
        self.llenaBuffer()


    ##
    # 
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
    # Leer Caracter de cadena
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
    #
    ##
    def alexico(self, uami):
        # Exp. Regular de entre 0 y 9
        numeros = re.compile('[0-9]')
        uami.lineas = self.contador
        c = self.leerCaracter()

        if c is '*':

            return {
                        "token": self.pr.producto,
                        "lexema": c
                    }

        elif c is '+':

            c2 = self.leerCaracter()

            if c2 is '+':

                return {
                            "token": self.pr.incremento,
                            "lexema": c + c2
                        }

            else:

                self.desleer()
                return {
                            "token": self.pr.suma,
                            "lexema": c
                        }

        # search regresa el numero de ocurrencias en la Exp. Regular
        elif numeros.search(c) > 0: 

            cad = ""

            while numeros.search(c) > 0:
                cad = cad + c
                c = self.leerCaracter()
                
            self.desleer()

            return {
                        "token": self.pr.entero,
                        "lexema": cad
                    }
        
        elif c is "\0":

            return {
                        "token": self.pr.hecho,
                        "lexema": c
                    }

        else:
            
            return {
                        "token": self.pr.error,
                        "lexema": c
                    }
        
    ##
    # Simula el signo de pesos de ENTERO y SUMA
    ##
    def desleer(self):
        self.buffer["pos_leida"] = self.buffer["pos_leida"] - 1

            
    