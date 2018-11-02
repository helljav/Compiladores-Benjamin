# -*- coding: utf-8 -*-
from modelos_DTs.Aritmeticos import dt_aritmeticos, dt_esAritmetico
from modelos_DTs.Entero import dt_Entero, dt_esDigito
from modelos_DTs.Relacionales import dt_relacionales, dt_esRelacional
from modelos_DTs.Logicos import dt_logicos, dt_esLogico
from modelos_DTs.Delimitadores import dt_delimitadores, dt_esDelimitador
from modelos_DTs.Resto_del_Mundo import dt_restoMundo, dt_esRestoMundo

class DTS(object):

    ##
    # Constructor
    # @Param alex: referencia de memoria del objeto alex
    # @Param pr: referencia de memoria del objeto pr
    ##
    def __init__( self, alex, pr ):
        self.alex = alex
        self.pr = pr

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

    ##
    # Metodo para reconocer si un caracter es Aritmetico
    #   @param: caracter a evaluar
    #   @Return: True si es aritmetico, False si no
    ##
    def esAritmetico( self, caracter ):
        return dt_esAritmetico( self, caracter )

    ##
    # Diagrama de Transicion Aritmeticos
    # @Return: diccionario con  token y lexema
    #           acorde a la respuesta
    ##
    def aritmeticos(self, lexema):
        return dt_aritmeticos(self, lexema)

    ##
    # Metodo para reconocer si un caracter es un digito
    #   @param: caracter a evaluar
    #   @Return: True si es digito, False si no
    ##
    def esDigito( self, caracter ):
        return dt_esDigito( self, caracter )

    ##
    # Diagrama de Transicion Entero
    # @Return: diccionario con  token y lexema
    #           acorde a la respuesta
    ##
    def Num_Entero(self, lexema):
        return dt_Entero( self, lexema )

    ##
    # Metodo para reconocer si un caracter es Relacional
    #   @param: caracter a evaluar
    #   @Return: True si es relacional, False si no
    ##
    def esRelacional( self, caracter ):
        return dt_esRelacional( self, caracter )
    
    ##
    # Diagrama de Transicion Relacionales
    # @Return: diccionario con  token y lexema
    #           acorde a la respuesta
    ##
    def relacionales( self, lexema ):
        return dt_relacionales( self, lexema )

    ##
    # Metodo para reconocer si un caracter es Logico
    #   @param: caracter a evaluar
    #   @Return: True si es logico, False si no
    ##
    def esLogico( self, caracter ):
        return dt_esLogico( self, caracter )

    ##
    # Diagrama de Transicion Logicos
    # @Return: diccionario con  token y lexema
    #           acorde a la respuesta
    ##
    def logicos( self, lexema ):
        return dt_logicos( self, lexema )

    ##
    # Metodo para reconocer si un caracter es un delimitador
    #   @param: caracter a evaluar
    #   @Return: True si es delimitador, False si no
    ##
    def esDelimitador( self, caracter ):
        return dt_esDelimitador( self, caracter )
    
    ##
    # Diagrama de Transicion Delimitadores
    # @Return: diccionario con  token y lexema
    #           acorde a la respuesta
    ##
    def delimitadores( self, lexema ):
        return dt_delimitadores( self, lexema )

    ##
    # Metodo para reconocer si un caracter es Resto del Mundo
    #   @param: caracter a evaluar
    #   @Return: True si es digito, False si no
    ##
    def esRestoMundo( self, caracter ):
        return dt_esRestoMundo( self, caracter)
    
    ##
    # Diagrama de Transicion Resto del Mundo
    # @Return: diccionario con  token y lexema
    #           acorde a la respuesta
    ##
    def restoMundo( self, lexema ):
        return dt_restoMundo( self, lexema )




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
        
