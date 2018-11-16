##
# Metodo para reconocer si un caracter puede ser cadena
#   @param: caracter a evaluar
#   @Return: True si es una letra, False si no
##
def dt_esCadena( self, caracter ):
    if caracter == "\"":
        return True
    return False

def dt_cadenas( self, lexema ):

    cont = self.alex.contador

    if lexema == "\"":

        caracter = ""
        resto = ""

        while caracter != "\"" and cont == self.alex.contador:
            resto += caracter
            caracter = self.alex.leerCaracter()

        if cont != self.alex.contador:
            lexema = lexema + resto
            self.alex.desleer()
            return {
                        "token": self.pr.ERROR,
                        "lexema": "falto cerrar la comilla " + lexema
                   }
        else:
            lexema = lexema + resto + caracter
            
            pos = self.alex.uami.tabla.findSymbol( lexema )
            
            if pos == -1:
                pos = self.alex.uami.tabla.addItem( lexema, self.pr.STRINGS )

            return pos                  