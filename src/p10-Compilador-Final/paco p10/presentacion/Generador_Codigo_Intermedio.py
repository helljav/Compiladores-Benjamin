class GeneradorCI(object):
    def __init__(self, uami):
        self.uamito = uami       
    
    
    def Emite(self,valor_token,lexema):
        if(valor_token== self.uamito.pr.VALOR_I):
            texto = "lvalue " + str(lexema) +"\n"
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", texto )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )

        elif(valor_token== self.uamito.pr.VALOR_D):
            texto = "rvalue "+ str(lexema) +"\n"
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", texto )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )

        elif(valor_token== self.uamito.pr.PUSH):
            texto ="push "+ str(lexema) +"\n"
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", texto )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )

        elif(valor_token== self.uamito.pr.ETIQUETA):
            texto = "label "+ str(lexema) +"\n"
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", texto )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )

        elif(valor_token== self.uamito.pr.HALT):
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", "halt\n" )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )

        elif(valor_token== self.uamito.pr.ASING):
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", ":=\n" )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )

        elif(valor_token== self.uamito.pr.VE_A):
            texto = "goto "+ str(lexema) +"\n"
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", texto )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )

        elif(valor_token== self.uamito.pr.SI_FALSO_VE_A):
            texto = "gofalse "+ str(lexema) +"\n"
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", texto )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )

        elif(valor_token== self.uamito.pr.ESCRIBE):
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", "write\n" )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )

        elif(valor_token== self.uamito.pr.COPIA):
            texto = "print "+ str(lexema) +"\n"
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", texto )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )

        elif(valor_token== self.uamito.pr.LOGOP):
            texto = lexema + "\n"
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", texto )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )

        elif(valor_token== self.uamito.pr.RELOP):
            texto = lexema + "\n"    
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", texto )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )

        elif(valor_token== self.uamito.pr.ADDOP):
            texto =  lexema + "\n"    
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", texto )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )

        elif(valor_token== self.uamito.pr.MULOP):
            texto = lexema + "\n"    
            self.uamito.escribirArchivo( self.uamito.urlObj, "a+", texto )
            self.uamito.ventana.escribirAreaObjeto( self.uamito.getArchivoTexto(self.uamito.urlObj) )