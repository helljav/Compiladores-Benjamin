class AFND(object):

    ##
    # Constructor
    # atributo Listas
    # guarda los caminos posibles
    ##

    def __init__( self ):
      self.Listas = []

    ##
    #  Buscar posibles caminos con Bactrack
    ##
    def vueltaAtras( self, cadena ):

      lista = []
      contador = 0
      res = False
      
      # Aplico Fuerza Bruta
      FzaBruta = self.edo_Q0_Q0( cadena, contador, lista )
      
      # Retomo el booleano que sera False
      res = FzaBruta[0]
      
      if(res == False):

        # Seteo las variables
        contador = FzaBruta[2]
        lista = FzaBruta[1][0:contador]

        # Mientras lista siga conteniendo elementos
        while( len(lista) > 0 ):

          # Si el ultimo elemento es 0
          if( lista[contador -1] == "(0,Q0)"):

            # y Si el penultimo tambien es 0
            # Tenemos dos ceros consecutivos, cambio
            # de trancision para el 2do cero
            if( lista[contador -2] == "(0,Q0)"):
              contador = contador - 1
              lista = lista[0:contador]
              self.edo_Q0_Q1( cadena, contador, lista )
            
            # Sino, es 1 entonces se retrocede
            else:
              contador = contador - 1
              lista =  lista[0:contador]

              # Si al retroceder llegamos al inicio pero este 
              # tambien es 1, entonces cambiamos de transicion
              # Para no desbordar la lista
              if(len(lista) == 1 and lista[0] == "(1,Q0)"):
                self.edo_Q0_Q1( cadena, contador, lista )
          
          # Sino, es 1 entonces se retrocede
          else:
                contador = contador - 1
                lista =  lista[0:contador]    

    ## 
    # Metodo que simula un camino para la transicion Q0-Q0
    ##
    def edo_Q0_Q0( self, cadena, contador, lista ):

        # Si es el fin de la cadena
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

    ## 
    # Metodo que simula un camino para la transicion Q0-Q1
    ##
    def edo_Q0_Q1( self, cadena, contador, lista ):

      # Si es el fin de la cadena
      if len(cadena) == contador:
          lista.append("Camino Invalido")
          self.Listas.append(lista)
          return False, lista, contador
      
      elif cadena[ contador ] == "1":
          lista.append("(1,Q0)")
          contador = contador + 1
          return  self.edo_Q0_Q0( cadena, contador, lista )
        
      elif cadena[ contador ] == "0":
        lista.append("(0,Q1)")
        contador = contador + 1
        return self.edo_Q1( cadena, contador, lista )

    def edo_Q1( self, cadena, contador, lista ):

      # Si es el fin de la cadena
        if len(cadena) == contador:
          lista.append("Camino Invalido")
          self.Listas.append(lista)
          return False, lista, contador
       
        elif cadena[ contador ] == "1":
          lista.append("(1,Q2)")
          contador = contador + 1
          self.edo_Q2( cadena, contador, lista )

      # Ya no tiene mas salidas a 0
        elif cadena[ contador ] == "0":
          lista.append("Camino Invalido")
          self.Listas.append(lista)
          return False
    
    def edo_Q2( self, cadena, contador, lista ):

        # Si es el fin de la cadena
        if len(cadena) == contador:
          lista.append("Camino VALIDO")
          self.Listas.append(lista)
          return True, lista, contador
        
        # Ya no tiene mas salidas a 1
        elif cadena[ contador ] == "1":
          lista.append("Camino Invalido")
          self.Listas.append(lista)
          return False

        # Ya no tiene mas salidas a 0
        elif cadena[ contador ] == "0":
          lista.append("Camino Invalido")
          self.Listas.append(lista)
          return False