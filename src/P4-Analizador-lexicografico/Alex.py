
from PR import Palabras_Reservadas

class Alex(object):

    ##
    # Constructor de la clase
    ##
    def __init__( self ):
        self.pr = Palabras_Reservadas()
    
    ##
    # Gramatica que reconoce operador Producto
    # @return: diccionario con el token (PRODUCTO) y su lexema (VALOR)
    # 
    def opeProducto( self, cadena, cont ):

        if cadena[cont] == "*":
            return  { 
                        "token": self.pr.producto,
                        "lexema": cadena[cont]
                    }

    ##
    # Gramatica que reconoce operador Producto
    # @return: diccionario con el token (SUMA) y su lexema (VALOR)
    # 
    def opeSuma( self, cadena, cont ):
        
        pass
        


    ##
    # Gramatica que reconoce operador Producto
    #   
    # @Parametros: la referencia de la clase,
    #              la cadena a evaluar
    #              el contador que recorre la cadena
    #  
    # @return: diccionario con el token (ENTERO) y su lexema (VALOR)
    # 
    def opeEntero( self, cadena, cont ):
        pass


    ##
    # Gramatica que reconoce operador Producto
    #   
    # @Parametros: la referencia de la clase,
    #              la cadena a evaluar
    #              el contador que recorre la cadena
    #  
    # @return: diccionario con el token (INCREMENTO) y su lexema (VALOR)
    # 

    def opeIncremento( self, cadena, cont ):
        pass



