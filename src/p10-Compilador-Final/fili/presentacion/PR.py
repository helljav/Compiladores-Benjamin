# -*- coding: utf-8 -*-

class Palabras_Reservadas(object):
    
    def __init__( self ):

        # Palabras Reservadas
        self.Reservadas = {

            "PROGRAMA" : "programa",
            "SI" : "si",
            "ENTONCES" : "entonces",
            "OTRO" : "otro",
            "HAZ" : "haz",
            "MIENTRAS" : "mientras",
            "COMIENZA" : "comienza",
            "TERMINA" : "termina",
            "IMPRIME" : "imprime",
            "REPITE" : "repite",
            "HASTA" : "hasta",
            "PARA" : "para",
            "A" : "a"

        }

        #Tokens 
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
        self.ERROR_SINTACTICO = "ERROR SINTACTICO"
        self.TOKEN_INV = "TOKEN INVALIDO"
        self.RESTO_MUNDO = "RESTO DEL MUNDO"
        self.ASIGNACION = "ASIGNACION"
        self.ID = "IDENTIFICADOR"
        self.NUM_ENT = "ENTERO"
        self.DELIMITADOR = "DELIMITADOR"


        self.PC = ";"
        self.COMA = ","
        self.IGUAL = "="
        self.P_ABRE = "("
        self.P_CIERRA = ")"
        self.MAS = "+"
        self.MENOS = "-"
        self.MULT = "*"
        self.DIV = "/"

        self.LT = "<"
        self.LE = "<="
        self.EQ = "=="
        self.GE = ">="
        self.NE = "!="
        self.NOT = "!"
        self.OR = "||"
        self.MODULO = "%"
        self.AND = "&&"

        self.VALOR_I = "lvalue"
        self.VALOR_D = "rvalue"
        self.PUSH = "push"
        self.ASIGN = ":="
        self.ETIQUETA = "label"
        self.VE_A = "goto"
        self.SI_FALSO_VE_A = "gofalse"
        self.ESCRIBE = "write"
        self.IMPRIME = "print"
        self.HALT = "halt"