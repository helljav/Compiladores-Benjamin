class Automata(object):

    def edo_Q0( self, cadena, contador, lista ):

        lista.append("Q0")
        contador = contador + 1

        if len(cadena) == contador:
          return False, lista
        
        elif cadena[ contador ] == "0":
          return self.edo_Q1( cadena, contador, lista )

        elif cadena[ contador ] == "1":
          return  self.edo_Q0( cadena, contador, lista )

    
    def edo_Q1( self, cadena, contador, lista ):

        lista.append("Q1")
        contador = contador + 1

        if len(cadena) == contador:
          return False, lista

        elif cadena[ contador ] == "0":
          return self.edo_Q2( cadena, contador, lista )

        elif cadena[ contador ] == "1":
          return self.edo_Q0( cadena, contador, lista )

    def edo_Q2( self, cadena, contador, lista ):

        lista.append("Q2")
        contador = contador + 1

        if len(cadena) == contador:
          return True, lista

        elif cadena[ contador ] == "0":
          return self.edo_Q2( cadena, contador, lista )

        elif cadena[ contador ] == "1":
          return self.edo_Q0( cadena, contador, lista )
