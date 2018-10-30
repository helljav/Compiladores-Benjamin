from PR import Palabras_Reservadas

class Tabla(object):

    ##
    # Constructor
    ##
    def __init__(self):
        self.tope = 0
        self.tabla = []

        print "leng de tabla: ", len(self.tabla)

        # print self.tope
        # print self.columnas
        # print self.renglones#!/usr/bin/env python

        # print self.tabla

    ##
    # Metodo para buscar un simbolo en la tabla
    # @Param lexema: el lexema a buscar en la tabla
    # @Return:
    ##
    def findSymbol( self, lexema ):

        cont = 0

        for lista in self.tabla:

            if lexema is lista[1]:
                return cont

            cont += 1

        return -1

    ##
    # Metodo para obtener token
    # @Param index: indice del elemeto de la tabla
    # @Return token: el token del elemento indice en la tabla
    ##
    def getToken( self, index ):
        return self.tabla[index][0]

    ##
    # Metodo para obtener lexema
    # @Param index: indice del elemeto de la tabla
    # @Return lexema: el lexema del elemento indice en la tabla
    ##
    def getLexema( self, index ):
        return self.tabla[index][1]

    ##
    # Metodo para agregar un nuevo elemento a la tabla
    # @Param token: token del elemento a agregar
    # @Param lexema: lexema del elemeto a agregar
    # @Return:
    ##
    def addItem( self, token, lexema ):

        token = str(token)
        lexema = str(lexema)
        # Validacion
        item = [token, lexema]
        print item
        self.tabla.append(item)

    ##
    # Metodo para imprimir la tabla
    # @Param:
    # @Return:
    ##
    def printTable( self ):

        c = ["Token", "Lexema"]
        cabecera = "\t\t".join(c) + "\n"
        print cabecera

        elementos = ""
        for lista in self.tabla:
            elementos = elementos + "\t\t".join(lista) + "\n"

        print elementos
    ##
    # Metodo para inicializar palabras reservadas
    # @Param:
    # @Return:
    ##
    def runReservedWords(self):
        pr = Palabras_Reservadas()
        self.addItem(pr.palabras_reservadas["suma"]["token"], pr.palabras_reservadas["suma"]["lexema"])


obj = Tabla()
obj.addItem(6,8)
obj.runReservedWords()
obj.printTable()
# print obj.getToken(0)
# print obj.getLexema(0)
# print "indece buscado", obj.findSymbol("6")
