# -*- coding: utf-8 -*-

class Palabras_Reservadas(object):
    
    def __init__( self ):

        # Palabras Reservadas
        self.PROGRAMA = "programa"
        self.SI = "si"
        self.ENTONCES = "entonces"
        self.OTRO = "otro"
        self.HAZ = "haz"
        self.MIENTRAS = "mientras"
        self.COMIENZA = "comienza"
        self.TERMINA = "termina"
        self.IMPRIME = "imprime"
        self.REPITE = "repite"
        self.HASTA = "hasta"
        self.PARA = "para"
        self.A = "a"

        #Tokens lexicograficos
        self.HECHO = "FIN DE ARCHIVO"
        self.EOS = "EOS"
        self.COMENTARIO = "COMENTARIO"
        self.P_RES = "PALABRA RESERVADA"
        self.CADENA = "CADENA"
        self.RELOP = "OPE. RELACIONAL"
        self.LOGOP = "OPE. LOGICO"
        self.SUMA = "OPE. DE SUMA"
        self.RESTA = "OPE. DE RESTA"
        self.MULTIPLICACION = "OPE. DE MULTIPLICACION"
        self.DIVISION = "OPE. DE DIVICION"
        self.MODULO = "OPE. DE MODULO"
        self.STRINGS = "CADENAS DE CARACTERES"
        self.ERROR = "ERROR LEXICOGRAFICO"
        self.TOKEN_INV = "TOKEN INVALIDO"
        self.RESTO_MUNDO = "RESTO DEL MUNDO"
        self.ASIGNACION = "ASIGNACION"
        self.ID = "IDENTIFICADOR"
        self.NUM_ENT = "ENTERO"
        self.DELIMITADOR = "DELIMITADOR"

        #LEXEMAS PARA OPERADORES LOGICOS, ARITMETICOS Y RELACIONALES
        self.MAS = "+"
        self.MENOS = "-"
        self.MULT = "*"
        self.DIV = "/"
        self.MOD = "%"
        self.ASG = "="

        self.LT = "<"
        self.LE = "<="
        self.EQ = "=="
        self.GT = ">"
        self.GE = ">="
        self.NE = "!="

        self.NOT = "!"
        self.OR = "||"
        self.AND = "&&"
        

        # ñoño
        # C = 'ñá'.decode('utf8')
        # print C
        