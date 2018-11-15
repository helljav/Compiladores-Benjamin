class Parser(object):
    
    def __init__( self, uami ):
        self.uami = uami
        self.preanalisis = {
                            "lexema" : "hola",
                            "token" : 0
                           }

    def inicio( self ):
        
        pos = self.uami.alex.alexico()["token"]
        print pos
        self.preanalisis["lexema"] = self.uami.tabla.getLexema( pos )
        self.preanalisis["token"] = self.uami.tabla.getToken( pos )
        print self.preanalisis["lexema"]
        print self.preanalisis["token"]
        self.encabezado()
        # self.secuencia()
        # self.parea(self.uami.pr.HECHO)

    def encabezado( self ):

        programa = self.uami.pr.Reservadas["PROGRAMA"]
        pc = ";"
        programa = self.uami.pr.Reservadas["PROGRAMA"]

        self.parea( programa )
    
    def secuencia( self ):
        pass
    
    def parea( self, se_espera ):

        if self.preanalisis["lexema"] == se_espera or self.preanalisis["token"] == se_espera:
            pos = self.uami.alex.alexico()
            self.preanalisis["lexema"] = self.uami.tabla.getLexema( pos )
            self.preanalisis["token"] = self.uami.tabla.getToken( pos )
            return True

        else:
            self.uami.errores += 1

            texto = [
                            "Linea: ",
                            str(self.uami.lineas),
                            "\t",
                            self.uami.pr.ERROR_SINTACTICO,
                            "\n\t",
                            "Se esperaba: ",
                            se_espera,
                            "\n\n"
                    ]

            self.uami.escribirArchivo( self.uami.urlErr, "a+", texto )
            return False