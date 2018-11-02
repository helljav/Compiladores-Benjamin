##
# Metodo para reconocer si un caracter es Logico
#   @param: caracter a evaluar
#   @Return: True si es logico, False si no
##
def dt_esLogico( self, caracter ):
    
    operadores = [ "&", "|", "!" ]
    return self.perteneceLista( caracter, operadores )


##
# Diagrama de Transicion Logicos
# @Return: diccionario con  token y lexema
#           acorde a la respuesta
##
def dt_logicos( self, lexema ):

        cont = self.alex.contador

        # Negacion
        if lexema is '!':

            if self.alex.leerCaracter() != "=" or self.alex.contador == cont:
                self.alex.desleer()
                
                return {
                            "token": self.pr.LOGOP,
                            "lexema": lexema
                        }
        
        # Caso And 
        elif lexema is '&':

            lexema = lexema + self.alex.leerCaracter()

            if lexema[ 1 ] is '&':

                # misma linea
                if cont == self.alex.contador:
                    return {
                            "token": self.pr.LOGOP,
                            "lexema": lexema
                        }

                else:
                    self.alex.desleer()
                    return {
                            "token": self.pr.ERROR,
                            "lexema": lexema[0]
                        }

            else:
                return {
                            "token": self.pr.ERROR,
                            "lexema": lexema
                        }
        
        # Caso Or 
        elif lexema is '|':

            lexema = lexema + self.alex.leerCaracter()

            if lexema[ 1 ] is '|':

                # misma linea
                if cont == self.alex.contador:
                    return {
                            "token": self.pr.LOGOP,
                            "lexema": lexema
                        }

                else:
                    self.alex.desleer()
                    return {
                            "token": self.pr.ERROR,
                            "lexema": lexema[0]
                        }
                          
            else:
                return {
                            "token": self.pr.ERROR,
                            "lexema": lexema
                        }