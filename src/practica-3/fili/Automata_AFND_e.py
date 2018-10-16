class AFND_e(object):

    def __init__( self ):
      self.Listas = []

    def edo_Q0( self, cadena ):

      boleano = False
      mensaje = ""
      
      res = self.edo_Q1( cadena, 0, ["(e,Q1)"] )
      boleano = res[0]

      if boleano == True:
        print "ACEPTADA: La cadena es un impar de ceros"
        mensaje = "ACEPTADA: La cadena es un impar de ceros"
        return mensaje

      else:
        res = self.edo_Q3( cadena, 0, ["(e,Q3)"] )
        boleano = res[0]

        if boleano == True:
          print "ACEPTADA: La cadena No es multiplo de 3"
          mensaje = "ACEPTADA: La cadena No es multiplo de 3"
          return mensaje

        else:
          print "CADENA NO ACEPTADA"
          mensaje = "CADENA NO ACEPTADA"
          return mensaje

    
    def edo_Q1( self, cadena, contador, lista ):

        if len(cadena) == contador:
          lista.append("Camino-Invalido")
          self.Listas.append(lista)
          return False, lista

        elif cadena[ contador ] == "0":
          lista.append("(0,Q2)")
          contador = contador + 1
          return self.edo_Q2( cadena, contador, lista )

        elif cadena[ contador ] == "1":
          lista.append("(1,Q1)")
          contador = contador + 1
          return self.edo_Q1( cadena, contador, lista )

    def edo_Q2( self, cadena, contador, lista ):

        if len(cadena) == contador:
          lista.append("Camino-Valido")
          self.Listas.append(lista)
          return True, lista
        
        elif cadena[ contador ] == "0":
          lista.append("(0,Q1)")
          contador = contador + 1
          return self.edo_Q1( cadena, contador, lista )

        elif cadena[ contador ] == "1":
          lista.append("(1,Q2)")
          contador = contador + 1
          return  self.edo_Q2( cadena, contador, lista )

    
    def edo_Q3( self, cadena, contador, lista ):

        if len(cadena) == contador:
          lista.append("Camino-Invalido")
          self.Listas.append(lista)
          return False, lista

        elif cadena[ contador ] == "0":
          lista.append("(0,Q3)")
          contador = contador + 1
          return self.edo_Q3( cadena, contador, lista )

        elif cadena[ contador ] == "1":
          lista.append("(1,Q4)")
          contador = contador + 1
          return self.edo_Q4( cadena, contador, lista )

    def edo_Q4( self, cadena, contador, lista ):

        if len(cadena) == contador:
          lista.append("Camino-Valido")
          self.Listas.append(lista)
          return True, lista

        elif cadena[ contador ] == "0":
          lista.append("(0,Q4)")
          contador = contador + 1
          return self.edo_Q4( cadena, contador, lista )

        elif cadena[ contador ] == "1":
          lista.append("(1,Q5)")
          contador = contador + 1
          return self.edo_Q5( cadena, contador, lista )

    def edo_Q5( self, cadena, contador, lista ):

        if len(cadena) == contador:
          lista.append("Camino-Valido")
          self.Listas.append(lista)
          return True, lista

        elif cadena[ contador ] == "0":
          lista.append("(0,Q5)")
          contador = contador + 1
          return self.edo_Q5( cadena, contador, lista )

        elif cadena[ contador ] == "1":
          lista.append("(1,Q3)")
          contador = contador + 1
          return self.edo_Q3( cadena, contador, lista )
