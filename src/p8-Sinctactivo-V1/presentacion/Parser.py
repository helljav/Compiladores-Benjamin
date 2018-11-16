class Parser(object):
    
    def __init__( self, uami ):
        self.uami = uami
        self.preanalisis = {
                            "lexema" : "hola",
                            "token" : 0
                           }

    def inicio( self ):
        
        pos = self.uami.alex.alexico()
        self.preanalisis["lexema"] = self.uami.tabla.getLexema( pos )
        self.preanalisis["token"] = self.uami.tabla.getToken( pos )
        self.encabezado()
        # self.secuencia()
        # self.parea(self.uami.pr.HECHO)

    def encabezado( self ):

        programa = self.uami.pr.Reservadas["PROGRAMA"]
        identificador  = self.uami.pr.ID
        pc = ";"

        print self.parea( programa )
        print self.parea( identificador )
        print "tercer invocacion de exodia"
        print self.parea( pc )
    
    def secuencia( self ):
        pass
    
    def parea( self, se_espera ):

        if self.preanalisis["lexema"] == se_espera or self.preanalisis["token"] == se_espera:

            print "entre", se_espera

            try:
                pos = self.uami.alex.alexico()
                self.preanalisis["lexema"] = self.uami.tabla.getLexema( pos )
                self.preanalisis["token"] = self.uami.tabla.getToken( pos )
            except:
                print "es un diccionario"
                
                if pos["token"] is self.uami.pr.DELIMITADOR:
                    return self.parea( se_espera )
                
                # Cuando sea Error Token invalido
                elif pos["token"] == self.uami.pr.TOKEN_INV:

                    texto = [
                                "Linea: ",
                                str(self.uami.lineas),
                                "\t",
                                pos["token"],
                                "\n\t",
                                pos["lexema"] + " no Reconocido",
                                "\n\n"
                            ]

                    self.uami.errores += 1 
                   
                    self.uami.escribirArchivo( self.uami.urlErr, "a+", texto )
                    self.uami.ventana.txtAreaFileError.setText( self.uami.getArchivoTexto( self.uami.urlErr ) )
            
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
