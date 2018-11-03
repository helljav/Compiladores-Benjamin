##
# Metodo para reconocer si un caracter puede ser cadena
#   @param: caracter a evaluar
#   @Return: True si es una letra, False si no
##
def dt_esComentario( self, caracter ):
    if caracter == "{":
        return True
    return False

def dt_comentarios( self, lexema ):

    cont = self.alex.contador

    if lexema == "{":

        caracter = ""
        resto = ""

        while caracter != "}" and cont == self.alex.contador:
            resto += caracter
            caracter = self.alex.leerCaracter()

        if cont != self.alex.contador:
            lexema = lexema + resto
            self.alex.desleer()
            return {
                        "token": self.pr.ERROR,
                        "lexema": "falto cerrar llave " + lexema
                   }
        else:
            lexema = lexema + resto + caracter
            return {
                        "token": self.pr.COMENTARIO,
                        "lexema": lexema
                    }