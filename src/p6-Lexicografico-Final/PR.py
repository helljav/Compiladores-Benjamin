# -*- coding: utf-8 -*-

class Palabras_Reservadas(object):
    
    def __init__( self ):

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
        self.RELOP = "OPERADOR RELACIONAL"
        self.LOGOP = "OPERADOR LOGICO"
        self.ADDOP = "OPERADOR DE SUMA O RESTA"
        self.MULOP = "OPERADOR DE MULTIPLICACION"
        self.STRINGS = "OPERADOR DE MULTIPLICACION"
        self.ERROR = "ERROR LEXICOGRAFICO"
        self.TOKEN_INV = "TOKEN INVALIDO"
        self.RESTO_MUNDO = "RESTO DEL MUNDO"
        self.ASIGNACION = "ASIGNACION"
        self.ID = "IDENTIFICADOR"
        self.NUM_ENT = "ENTERO"
        #LEXEMAS PARA OPERADORES LOGICOS, ARITMETICOS Y RELACIONALES
        self.LT = "<"
        self.LE = "<="
        self.EQ = "=="
        self.ASG = "="
        self.GE = ">="
        self.NE = "!="
        self.NOT = "!"
        self.MAS = "+"
        self.MENOS = "-"
        self.OR = "||"
        self.MULT = "*"
        self.DIV = "/"
        self.MODULO = "%"
        self.AND = "&&"
        

        # ñoño
        C = 'ñá'.decode('utf8')
        print C
        