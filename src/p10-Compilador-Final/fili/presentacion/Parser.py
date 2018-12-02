from Generador_CI import Generador_CI

class Parser(object):
    
    def __init__( self, uami ):
        self.uami = uami
        self.gci = Generador_CI(uami)
        self.etiqueta = 0
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
        self.parea(self.uami.pr.HECHO)
        self.gci.emite(self.uami.pr.HALT, None)


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

        self.parea(comienza);
        
        while self.preanalisis["lexema"] != termina and  \
              self.preanalisis["lexema"] != self.uami.pr.HECHO:
                    self.enunciado()

        self.parea(termina)

    def enunciado( self ):
        
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
    # BNF 
    # ID -> ASIGNACION -> <expresion> -> ;
    #  
    # BNF CON CODIGO INTERMEDIO
    # emite(lvalue, lexema)
    # ID -> ASIGNACION -> <expresion>
    #                               emite(asign,null)
    #  -> ;
    ##
    def asignacion( self ):
        identificador = self.uami.pr.ID
        asignacion = self.uami.pr.IGUAL
        pc = self.uami.pr.PC

        lvalue = self.uami.pr.VALOR_I
        amarre = self.uami.pr.ASIGN

        self.gci.emite( lvalue, self.preanalisis["lexema"])
        self.parea(identificador)
        self.parea(asignacion)
        self.expresion()
        self.gci.emite( amarre, None )
        self.parea( pc )

    ##
    # BNF 
    # SI -> <expresion> -> ENTONCES -> <enunciado> -> [ OTRO <enunciado> | e] 
    #
    # BNF CON CODIGO INTERMEDIO
    # SI -> <expresion>
    #                   emite(gofalse, cond = etiqueta++) 
    # -> ENTONCES -> <enunciado>
    #                   emite(goto, salida = etiqueta++) 
    # -> [ OTRO
    #              emite(label, cond)
    # -> <enunciado> | e ]
    #              emite(label, salida)  
    ##
    def enunc_condicional(self):
        si = self.uami.pr.Reservadas["SI"]
        entonces = self.uami.pr.Reservadas["ENTONCES"]
        otro = self.uami.pr.Reservadas["OTRO"]

        gofalse = self.uami.pr.SI_FALSO_VE_A
        goto = self.uami.pr.VE_A
        label = self.uami.pr.ETIQUETA

        self.parea( si )
        self.expresion()

        self.etiqueta += 1
        cond = self.etiqueta
        self.gci.emite( gofalse, str(cond))

        self.parea( entonces )
        self.enunciado()

        self.etiqueta +=1
        salida = self.etiqueta
        self.gci.emite( goto, str(salida))

        if self.preanalisis["lexema"] is otro:
            self.gci.emite( label, str(cond))
            self.leerToken()
            self.enunciado()
        
        self.gci.emite( label, str(salida))

    ##
    # BNF 
    # MIENTRAS -> <expresion> -> HAZ -> <enunciado>
    #  
    # BNF CON CODIGO INTERMEDIO
    # MIENTRAS
    #       emite(label, cond = etiqueta++) 
    #  -> <expresion>
    #       emite(gofalse, salida = etiqueta++) 
    #  -> HAZ -> <enunciado>
    #       emite(goto, cond)
    #       emite(label, salida)  
    ##
    def enunc_mientras(self):
        mientras = self.uami.pr.Reservadas["MIENTRAS"]
        haz = self.uami.pr.Reservadas["HAZ"]

        goto = self.uami.pr.VE_A
        gofalse = self.uami.pr.SI_FALSO_VE_A
        label = self.uami.pr.ETIQUETA

        self.parea( mientras )
        
        self.etiqueta += 1
        cond = self.etiqueta
        self.gci.emite( label, str(cond))
        
        self.expresion()

        self.etiqueta += 1
        salida = self.etiqueta
        self.gci.emite( gofalse, str(salida))

        self.parea( haz )
        self.enunciado()

        self.gci.emite( goto, str(cond))
        self.gci.emite( label, str(salida))

    ##
    # BNF
    # PARA -> ID -> ASIGNACION -> <expresion> -> A -> <expresion> -> HAZ -> <enunciado>
    #
    # BNF CI
    # PARA
    #   emite(lvalue, c= lexema) 
    # -> ID -> ASIGNACION -> <expresion>
    #   emite(asign,null)
    # -> A
    #   emite(label,entrada = etiqueta++)
    #   emite(rvalue, c)
    # -> <expresion>
    #   emite(Relop, LE)
    #   emite(gofalse, salida = etiqueta++)
    # -> HAZ -> <enunciado>
    #   emite(lvalue,c) 
    #   emite(rvalue,c) 
    #   emite(push,1) 
    #   emite(addop, mas) 
    #   emite(asign, null) 
    #   emite(goto,entrada) 
    #   emite(label,salida) 
    ##
    def enunc_para(self):
        para = self.uami.pr.Reservadas["PARA"]
        identificador = self.uami.pr.ID
        asignacion = self.uami.pr.IGUAL
        a = self.uami.pr.Reservadas["A"]
        haz = self.uami.pr.Reservadas["HAZ"]

        relop = self.uami.pr.RELOP
        le = self.uami.pr.LE
        mas = self.uami.pr.MAS
        goto = self.uami.pr.VE_A
        gofalse = self.uami.pr.SI_FALSO_VE_A
        label = self.uami.pr.ETIQUETA
        lvalue = self.uami.pr.VALOR_I
        rvalue = self.uami.pr.VALOR_D
        amarre = self.uami.pr.ASIGN
        push = self.uami.pr.PUSH

        self.parea( para )

        c = self.preanalisis["lexema"]
        self.gci.emite( lvalue, c)

        self.parea( identificador )
        self.parea( asignacion )
        self.expresion()

        self.gci.emite( amarre, None )

        self.parea( a )

        self.etiqueta += 1
        entrada = self.etiqueta
        self.gci.emite(label,str(entrada))
        self.gci.emite(rvalue, c)

        self.expresion()

        self.gci.emite(relop, le)
        self.etiqueta += 1
        salida = self.etiqueta
        self.gci.emite(gofalse, str(salida))

        self.parea( haz )
        self.enunciado()

        self.gci.emite( lvalue, c ) 
        self.gci.emite( rvalue, c ) 
        self.gci.emite( push, str(1) ) 
        self.gci.emite( mas, None ) 
        self.gci.emite( amarre, None ) 
        self.gci.emite( goto, str(entrada) )
        self.gci.emite( label, str(salida) )


    ##
    # BNF 
    # IMPRIME -> ( -> CADENA -> [,<expresion>]* -> ) -> ;
    #
    # BNF CI
    # IMPRIME -> (
    #   emite(print, lexema)
    # -> CADENA -> [,<expresion>
    #   emite(write, null)
    # ]* -> ) -> ;
    ##
    def enunc_impresion(self):
        imprime = self.uami.pr.Reservadas["IMPRIME"]
        p_abre = self.uami.pr.P_ABRE
        cadena = self.uami.pr.STRINGS
        coma = self.uami.pr.COMA
        p_cierra = self.uami.pr.P_CIERRA
        pc = self.uami.pr.PC

        IMPRIME = self.uami.pr.IMPRIME
        write = self.uami.pr.ESCRIBE

        self.parea( imprime )
        self.parea( p_abre )
        
        self.gci.emite(IMPRIME, self.preanalisis["lexema"] )
        
        if self.parea( cadena ):
            
            while self.preanalisis["lexema"] != p_cierra and \
                  self.preanalisis["lexema"] != self.uami.pr.HECHO:  
         
                res_coma = self.parea( coma )
                res_expresion = self.expresion()

                if res_coma == False or res_expresion == False:
                    break

        else:
            while self.preanalisis["lexema"] != p_cierra and \
                  self.preanalisis["lexema"] != self.uami.pr.HECHO:  
         
                res_coma = self.parea( coma )
                res_expresion = self.expresion()

                if res_coma == False or res_expresion == False:
                    break

        self.gci.emite(write, None )
        self.parea( p_cierra )
        self.parea( pc )

    ##
    # BFN 
    # REPITE -> <enunciado> -> HASTA -> <expresion> -> ;
    # 
    # BFN CI
    # REPITE
    #   emite(label, ciclo=etiqueta++)
    #  -> <enunciado> -> HASTA -> <expresion>
    #   emite(gofalse,ciclo)
    #  -> ; 
    ##
    def enunc_repite(self):
        repite = self.uami.pr.Reservadas["REPITE"]
        hasta = self.uami.pr.Reservadas["HASTA"]
        pc = self.uami.pr.PC

        gofalse = self.uami.pr.SI_FALSO_VE_A
        label = self.uami.pr.ETIQUETA

        self.parea( repite )
        
        self.etiqueta += 1
        ciclo = self.etiqueta
        self.gci.emite(label, str(ciclo))

        self.enunciado()
        self.parea( hasta )
        self.expresion()

        self.gci.emite(gofalse, str(ciclo))

        self.parea( pc )


    ##################### Expresion  #########################

    ##
    # BFN 
    # <expresion_simple> -> ( LOGOP <expresion_simple | RELOP <expresion_simple> | e)
    # 
    # BFN CI
    #  <expresion_simple>
    #       aux = lexema
    #  -> ( LOGOP <expresion_simple
    #       emite(RELOP, aux)
    #  | RELOP <expresion_simple>
    #       emite(LOGOP, aux)
    #  | e) 
    ##
    def expresion( self ):

        relop = self.uami.pr.RELOP
        logop = self.uami.pr.LOGOP

        res = self.expresion_simple()
        aux = self.preanalisis["lexema"]

        if self.preanalisis["token"] == relop:
            self.parea( relop )
            self.expresion_simple();
            self.gci.emite(relop, aux)
        
        elif self.preanalisis["token"] == logop:
            self.parea(logop)
            self.expresion_simple();
            self.gci.emite(logop, aux)

        if res == False:
            return False

    ##
    # BNF 
    # <termino> -> ( ADDOP <termino> | e )
    # 
    # BFN CI
    # <termino>
    #   aux = lexema
    #  -> ( ADDOP <termino> 
    #   emite(ADDOP, aux)
    # | e )
    ##
    def expresion_simple( self ):

        mas = self.uami.pr.MAS
        menos = self.uami.pr.MENOS

        res = self.termino()
        lexema = self.preanalisis["lexema"]

        if lexema == mas:
            self.parea( mas )
            self.termino()
            self.gci.emite(mas, None)

        elif lexema == menos:
            self.parea( menos )
            self.termino()
            self.gci.emite(menos, None)

        if res == False:
            return False

    ##
    # BNF 
    # <factor> ( MULOP <termino> | e)
    # 
    # BFN
    # <factor> 
    #   aux = lexema
    #  ( MULOP <termino>
    #   emite(MULOP,aux)
    #  | e )
    ##
    def termino( self ):
        mult = self.uami.pr.MULT
        div = self.uami.pr.DIV

        res = self.factor()
        lexema = self.preanalisis["lexema"]
        
        if lexema == mult:
            self.parea( mult )
            self.termino()
            self.gci.emite(mult,None)
            
        elif lexema == div:
            self.parea( div )
            self.termino()
            self.gci.emite(div,None)
        
        if res == False:
            return False
            
    ##
    # BNF 
    #<factor>: [ NUM_ENT | ID | ( -> <expresion> -> ) ]
    # 
    # BNF CI
    # <factor>: [
    #   emite(push, lexema)
    #  NUM_ENT |
    #   emite(rvalue, lexema) 
    #  ID | ( -> <expresion> -> ) ]
    ##
    def factor( self ):
        p_abre = self.uami.pr.P_ABRE
        p_cierra = self.uami.pr.P_CIERRA
        num_entero = self.uami.pr.NUM_ENT
        identificador = self.uami.pr.ID

        push = self.uami.pr.PUSH
        rvalue = self.uami.pr.VALOR_D
        lexema = self.preanalisis["lexema"]

        if self.preanalisis["lexema"] == p_abre:
            self.parea( p_abre )
            self.expresion()
            self.parea( p_cierra )
        
        elif self.preanalisis["token"] == num_entero:
            self.gci.emite(push,lexema)
            self.parea( num_entero )
        
        elif self.preanalisis["token"] == identificador:
            self.gci.emite(rvalue,lexema)
            self.parea( identificador )
        else:
            self.uami.alex.GenErrores.errorSintactico("una expresion", self.preanalisis)
            return False

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
