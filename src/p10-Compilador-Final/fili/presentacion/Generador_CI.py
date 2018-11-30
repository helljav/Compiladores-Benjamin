class Generador_CI(object):
    
    def __init__(self, uami ):
        self.uami = uami

    def emite(self, valor_Token, lexema):

        urlCI = self.uami.urlCI

        halt = self.uami.pr.HALT
        lvalue = self.uami.pr.VALOR_I
        rvalue = self.uami.pr.VALOR_D
        push = self.uami.pr.PUSH
        amarre = self.uami.pr.ASIGN
        gofalse = self.uami.pr.SI_FALSO_VE_A
        goto = self.uami.pr.VE_A
        label = self.uami.pr.ETIQUETA 
        mas = self.uami.pr.MAS
        menos = self.uami.pr.MENOS
        mult = self.uami.pr.MULT
        div = self.uami.pr.DIV
        relop = self.uami.pr.RELOP
        logop = self.uami.pr.LOGOP
        
        if valor_Token is halt:
            texto = halt + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )
        
        elif valor_Token is lvalue:
            texto = lvalue + " " + lexema + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )
        
        elif valor_Token is rvalue:
            texto = rvalue + " " + lexema + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )

        elif valor_Token is push:
            texto = push + " " + lexema + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )

        elif valor_Token is amarre:
            texto = amarre + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )
        
        elif valor_Token is gofalse:
            texto = gofalse + " " + lexema + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )
        
        elif valor_Token is goto:
            texto = goto + " " + lexema + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )
        
        elif valor_Token is label:
            texto = label + " " + lexema + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )
        
        elif valor_Token is mas:
            texto = mas + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )

        elif valor_Token is menos:
            texto = menos + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )
        
        elif valor_Token is mult:
            texto = mult + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )

        elif valor_Token is div:
            print div
            texto = div + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )

        elif valor_Token is relop:
            texto = lexema + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )

        elif valor_Token is logop:
            texto = lexema + "\n"
            self.uami.escribirArchivo( urlCI, "a+", texto )
            contenidoArchivo = self.uami.getArchivoTexto( urlCI )
            self.uami.ventana.escribirAreaCI( contenidoArchivo )