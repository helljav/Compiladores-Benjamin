##
# Metodo para reconocer si un caracter es una letra permitida
#   @param: caracter a evaluar
#   @Return: True si es una letra, False si no
##
def dt_esLetra( self, caracter ):
    letras = []
    for i in range(97,123):
        letras.append( chr(i) )
    return self.perteneceLista( caracter, letras )

##
# Metodo para reconocer si un caracter puede ser identificador
#   @param: caracter a evaluar
#   @Return: True si es una letra o guion bajo, False si no
##
def dt_esIdentificador( self, caracter ):
    if caracter == "_" or self.esLetra( caracter ) == True:
        return True
    
    return False

def dt_identificadores( self, lexema ):

    cont = self.alex.contador

    if self.esLetra( lexema ) or lexema is "_":

        id = lexema
        lexema = "" 
        while ( self.esLetra( id ) or self.esDigito( id ) or id == "_" ) and cont == self.alex.contador:
            lexema += id
            id = self.alex.leerCaracter()

        posicion = self.alex.uami.tabla.findSymbol( lexema )

        if posicion == -1:
            posicion = self.alex.uami.tabla.addItem( lexema, self.pr.ID )
    
        self.alex.desleer()
        return posicion
                