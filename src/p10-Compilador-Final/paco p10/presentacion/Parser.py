from generadorError import GeneradorError
from Generador_Codigo_Intermedio import GeneradorCI
class Parser(object):

    """
    Clase del analisador sintactico
    """
    #Constructor
    def __init__( self, uami ):
        self.uami = uami
        self.reportaError = GeneradorError(self.uami)
        self.etiquetas = 0
        self.GI = GeneradorCI(self.uami)
        
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
        self.parea(self.uami.pr.HECHO)
        self.GI.Emite(self.uami.pr.HALT,self.uami.pr.HECHO)

    def encabezado( self ):
        self.parea(self.uami.pr.Reservadas["PROGRAMA"])
        self.parea(self.uami.pr.ID)
        self.parea(self.uami.pr.PC)
    
    def estructura( self ):
        self.parea(self.uami.pr.Reservadas["COMIENZA"])
        while self.preanalisis["lexema"]!= self.uami.pr.Reservadas["TERMINA"] and self.preanalisis["lexema"]!=self.uami.pr.Reservadas["HASTA"] and self.preanalisis["lexema"]!=self.uami.pr.HECHO:
            self.enunciado()
        self.parea(self.uami.pr.Reservadas["TERMINA"])
    """************************************ ENUNCIADOS***************************************** """"" 


    """*********************************************************************************************************************
    El metodo permite llamar a las variables de nuestra gramatica libre de contexto, segun el token o lexema que 
    puedan identificar
    1.-Estructura
    2.-Asignacion
    3.-Enunciado condicional
    4.-Enunciado mientras
    5.-Enunciado para
    6.-Impresion
    7.-Enunciado repite
    8.-punto y coma
    ************************************************************************************************************************"""       

    def enunciado(self):
        if(self.preanalisis["lexema"]==self.uami.pr.Reservadas["COMIENZA"] or self.preanalisis["lexema"]==self.uami.pr.Reservadas["TERMINA"] ):
            self.estructura()
        elif(self.preanalisis["token"]==self.uami.pr.ID or self.preanalisis["lexema"]==self.uami.pr.IGUAL):
            self.asignacion()
        elif(self.preanalisis["lexema"]==self.uami.pr.Reservadas["SI"] or self.preanalisis["lexema"]==self.uami.pr.Reservadas["ENTONCES"]):
            self.enunc_condicional()
        elif(self.preanalisis["lexema"]==self.uami.pr.Reservadas["MIENTRAS"] or self.preanalisis["lexema"]==self.uami.pr.Reservadas["HAZ"]):
            self.enunc_mientras()
        elif(self.preanalisis["lexema"]==self.uami.pr.Reservadas["PARA"] or self.preanalisis["lexema"]==self.uami.pr.Reservadas["A"] ):
            self.enunc_para()
        elif(self.preanalisis["lexema"]==self.uami.pr.Reservadas["IMPRIME"]) or self.preanalisis["token"]==self.uami.pr.RESTO_MUNDO:
            self.enunc_impresion()
        elif(self.preanalisis["lexema"]==self.uami.pr.Reservadas["REPITE"]or self.preanalisis["lexema"]==self.uami.pr.Reservadas["HASTA"]):
            self.enunc_repite()
        elif(self.preanalisis["lexema"]==self.uami.pr.PC):
            self.parea(self.uami.pr.PC)
        else:
            #si no entra en alguna de las anteriores se hace una impresion de error y se actualiza preanlisis
            #para evitar que se cicle 
            self.reportaError.imprimeErroresSintacticos("enunciado",self.preanalisis["lexema"])
            if self.preanalisis["lexema"] != self.uami.pr.Reservadas["TERMINA"]:
                pos = self.uami.alex.alexico()
                if pos != self.uami.pr.HECHO:
                    self.preanalisis["lexema"] = self.uami.tabla.getLexema(pos)
                    self.preanalisis["token"] = self.uami.tabla.getToken(pos)
                else:
                    self.preanalisis["lexema"] = self.uami.pr.HECHO
                

      
    
    def enunc_condicional(self):
        self.parea(self.uami.pr.Reservadas["SI"])
        self.expresion()
        self.etiquetas +=1
        cond = self.etiquetas
        self.GI.Emite(self.uami.pr.SI_FALSO_VE_A, cond)
        self.parea(self.uami.pr.Reservadas["ENTONCES"])
        self.enunciado()
        self.etiquetas +=1
        salida = self.etiquetas
        self.GI.Emite(self.uami.pr.VE_A,salida)
        if(self.preanalisis["lexema"]==self.uami.pr.Reservadas["OTRO"]):
            self.parea(self.uami.pr.Reservadas["OTRO"])
            self.GI.Emite(self.uami.pr.ETIQUETA,cond)
            self.enunciado()
        self.GI.Emite(self.uami.pr.ETIQUETA,salida)


    def enunc_mientras(self):
        self.parea(self.uami.pr.Reservadas["MIENTRAS"])
        self.etiquetas +=1
        cond = self.etiquetas
        self.GI.Emite(self.uami.pr.ETIQUETA,cond)
        self.expresion()
        self.etiquetas +=1
        salida = self.etiquetas
        self.GI.Emite(self.uami.pr.SI_FALSO_VE_A,salida)
        self.parea(self.uami.pr.Reservadas["HAZ"])
        self.enunciado()
        self.GI.Emite(self.uami.pr.VE_A,cond)
        self.GI.Emite(self.uami.pr.ETIQUETA,salida)
    
    def enunc_impresion(self):
        self.parea(self.uami.pr.Reservadas["IMPRIME"])
        self.parea(self.uami.pr.RESTO_MUNDO)#Parentesis que abre
        self.GI.Emite(self.uami.pr.COPIA,self.preanalisis["lexema"])
        self.parea(self.uami.pr.STRINGS)
        if(self.preanalisis["token"]==self.uami.pr.RESTO_MUNDO):
            
            while (self.preanalisis["token"]!=self.uami.pr.RESTO_MUNDO and self.preanalisis["token"]!=self.uami.pr.HECHO): 
                self.parea(self.uami.pr.RESTO_MUNDO)#Coma
                if(self.preanalisis["token"]==self.uami.pr.STRINGS):
                    self.GI.Emite(self.uami.pr.COPIA,self.preanalisis["lexema"])
                    self.parea(self.uami.pr.STRINGS)
                else:
                    self.expresion()
                    self.GI.Emite(self.uami.pr.ESCRIBE,self.uami.pr.HECHO)
                    
       

        self.parea(self.uami.pr.RESTO_MUNDO)#Parentesis que cierra
        self.parea(self.uami.pr.RESTO_MUNDO)#PUNTO Y COMA



    def enunc_para(self):
        self.parea(self.uami.pr.Reservadas["PARA"])
        c = self.preanalisis["lexema"]
        self.GI.Emite(self.uami.pr.VALOR_I,c)
        self.parea(self.uami.pr.ID)
        self.parea(self.uami.pr.IGUAL)
        self.expresion()
        self.GI.Emite(self.uami.pr.ASING,self.uami.pr.HECHO)
        self.parea(self.uami.pr.Reservadas["A"])
        self.etiquetas +=1
        entrada = self.etiquetas
        self.GI.Emite(self.uami.pr.ETIQUETA,entrada)
        self.GI.Emite(self.uami.pr.VALOR_D,c)
        self.expresion()
        self.GI.Emite(self.uami.pr.RELOP,"<=")
        self.etiquetas +=1
        salida = self.etiquetas
        self.GI.Emite(self.uami.pr.SI_FALSO_VE_A,salida)
        self.parea(self.uami.pr.Reservadas["HAZ"])
        self.enunciado()
        self.GI.Emite(self.uami.pr.VALOR_I,c)
        self.GI.Emite(self.uami.pr.VALOR_D,c)
        self.GI.Emite(self.uami.pr.PUSH,1)
        self.GI.Emite(self.uami.pr.ADDOP,"+")
        self.GI.Emite(self.uami.pr.ASING,self.uami.pr.HECHO)
        self.GI.Emite(self.uami.pr.VE_A,entrada)
        self.GI.Emite(self.uami.pr.ETIQUETA,salida)

   
    def enunc_repite(self):
        self.parea(self.uami.pr.Reservadas["REPITE"])
        self.etiquetas +=1
        ciclo = self.etiquetas
        self.GI.Emite(self.uami.pr.ETIQUETA,ciclo)        
        #while self.preanalisis["lexema"] != self.uami.pr.Reservadas["HASTA"] and self.preanalisis["lexema"] != self.uami.pr.Reservadas["TERMINA"] and self.preanalisis["lexema"] != self.uami.pr.HECHO:
        self.enunciado()
        self.parea(self.uami.pr.Reservadas["HASTA"])
        self.expresion()
        self.GI.Emite(self.uami.pr.SI_FALSO_VE_A,ciclo)
        self.parea(self.uami.pr.PC)
    

    """*************************************************** otros :V*******************************"""      

    def asignacion( self ):
        self.GI.Emite(self.uami.pr.VALOR_I,self.preanalisis["lexema"])
        self.parea(self.uami.pr.ID)
        self.parea(self.uami.pr.IGUAL)
        self.expresion()
        self.GI.Emite(self.uami.pr.ASING,self.uami.pr.HECHO)
        self.parea(self.uami.pr.PC)

    def expresion(self):
        self.expresion_simple()
        aux = self.preanalisis["lexema"]
        if(self.preanalisis["token"]==self.uami.pr.RELOP):                      
            self.parea(self.uami.pr.RELOP)
            self.expresion_simple()
            self.GI.Emite(self.uami.pr.RELOP,aux)
        elif(self.preanalisis["token"]==self.uami.pr.LOGOP):
            print "Entre a logop ese men"
            self.parea(self.uami.pr.LOGOP)
            self.expresion_simple()
            self.GI.Emite(self.uami.pr.LOGOP,aux)
    
    def expresion_simple(self):
        self.termino()        
        #while(self.preanalisis["token"]==self.uami.pr.ADDOP):
        print "while espresion simple",self.preanalisis["lexema"], self.preanalisis["token"]
        if(self.preanalisis["token"]==self.uami.pr.ADDOP):
            aux = self.preanalisis["lexema"]             
            self.parea(self.uami.pr.ADDOP)
            self.termino()
            self.GI.Emite(self.uami.pr.ADDOP,aux)

    def termino(self):
        self.factor()
        #while(self.preanalisis["token"]==self.uami.pr.MULOP):
        if(self.preanalisis["token"]==self.uami.pr.MULOP):
            aux = self.preanalisis["lexema"] 
            self.parea(self.uami.pr.MULOP)
            self.termino()
            self.GI.Emite(self.uami.pr.MULOP,aux)
    
    def factor(self):
        if(self.preanalisis["token"]==self.uami.pr.RESTO_MUNDO):
            self.parea(self.uami.pr.RESTO_MUNDO)
            self.expresion()
            self.parea(self.uami.pr.RESTO_MUNDO)
        elif(self.preanalisis["token"]==self.uami.pr.NUM_ENT):
            self.GI.Emite(self.uami.pr.PUSH,self.preanalisis["lexema"])
            self.parea(self.uami.pr.NUM_ENT)
        elif(self.preanalisis["token"]==self.uami.pr.ID):
            self.GI.Emite(self.uami.pr.VALOR_D,self.preanalisis["lexema"])
            self.parea(self.uami.pr.ID)
        else:
            self.reportaError.imprimeErroresSintacticos("una expresion", self.preanalisis["lexema"])         
        

    
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
            self.reportaError.imprimeErroresSintacticos("una expresion",self.preanalisis["lexema"])
            # if self.preanalisis["lexema"] != self.uami.pr.Reservadas["TERMINA"]:
            #     pos = self.uami.alex.alexico()
            #     if pos != self.uami.pr.HECHO:
            #         self.preanalisis["lexema"] = self.uami.tabla.getLexema(pos)
            #         self.preanalisis["token"] = self.uami.tabla.getToken(pos)
            #     else:
            #         self.preanalisis["lexema"] = self.uami.pr.HECHO         
            
