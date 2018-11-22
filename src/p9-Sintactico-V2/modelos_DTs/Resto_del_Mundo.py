##
# Metodo para reconocer si un caracter es Resto del Mundo
#   @param: caracter a evaluar
#   @Return: True si es digito, False si no
##
def dt_esRestoMundo( self, caracter ):
        restoMundo = [",", ";", "(", ")"]
        return self.perteneceLista( caracter, restoMundo )


##
# Diagrama de Transicion Resto del Mundo
# @Return: diccionario con  token y lexema
#           acorde a la respuesta
##
def dt_restoMundo( self, lexema ):
    
    pos = self.alex.uami.tabla.findSymbol( lexema )
    
    if lexema == ",":

        if pos == -1:
            pos = self.alex.uami.tabla.addItem( lexema, self.pr.RESTO_MUNDO)

        return pos
               

    elif lexema == ";":

        if pos == -1:
            pos = self.alex.uami.tabla.addItem( lexema, self.pr.RESTO_MUNDO)

        return pos
               

    elif lexema == ")":

        if pos == -1:
            pos = self.alex.uami.tabla.addItem( lexema, self.pr.RESTO_MUNDO)

        return  pos
               

    elif lexema == "(":

        if pos == -1:
            pos = self.alex.uami.tabla.addItem( lexema, self.pr.RESTO_MUNDO)

        return pos              