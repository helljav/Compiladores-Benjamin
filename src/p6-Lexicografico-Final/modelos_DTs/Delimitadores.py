##
# Metodo para reconocer si un caracter es un delimitador
#   @param: caracter a evaluar
#   @Return: True si es delimitador, False si no
##
def dt_esDelimitador( self, caracter ):
    delimitadores = ["\n", "\t", "\b", " "]
    return self.perteneceLista( caracter, delimitadores )


##
# Diagrama de Transicion Delimitadores
# @Return: diccionario con  token y lexema
#           acorde a la respuesta
##
def dt_delimitadores( self, lexema ):
    
    if lexema == " ":

        return {
                    "token": self.pr.DELIMITADOR,
                    "lexema": lexema
                }

    if lexema == "\n":

        return {
                    "token": self.pr.DELIMITADOR,
                    "lexema": lexema
                }
    if lexema == "\t":

        return {
                    "token": self.pr.DELIMITADOR,
                    "lexema": lexema
                }
    if lexema == "\b":

        return {
                    "token": self.pr.DELIMITADOR,
                    "lexema": lexema
                }
        
    