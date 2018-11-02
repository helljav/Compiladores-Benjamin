def dt_Entero(self, lexema):

        cont = self.alex.contador

        if self.esDigito( lexema ):
            # Empieza en cero
            if lexema is "0":
                lexema += self.alex.leerCaracter()
                # Segundo caracter es "otro"
                # Return entero cero
                if self.esDigito( lexema[1] ) == False:
                    self.alex.desleer()
                    return {
                            "token": self.pr.NUM_ENT,
                            "lexema": lexema[ 0 ]
                        }
                # Segundo caracter es un digito
                else:
                    # Se lee todo el numero entero para regresarlo como error y lexema
                    digito = self.alex.leerCaracter()
                    while self.esDigito( digito ) and cont == self.alex.contador:
                        lexema += digito
                        digito = self.alex.leerCaracter()
                    self.alex.desleer()
                    return {
                            "token": self.pr.ERROR,
                            "lexema": lexema
                        }
            # No empieza en cero
            else:
                # lee todo el numero y lo regresa como entero
                digito = lexema
                lexema = ""
                while self.esDigito( digito ) and cont == self.alex.contador:
                    lexema += digito
                    digito = self.alex.leerCaracter()

                self.alex.desleer()
                return {
                            "token": self.pr.NUM_ENT,
                            "lexema": lexema
                        }