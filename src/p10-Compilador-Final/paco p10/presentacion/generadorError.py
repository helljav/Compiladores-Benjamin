class GeneradorError(object):

    def __init__(self, uami):
        self.uamito = uami

    def imprimeErroresSintacticos(self,se_espera,preanalisis):
        self.uamito.errores += 1
        texto = [
                        "Linea: ",
                        str(self.uamito.lineas),
                        "\t",
                        self.uamito.pr.ERROR_SINTACTICO,
                        "\n\t",
                        "Se esperaba: ",
                        se_espera,
                        "\n\t",
                        "antes de: ",
                        preanalisis,
                        "\n\n"
                ]    
        self.uamito.escribirArchivo( self.uamito.urlErr, "a+", texto )
        
        cadRes = self.uamito.ventana.getTextAreaResultado()
        cadRes += "<< Error Sintactico Encontrado >>\n"
        
        self.uamito.ventana.escribirAreaResultado( cadRes )


    def erroresLex( self, respuesta ):

        self.uamito.errores += 1
        texto = [
                    "Linea: ",
                    str(self.uamito.lineas),
                    "\n\t",
                    respuesta["token"],
                    "\n\t",
                    respuesta["lexema"],
                    "\n\n"
                ]

        self.uamito.escribirArchivo( self.uamito.urlErr, "a+", texto )
        cadRes = self.uamito.ventana.getTextAreaResultado()
        cadRes += "<< Error Lexicografico Encontrado >>\n"
        self.uamito.ventana.escribirAreaResultado( cadRes )
