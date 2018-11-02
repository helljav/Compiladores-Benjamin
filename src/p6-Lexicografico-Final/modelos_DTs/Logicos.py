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