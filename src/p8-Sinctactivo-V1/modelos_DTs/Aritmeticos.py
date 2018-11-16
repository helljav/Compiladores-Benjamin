##
# Metodo para reconocer si un caracter es Aritmetico
#   @param: caracter a evaluar
#   @Return: True si es aritmetico, False si no
##
def dt_esAritmetico( self, caracter ):
    operadores = [ "=", "-", "+", "/", "*", "%" ]
    return self.perteneceLista( caracter, operadores )

##
# Diagrama de Transicion Aritmeticos
# @Return: diccionario con  token y lexema
#           acorde a la respuesta
##
def dt_aritmeticos(self, lexema):

        cont = self.alex.contador
        pos = self.alex.uami.tabla.findSymbol( lexema )
    
        # Asignacion
        if lexema is "=":

            if self.alex.leerCaracter() != "=" or self.alex.contador != cont:

                if pos == -1:
                    pos = self.alex.uami.tabla.addItem( lexema, self.pr.ASIGNACION)

                self.alex.desleer()
                
                return pos
                        
            else:
                self.alex.desleer()
                return self.relacionales( lexema )


        # Suma
        elif lexema is '+':

            if pos == -1:
                pos = self.alex.uami.tabla.addItem( lexema, self.pr.SUMA)
            return pos
                    

        # Resta
        elif lexema is '-':

            if pos == -1:
                pos = self.alex.uami.tabla.addItem( lexema, self.pr.RESTA)
            
            return pos
                    

        # DIVISION
        elif lexema is '/':

            if pos == -1:
                pos = self.alex.uami.tabla.addItem( lexema, self.pr.DIVISION)

            return pos
                    

        # Multiplicacion
        elif lexema is '*':

            if pos == -1:
                pos = self.alex.uami.tabla.addItem( lexema, self.pr.MULTIPLICACION)

            return pos
                    
        
        # MODULO
        elif lexema is '%':

            if pos == -1:
                pos = self.alex.uami.tabla.addItem( lexema, self.pr.MODULO)

            return pos
                    