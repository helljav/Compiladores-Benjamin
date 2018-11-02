# -*- coding: utf-8 -*-
from modelos_DTs.Aritmeticos import dt_aritmeticos
from modelos_DTs.Entero import dt_Entero
from modelos_DTs.Relacionales import dt_relacionales
from modelos_DTs.Logicos import dt_logicos
from modelos_DTs.Delimitadores import dt_delimitadores

class DTS(object):

    def __init__( self, alex, pr ):
        self.alex = alex
        self.pr = pr

    def aritmeticos(self, lexema):
        return dt_aritmeticos(self, lexema)

    def Num_Entero(self, lexema):
        return dt_Entero( self, lexema )
    
    def relacionales( self, lexema ):
        return dt_relacionales( self, lexema )

    def logicos( self, lexema ):
        return dt_logicos( self, lexema )
    
    def delimitadores( self, lexema ):
        return dt_delimitadores( self, lexema )

    

    ##
    # Metodo para ver si un elemento
    # pertenece a una lista
    # mediante un ForEach
    #   @Param lista: lista en la cual se hara la busqueda
    #   @Param elemento: elemento a buscar en la lista
    #   @Return Bolean: True si pertenece, False si no 
    ##
    def perteneceLista( self, caracter, lista):

        for elemento in lista:

            if caracter == str(elemento):
                return True

        return False

    def esDelimitador( self, caracter ):
        delimitadores = ["\n", "\t", "\b", " "]
        return self.perteneceLista( caracter, delimitadores )

    ##
    # Metodo para reconocer si un caracter es Logico
    #   @param: caracter a evaluar
    #   @Return: True si es digito, False si no
    ##
    def esLogico( self, caracter ):
        
        operadores = [ "&", "|", "!" ]
        return self.perteneceLista( caracter, operadores )

    ##
    # Metodo para reconocer si un caracter es Relacional
    #   @param: caracter a evaluar
    #   @Return: True si es digito, False si no
    ##
    def esRelacional( self, caracter ):
        
        operadores = [ "=", "<", ">", "!" ]
        return self.perteneceLista( caracter, operadores )

    ##
    # Metodo para reconocer si un caracter es Aritmetico
    #   @param: caracter a evaluar
    #   @Return: True si es digito, False si no
    ##
    def esAritmetico( self, caracter ):

        operadores = [ "=", "-", "+", "/", "*", "%" ]
        return self.perteneceLista( caracter, operadores )

    ##
    # Metodo para reconocer si un caracter es un digito
    #   @param: caracter a evaluar
    #   @Return: True si es digito, False si no
    ##
    def esDigito( self, caracter ):

        digitos = list( range(0,10) )
        return self.perteneceLista(caracter, digitos)

    ##
    # Metodo para reconocer si un caracter es una letra permitida
    #   @param: caracter a evaluar
    #   @Return: True si es una letra, False si no
    ##
    def esLetra( self, caracter ):

        letras = []

        for i in range(97,123):
            letras.append( chr(i) )

        print letras

        return self.perteneceLista( caracter, letras )
        
