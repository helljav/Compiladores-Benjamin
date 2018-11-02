def dt_relacionales( self, lexema ):

        cont = self.alex.contador
        
        # Caso ==
        if lexema is '=':

            lexema = lexema + self.alex.leerCaracter()

            if lexema[ 1 ] is '=' and cont == self.alex.contador:
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