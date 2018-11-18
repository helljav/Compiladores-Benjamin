class Parser(object):
    
    def __init__( self, uami ):
        self.uami = uami
        self.preanalisis = {
                            "lexema" : "hola",
                            "token" : 0
                           }

    def inicio( self ):
        #Mandamos a llamar por primera vez a lexico y recibimos su posicion en la tabla de simbolos
        pos = self.uami.alex.alexico()
        self.preanalisis["lexema"] = self.uami.tabla.getLexema( pos )
        self.preanalisis["token"] = self.uami.tabla.getToken( pos )
        self.encabezado()
        self.secuencia()
        # self.parea(self.uami.pr.HECHO)

    def encabezado( self ):

        programa = self.uami.pr.Reservadas["PROGRAMA"]
        identificador  = self.uami.pr.ID
        pc = self.uami.pr.PC

        self.parea( programa )
        self.parea( identificador )
        self.parea( pc )
    
    def secuencia( self ):
        comienza = self.uami.pr.Reservadas["COMIENZA"]
        termina = self.uami.pr.Reservadas["TERMINA"]

        print termina

        self.parea( comienza )

        while self.preanalisis["lexema"] != termina:
            self.asignacion()

            pos = self.uami.alex.alexico()

            if pos == "FIN DE ARCHIVO":
                return True

            self.preanalisis["lexema"] = self.uami.tabla.getLexema( pos )
            self.preanalisis["token"] = self.uami.tabla.getToken( pos )
            
        
        self.parea( termina )
        

    def asignacion( self ):
        identificador = self.uami.pr.ID
        igual = self.uami.pr.IGUAL
        num_entero = self.uami.pr.NUM_ENT
        pc = self.uami.pr.PC

        self.parea( identificador )
        self.parea( igual )
        self.parea( num_entero )
        self.parea( pc )
    
    def parea( self, se_espera ):

        if self.preanalisis["lexema"] == se_espera or self.preanalisis["token"] == se_espera:

            pos = self.uami.alex.alexico()

            if pos == "FIN DE ARCHIVO":
                return True

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
                            "\n\t",
                            "antes de: ",
                            self.preanalisis["lexema"],
                            "\n\n"
                    ]

            self.uami.escribirArchivo( self.uami.urlErr, "a+", texto )
            
            cadRes = self.uami.ventana.getTextAreaResultado()
            cadRes += "<< Error Sintactico Encontrado >>\n"
            
            self.uami.ventana.escribirAreaResultado( cadRes )

            pos = self.uami.alex.alexico()
            
            if pos == "FIN DE ARCHIVO":
                return False

            self.preanalisis["lexema"] = self.uami.tabla.getLexema( pos )
            self.preanalisis["token"] = self.uami.tabla.getToken( pos )
            return False
