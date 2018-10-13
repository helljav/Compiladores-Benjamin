class AFND(object):

    def __init__( self ):
      self.Listas = []

    def vueltaAtras( self, cadena ):

      lista = []
      retroceso = 0
      contador = 0
      res = False
      
      FzaBruta = self.edo_Q0_Q0( cadena, contador, lista )
      
      res = FzaBruta[0]
      
      if(res == False):

        contador = FzaBruta[2]
        print contador
        lista = FzaBruta[1][0:contador]
        print lista
        retroceso = 0

        while( retroceso < len(cadena) and len(lista) > 0):
          
          if( lista[contador -1] == "(0,Q0)"):
            contador = contador - 1
            lista = lista[0:contador]
            self.edo_Q0_Q1( cadena, contador, lista )
          else:
                contador = contador - 1
                lista =  lista[0:contador]
              

          


    def edo_Q0_Q0( self, cadena, contador, lista ):

        if len(cadena) == contador:
          lista.append("Camino Invalido")
          self.Listas.append(lista)
          return False, lista, contador
        
        elif cadena[ contador ] == "0":
          lista.append("(0,Q0)")
          contador = contador + 1
          return self.edo_Q0_Q0( cadena, contador, lista )

        elif cadena[ contador ] == "1":
          lista.append("(1,Q0)")
          contador = contador + 1
          return  self.edo_Q0_Q0( cadena, contador, lista )

    def edo_Q0_Q1( self, cadena, contador, lista ):

      if len(cadena) == contador:
          lista.append("Camino Invalido")
          self.Listas.append(lista)
          return False, lista, contador
        
      elif cadena[ contador ] == "0":
        lista.append("(0,Q1)")
        contador = contador + 1
        return self.edo_Q1( cadena, contador, lista )

    def edo_Q1( self, cadena, contador, lista ):

        if len(cadena) == contador:
          lista.append("Camino Invalido")
          self.Listas.append(lista)
          return False, lista, contador
        
        elif cadena[ contador ] == "1":
          lista.append("(1,Q2)")
          contador = contador + 1
          self.edo_Q2( cadena, contador, lista )
    
    def edo_Q2( self, cadena, contador, lista ):

        if len(cadena) == contador:
          lista.append("Camino VALIDO")
          self.Listas.append(lista)
          return True, lista, contador
        
        elif cadena[ contador ] == "0":
          return False, lista

        elif cadena[ contador ] == "1":
          return False, lista