# -*- coding: utf-8 -*-

class Palabras_Reservadas(object):

    def __init__( self ):
        self.palabras_reservadas = {

            "producto": {
                            "token": "PRODUCTO",
                            "lexema":"*"
                         },
            "suma":      {
                            "token":"SUMA",
                             "lexema": "+"
                        },

            "incremento":
                        {
                            "token": "INCREMENTO",
                             "lexema": "++"
                        },

            "entero":
                        {
                            "token": "Num_Entero",
                             "lexema": "ENTERO"
                        },

            "error" :
                        {
                            "token": "ERROR",
                            "lexema": "error"
                        },

            "hecho" :
                        {
                            "token": "FINAL DE ARCHIVO",
                            "lexema": "\0"
                        },

            "asignacion" :
                        {
                            "token": "ASIGNACION",
                            "lexema": "="

                        },

            "resta" :
                        {
                            "token": "RESTA",
                            "lexema": "-"

                        },

            "imprimir" :
                        {
                            "token": "PRINT",
                            "lexema": "print"

                        },

            "letras" :
                        {
                            "token": "LETRAS",
                            "lexema": "letras"
                            }

        }


        # # ñoño
        # C = 'ñá'.decode('utf8')
        # print C
