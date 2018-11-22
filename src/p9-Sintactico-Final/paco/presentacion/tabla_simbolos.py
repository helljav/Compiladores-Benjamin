class Tabla(object):

    ##
    # Constructor
    ##
    def __init__(self, pr):
        self.pr = pr
        self.tope = 0
        self.tabla = []

    ##
    # Metodo para buscar un simbolo en la tabla
    # @Param lexema: el lexema a buscar en la tabla
    # @Return:
    ##
    def findSymbol( self, lexema ):

        indice = self.tope - 1
        for lista in reversed(self.tabla):
            if lexema == lista[0]:
                return indice
            indice -= 1
        return -1

    ##
    # Metodo para obtener token
    # @Param pos: indice del elemeto de la tabla
    # @Return token: el token del elemento indice en la tabla
    ##
    def getToken( self, pos ):
        return self.tabla[pos][1]

    ##
    # Metodo para obtener lexema
    # @Param pos: indice del elemeto de la tabla
    # @Return lexema: el lexema del elemento indice en la tabla
    ##
    def getLexema( self, pos ):
        return self.tabla[pos][0]

    ##
    # Metodo para agregar un nuevo elemento a la tabla
    # @Param token: token del elemento a agregar
    # @Param lexema: lexema del elemeto a agregar
    # @Return:
    ##
    def addItem( self, lexema, token ):
        indice = self.tope
        self.tope += 1
        item = [ lexema, token ]
        self.tabla.append(item)
        return indice

    ##
    # Metodo para imprimir la tabla
    # en la consola a modo de pruebas  
    ##
    def imprimirTabla( self ):
        
        indice = self.tope - 1

        cadTabla = [
            "\n\n",
            "<<<<<\tTabla\t>>>>>",
            "\n\n",
            "indice",
            "\t",
            "Lexema",
            "\t",
            "Token",
            "\n\n"
            ]

        for lista in reversed( self.tabla ):
            texto = str(indice) + "\t" + "\t".join(lista) + "\n"
            cadTabla.append( texto )
            indice -= 1

        return cadTabla

    ##
    # Metodo para inicializar palabras reservadas
    ##
    def cargarPal_Res(self):
 
        valores = self.pr.Reservadas.values()
        
        for valor in valores:
            self.addItem( valor, self.pr.P_RES )
