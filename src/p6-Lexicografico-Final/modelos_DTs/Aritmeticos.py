def dt_aritmeticos(self, lexema):

        cont = self.alex.contador
    
        # Asignacion
        if lexema is '=':

            if self.alex.leerCaracter() != "=" or self.alex.contador != cont:
                self.alex.desleer()
                return {
                            "token": self.pr.ASIGNACION,
                            "lexema": lexema
                        }
            else:
                self.alex.desleer()
                return self.relacionales( lexema )


        # Suma
        elif lexema is '+':

            return {
                        "token": self.pr.SUMA,
                        "lexema": lexema
                    }

        # Resta
        elif lexema is '-':

            return {
                        "token": self.pr.RESTA,
                        "lexema": lexema
                    }

        # DIVISION
        elif lexema is '/':

            return {
                        "token": self.pr.DIVISION,
                        "lexema": lexema
                    }

        # Multiplicacion
        elif lexema is '*':

            return {
                        "token": self.pr.MULTIPLICACION,
                        "lexema": lexema
                    }
        
        # MODULO
        elif lexema is '%':

            return {
                        "token": self.pr.MODULO,
                        "lexema": lexema
                    }