
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
        self.contenidodelArchivo = str(contenido_GUI.toPlainText()).split("\n")
        print 
        print self.contenidodelArchivo
        self.contador = 0

        self.Buffer = {
                        "pos_leida":0,
                        "tamano": 0,
                        "cadena" :"" 
                      }

    def Llena_Buffer(self):
        if self.contador < len (self.contenido_del_archivo[:]):
            Cadena = self.contenido_del_archivo[self.contador] + " "
            self.Buffer["pos_leida"] = 0
            self.Buffer["cadena"] = Cadena
            self.Buffer["tamano"] = len(Cadena)
        else:
            self.Buffer["pos_leida"] = 0
            self.Buffer["cadena"] = "null"
            self.Buffer["tamano"] = 0
            
    