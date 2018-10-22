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
    def __init__( self, contenido_GUI ):
        self.pr = Palabras_Reservadas()
        self.contenido_del_archivo = str(contenido_GUI.toPlainText()).split("\n")
        # print 
        # print self.contenido_del_archivo
        self.contador = 0

        self.Buffer = {
                        "pos_leida":0,
                        "tamano": 0,
                        "cadena" :"" 
                      }

    def Llena_Buffer(self):
        if self.contador < len (self.contenido_del_archivo[:]):
            Cadena = str(self.contenido_del_archivo[self.contador])
            self.Buffer["pos_leida"] = 0
            self.Buffer["cadena"] = Cadena
            self.Buffer["tamano"] = len(Cadena)
        else:
            self.Buffer["pos_leida"] = 0
            self.Buffer["cadena"] = "null"
            self.Buffer["tamano"] = 0


    ##
    # Leer Cadena
    ##
    def leerCaracter( self ):

        if self.Buffer["pos_leida"] == self.Buffer["tamano"]:
            
            self.contador = self.contador + 1
            self.Llena_Buffer()
        
        if self.Buffer["tamano"] != 0:
            
            caracter = self.Buffer["cadena"][self.Buffer["pos_leida"]]
            self.Buffer["pos_leida"] = self.Buffer["pos_leida"] + 1

            return caracter

        else:
            return "\0"
    
    def Alexico (self, obj_UAMI):

        # Exp. Regular de entre 0 y 9
        numeros = re.compile('[0-9]')
        self.Llena_Buffer()

        obj_UAMI.lineas = self.contador

        c = self.leerCaracter()

        if c is '*':

            return {
                        "token": self.pr.producto,
                        "lexema": c
                    }

        elif c is '+':

            c2 = self.leerCaracter()
            print "c1 = ", c
            print "c2 = ", c2

            if c2 is '+':

                print c + c2

                return {
                            "token": self.pr.incremento,
                            "lexema": c + c2
                        }

            else:

                self.Deslee()
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
            
            self.Deslee()

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
    def Deslee(self):
        self.Buffer["pos_leida"] = self.Buffer["pos_leida"] - 1

            
    