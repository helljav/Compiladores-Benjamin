##
# Metodo para reconocer si un caracter es Relacional
#   @param: caracter a evaluar
#   @Return: True si es relacional, False si no
##
def dt_esRelacional( self, caracter ):
    
    operadores = [ "=", "<", ">", "!" ]
    return self.perteneceLista( caracter, operadores )


##
# Diagrama de Transicion Relacionales
# @Return: diccionario con  token y lexema
#           acorde a la respuesta
##
def dt_relacionales( self, lexema ):

        cont = self.alex.contador
        
        # Caso ==
        if lexema is '=':

            lexema = lexema + self.alex.leerCaracter()

            if lexema[ 1 ] is '=' and cont == self.alex.contador:

                pos = self.alex.uami.tabla.findSymbol( lexema )

                if pos == -1:
                    pos = self.alex.uami.tabla.addItem( lexema, self.pr.RELOP)

                return  pos
                        
        
        # Caso !=
        if lexema is '!':

            lexema = lexema + self.alex.leerCaracter()

            if lexema[ 1 ] is '=' and cont == self.alex.contador:

                pos = self.alex.uami.tabla.findSymbol( lexema )

                if pos == -1:
                    pos = self.alex.uami.tabla.addItem( lexema, self.pr.RELOP)

                return pos
                        
            else: 
                # print "entro del otro lado y voy para alla con el lexema", lexema[0]
                self.alex.desleer()
                return self.logicos( lexema[0] )

        # Caso >= y >
        elif lexema is '>':

            lexema = lexema + self.alex.leerCaracter()

            if lexema[ 1 ] is '=' and cont == self.alex.contador:

                pos = self.alex.uami.tabla.findSymbol( lexema )

                if pos == -1:
                    pos = self.alex.uami.tabla.addItem( lexema, self.pr.RELOP)

                return pos
                        

            else:

                pos = self.alex.uami.tabla.findSymbol( lexema[0] )

                if pos == -1:
                    pos = self.alex.uami.tabla.addItem( lexema[0], self.pr.RELOP)

                self.alex.desleer()
                return  pos
                        
        
        # Caso <= y <
        elif lexema is '<':

            lexema = lexema + self.alex.leerCaracter()

            if lexema[ 1 ] is '=' and cont == self.alex.contador:

                pos = self.alex.uami.tabla.findSymbol( lexema )

                if pos == -1:
                    pos = self.alex.uami.tabla.addItem( lexema, self.pr.RELOP)

                return pos
                        

            else:

                pos = self.alex.uami.tabla.findSymbol( lexema[0] )

                if pos == -1:
                    pos = self.alex.uami.tabla.addItem( lexema[0], self.pr.RELOP)

                self.alex.desleer()
                return  pos
                        