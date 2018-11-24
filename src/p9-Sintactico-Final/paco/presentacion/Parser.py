from generadorError import GeneradorError
class Parser(object):

    """
    Clase del analisador sintactico
    """
    #Constructor
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
        #Mandamos a llamar a los metodos, segun la gramtica libre de contexto
        self.encabezado()
        self.estructura()
        #self.parea(self.uami.pr.HECHO)

    def encabezado( self ):

        programa = self.uami.pr.Reservadas["PROGRAMA"]
        identificador  = self.uami.pr.ID
        pc = self.uami.pr.PC

        self.parea( programa )
        self.parea( identificador )
        self.parea( pc )
    
    def estructura( self ):
        comienza = self.uami.pr.Reservadas["COMIENZA"]
        termina = self.uami.pr.Reservadas["TERMINA"]
        self.parea(comienza)
        while self.preanalisis["lexema"]!= termina and self.preanalisis["lexema"]!=self.uami.pr.HECHO:
            self.enunciado()
        self.parea(termina)

       

    def enunciado(self):
        print self.preanalisis["lexema"]
        if(self.preanalisis["lexema"]==self.uami.pr.Reservadas["COMIENZA"]):
            self.estructura
        elif(self.preanalisis["token"]==self.uami.pr.ID):
            self.asignacion()
        elif(self.preanalisis["lexema"]==self.uami.pr.Reservadas["SI"]):
            self.enunc_condicional()
        elif(self.preanalisis["lexema"]==self.uami.pr.Reservadas["MIENTRAS"]):
            self.enunc_mientras()
        elif(self.preanalisis["lexema"]==self.uami.pr.Reservadas["PARA"]):
            self.enunc_para()
        elif(self.preanalisis["lexema"]==self.uami.pr.Reservadas["IMPRIME"]):
            self.enunc_impresion()
        elif(self.preanalisis["lexema"]==self.uami.pr.Reservadas["REPITE"]):
            self.enunc_repite()
        elif(self.preanalisis["lexema"]==self.uami.pr.PC):
            self.parea(self.uami.pr.PC)
      
        
    def enunc_condicional(self):
        pass
    def enunc_mientras(self):
        pass
    def enunc_para(self):
        pass
    def enunc_impresion(self):
        pass
    def enunc_repite(self):
        pass
    

        

    def asignacion( self ):
        self.parea(self.uami.pr.ID)
        self.parea(self.uami.pr.IGUAL)
        self.expresion()
        self.parea(self.uami.pr.PC)

    def expresion(self):
        self.expresion_simple()
        if(self.preanalisis["lexema"]==self.uami.pr.RELOP):
            self.expresion_simple()
        elif(self.preanalisis["lexema"]==self.uami.pr.LOGOP):
            self.expresion_simple()
    
    def expresion_simple(self):
        self.termino()
        while(self.preanalisis["token"]==self.uami.pr.ADDOP):
            self.parea(self.uami.pr.ADDOP)
            self.termino()

    def termino(self):
        self.factor()
        while(self.preanalisis["token"]==self.uami.pr.MULOP):
            self.parea(self.uami.pr.MULOP)
            self.termino()
    
    def factor(self):
        if(self.preanalisis["lexema"]==self.uami.pr.PTSSA):
            self.expresion()
            self.parea(self.uami.pr.PTSSC)
        elif(self.preanalisis["token"]==self.uami.pr.NUM_ENT):
            self.parea(self.uami.pr.NUM_ENT)
        elif(self.preanalisis["token"]==self.uami.pr.ID):
            self.parea(self.uami.pr.ID)
            
        

    
    def parea( self, se_espera ):

        if self.preanalisis["lexema"] == se_espera or self.preanalisis["token"] == se_espera:
            pos = self.uami.alex.alexico()
            if pos != self.uami.pr.HECHO:
                self.preanalisis["lexema"] = self.uami.tabla.getLexema(pos)
                self.preanalisis["token"] = self.uami.tabla.getToken(pos)
            else:
                self.preanalisis["lexema"] = self.uami.pr.HECHO
            return True
        else:
            reportaError = GeneradorError(self.uami)
            reportaError.imprimeErroresSintacticos(se_espera,self.preanalisis["lexema"])            
            return False
