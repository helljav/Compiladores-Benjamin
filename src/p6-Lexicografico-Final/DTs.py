# -*- coding: utf-8 -*-

class DTS(object):

    def __init__( self, alex, pr ):
        self.alex = alex
        self.pr = pr

    def aritmeticos(self, lexema):

        # Asignacion
        if lexema is '=':

            if self.alex.leerCaracter() != "=":
                self.alex.desleer()
                return {
                            "token": self.pr.ASIGNACION,
                            "lexema": lexema
                        }
            else:
                self.alex.desleer()
                return self.relacionales( lexema )


        # Suma
        elif lexema is '+':

            return {
                        "token": self.pr.SUMA,
                        "lexema": lexema
                    }

        # Resta
        elif lexema is '-':

            return {
                        "token": self.pr.RESTA,
                        "lexema": lexema
                    }

        # DIVISION
        elif lexema is '/':

            return {
                        "token": self.pr.DIVISION,
                        "lexema": lexema
                    }

        # Multiplicacion
        elif lexema is '*':

            return {
                        "token": self.pr.MULTIPLICACION,
                        "lexema": lexema
                    }
        
        # MODULO
        elif lexema is '%':

            return {
                        "token": self.pr.MODULO,
                        "lexema": lexema
                    }

    def Num_Entero(self, lexema):

        if self.esDigito( lexema ):
            # Empieza en cero
            if lexema is "0":
                lexema += self.alex.leerCaracter()
                # Segundo caracter es "otro"
                # Return entero cero
                if self.esDigito( lexema[1] ) == False:
                    self.alex.desleer()
                    return {
                            "token": self.pr.NUM_ENT,
                            "lexema": lexema[ 0 ]
                        }
                # Segundo caracter es un digito
                else:
                    # Se lee todo el numero entero para regresarlo como error y lexema
                    digito = self.alex.leerCaracter()
                    while self.esDigito( digito ):
                        lexema += digito
                        digito = self.alex.leerCaracter()
                    return {
                            "token": self.pr.ERROR,
                            "lexema": lexema
                        }
            # No empieza en cero
            else:
                # lee todo el numero y lo regresa como entero
                digito = lexema
                lexema = ""
                while self.esDigito( digito ):
                    lexema += digito
                    digito = self.alex.leerCaracter()

                self.alex.desleer()
                return {
                            "token": self.pr.NUM_ENT,
                            "lexema": lexema
                        }
    
    def relacionales( self, lexema ):

        # Caso ==
        if lexema is '=':

            lexema = lexema + self.alex.leerCaracter()

            if lexema[ 1 ] is '=':
                return {
                            "token": self.pr.RELOP,
                            "lexema": lexema
                        }
        
        # Caso !=
        if lexema is '!':

            lexema = lexema + self.alex.leerCaracter()

            if lexema[ 1 ] is '=':

                return {
                            "token": self.pr.RELOP,
                            "lexema": lexema
                        }
            else:
                self.alex.desleer()
                return self.logicos( lexema[0]);

        # Caso >= y >
        elif lexema is '>':

            lexema = lexema + self.alex.leerCaracter()

            if lexema[ 1 ] is '=':

                return {
                            "token": self.pr.RELOP,
                            "lexema": lexema
                        }

            else:

                self.alex.desleer()
                return {
                            "token": self.pr.RELOP,
                            "lexema": lexema[ 0 ]
                        }
        
        # Caso <= y <
        elif lexema is '<':

            lexema = lexema + self.alex.leerCaracter()

            if lexema[ 1 ] is '=':
                return {
                            "token": self.pr.RELOP,
                            "lexema": lexema
                        }

            else:
                self.alex.desleer()
                return {
                            "token": self.pr.RELOP,
                            "lexema": lexema[ 0 ]
                        }

    def logicos( self, lexema ):

        # Caso Negacion
        if lexema is "!":
            return {
                        "token": self.pr.LOGOP,
                        "lexema": lexema
                    }
        
        # Caso And 
        elif lexema is '&':

            lexema = lexema + self.alex.leerCaracter()

            if lexema[ 1 ] is '&':

                return {
                            "token": self.pr.LOGOP,
                            "lexema": lexema
                        }
        # Caso Or 
        elif lexema is '|':

            lexema = lexema + self.alex.leerCaracter()

            if lexema[ 1 ] is '|':

                return {
                            "token": self.pr.LOGOP,
                            "lexema": lexema
                        }
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
        
