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