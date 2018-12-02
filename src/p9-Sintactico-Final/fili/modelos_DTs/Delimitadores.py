##
# Metodo para reconocer si un caracter es un delimitador
#   @param: caracter a evaluar
#   @Return: True si es delimitador, False si no
##
def dt_esDelimitador( self, caracter ):
    delimitadores = ["\n", "\t", "\b", " "]
    return self.perteneceLista( caracter, delimitadores )
    