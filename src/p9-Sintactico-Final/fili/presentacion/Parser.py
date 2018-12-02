class Parser(object):
    
    def __init__( self, uami ):
        self.uami = uami
        self.preanalisis = {
                            "lexema" : "",
                            "token" : 0
                           }

    ## 
    #  BNF
    #  <encabezado> -> <estructura> -> HECHO;
    ##
    def inicio( self ):
        
        pos = self.uami.alex.alexico()
        self.preanalisis["lexema"] = self.uami.tabla.getLexema( pos )
        self.preanalisis["token"] = self.uami.tabla.getToken( pos )
        
        self.encabezado()
        self.estructura()
        print "fin estructura"
        self.parea(self.uami.pr.HECHO)
        print "hecho reconocido"


    ## 
    #  BNF
    #  PROGRAMA -> ID -> ;
    ##
    def encabezado( self ):
        programa = self.uami.pr.Reservadas["PROGRAMA"]
        identificador  = self.uami.pr.ID
        pc = self.uami.pr.PC

        self.parea( programa )
        self.parea( identificador )
        self.parea( pc )

    ## 
    #  BNF
    #  COMIENZA -> <enunciado>* -> TERMINA
    ##
    def estructura( self ):
        comienza = self.uami.pr.Reservadas["COMIENZA"]
        termina = self.uami.pr.Reservadas["TERMINA"]
        hasta = self.uami.pr.Reservadas["HASTA"]
        

        self.parea(comienza);
        
        while self.preanalisis["lexema"] != termina and  \
              self.preanalisis["lexema"] != self.uami.pr.HECHO:
                    self.enunciado()

        self.parea(termina)

    def enunciado( self ):

        # print self.preanalisis["token"]
        print self.preanalisis["lexema"]
        
        # ESTRUCTURA
        if self.preanalisis["lexema"] == self.uami.pr.Reservadas["COMIENZA"]:
            self.estructura()
        
        # ASIGNACION
        elif self.preanalisis["token"] == self.uami.pr.ID:
                self.asignacion()

        # ENUNC_CONDICIONAL
        elif self.preanalisis["lexema"] == self.uami.pr.Reservadas["SI"]:
                self.enunc_condicional()

        # ENUNC_MIENTRAS
        elif self.preanalisis["lexema"] == self.uami.pr.Reservadas["MIENTRAS"]:
                self.enunc_mientras()

        # ENUNC_PARA
        elif self.preanalisis["lexema"] == self.uami.pr.Reservadas["PARA"]:
                self.enunc_para()

        # ENUNC_IMPRESION
        elif self.preanalisis["lexema"] == self.uami.pr.Reservadas["IMPRIME"]:
                self.enunc_impresion()

        #ENUNC_REPITE
        elif self.preanalisis["lexema"] == self.uami.pr.Reservadas["REPITE"]:
                self.enunc_repite()

        # ;
        elif self.preanalisis["lexema"] == self.uami.pr.PC:
            self.parea(self.uami.pr.PC)

        else:
            self.uami.alex.GenErrores.errorSintactico("enunciado", self.preanalisis)
            self.leerToken()

    ##
    # ID -> ASIGNACION -> <expresion> -> ;
    ##
    def asignacion( self ):
        identificador = self.uami.pr.ID
        asignacion = self.uami.pr.IGUAL
        pc = self.uami.pr.PC

        self.parea( identificador )
        self.parea( asignacion )
        self.expresion()
        self.parea( pc )

    ##
    # SI -> <expresion> -> ENTONCES -> <enunciado>
    ##
    def enunc_condicional(self):
        si = self.uami.pr.Reservadas["SI"]
        entonces = self.uami.pr.Reservadas["ENTONCES"]
        otro = self.uami.pr.Reservadas["OTRO"]

        self.parea( si )
        self.expresion()
        self.parea( entonces )
        self.enunciado()

        if self.preanalisis["lexema"] is otro:
            self.leerToken()
            self.enunciado()

    ##
    # MIENTRAS -> <expresion> -> HAZ -> <enunciado>
    ##
    def enunc_mientras(self):
        mientras = self.uami.pr.Reservadas["MIENTRAS"]
        haz = self.uami.pr.Reservadas["HAZ"]

        self.parea( mientras )
        self.expresion()
        self.parea( haz )
        self.enunciado()

    ##
    # PARA -> ID -> ASIGNACION -> <expresion> -> A -> <expresion> -> HAZ -> <enunciado>
    ##
    def enunc_para(self):
        para = self.uami.pr.Reservadas["PARA"]
        identificador = self.uami.pr.ID
        asignacion = self.uami.pr.IGUAL
        a = self.uami.pr.Reservadas["A"]
        haz = self.uami.pr.Reservadas["HAZ"]

        self.parea( para )
        self.parea( identificador )
        self.parea( asignacion )
        self.expresion()
        self.parea( a )
        self.expresion()
        self.parea( haz )
        self.enunciado()


    ##
    # IMPRIME -> ( -> CADENA -> , -> <expresion> -> ) -> ;
    ##
    def enunc_impresion(self):
        imprime = self.uami.pr.Reservadas["IMPRIME"]
        p_abre = self.uami.pr.P_ABRE
        cadena = self.uami.pr.STRINGS
        coma = self.uami.pr.COMA
        p_cierra = self.uami.pr.P_CIERRA
        pc = self.uami.pr.PC

        self.parea( imprime )
        self.parea( p_abre )
        self.parea( cadena )
        self.parea( coma )
        self.expresion()
        self.parea( p_cierra )
        self.parea( pc )

    ##
    # REPITE -> <enunciado> -> HASTA -> <expresion> -> ;
    ##
    def enunc_repite(self):
        repite = self.uami.pr.Reservadas["REPITE"]
        hasta = self.uami.pr.Reservadas["HASTA"]
        pc = self.uami.pr.PC
        termina = self.uami.pr.Reservadas["TERMINA"]

        self.parea( repite )
        self.enunciado()
        self.parea( hasta )
        self.expresion()
        self.parea( pc )


    ##################### Expresion  #########################

    ##
    # <expresion>: <expresion_simple> -> ( LOGOP <expresion_simple | RELOP <expresion_simple> | e)
    ##
    def expresion( self ):

        relop = self.uami.pr.RELOP
        logop = self.uami.pr.LOGOP

        self.expresion_simple()

        if self.preanalisis["token"] == relop:
            self.parea( relop )
            self.expresion_simple();
        
        elif self.preanalisis["token"] == logop:
            self.parea(logop)
            self.expresion_simple();

    ##
    # <exp_simple>: <termino> -> ( ADDOP <termino> | e )
    ##
    def expresion_simple( self ):

        mas = self.uami.pr.MAS
        menos = self.uami.pr.MENOS

        self.termino()

        if self.preanalisis["lexema"] == mas:
            self.parea( mas )
            self.termino()
        elif self.preanalisis["lexema"] == menos:
            self.parea( menos )
            self.termino()


    ##
    # <termino> : <factor> ( MULOP <termino> | e)
    ##
    def termino( self ):
        mult = self.uami.pr.MULT
        div = self.uami.pr.DIV

        self.factor()
        
        if self.preanalisis["lexema"] == mult:
            self.parea( mult )
            self.termino()
        elif self.preanalisis["lexema"] == div:
            self.parea( div )
            self.termino()

    ##
    #<factor>: [ NUM_ENT | ID | ( -> <expresion> -> ) ]
    ##
    def factor( self ):
        p_abre = self.uami.pr.P_ABRE
        p_cierra = self.uami.pr.P_CIERRA
        num_entero = self.uami.pr.NUM_ENT
        identificador = self.uami.pr.ID

        if self.preanalisis["lexema"] == p_abre:
            self.parea( p_abre )
            self.expresion()
            self.parea( p_cierra )
        
        elif self.preanalisis["token"] == num_entero:
            self.parea( num_entero )
        
        elif self.preanalisis["token"] == identificador:
            self.parea( identificador )
        
        else:
            self.uami.alex.GenErrores.errorSintactico("una expresion", self.preanalisis)

    ##
    # Metodo para comparar tokens
    ##
    def parea( self, se_espera ):
        if self.preanalisis["lexema"] == se_espera or self.preanalisis["token"] == se_espera:
            self.leerToken()
            return True
        else:
            self.uami.alex.GenErrores.errorSintactico(se_espera, self.preanalisis)
            return False

    ##
    # Metodo para leer tokens
    ##
    def leerToken( self ):
        try:
            pos = self.uami.alex.alexico()
            self.preanalisis["lexema"] = self.uami.tabla.getLexema( pos )
            self.preanalisis["token"] = self.uami.tabla.getToken( pos )
            
        except:
            self.preanalisis["lexema"] = self.uami.pr.HECHO
