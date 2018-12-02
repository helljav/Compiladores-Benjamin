class Generador_de_Errores(object):

    def __init__(self, uami):
        self.uami = uami
    
    def errorLexicografico( self, respuesta ):

        self.uami.errores += 1
        texto = [
                    "Linea: ",
                    str(self.uami.lineas),
                    "\n\t",
                    respuesta["token"],
                    "\n\t",
                    respuesta["lexema"],
                    "\n\n"
                ]

        self.uami.escribirArchivo( self.uami.urlErr, "a+", texto )
        cadRes = self.uami.ventana.getTextAreaResultado()
        cadRes += "<< Error Lexicografico Encontrado >>\n"
        self.uami.ventana.escribirAreaResultado( cadRes )

    def errorSintactico( self, se_espera, preanalisis ):
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
                        preanalisis["lexema"],
                        "\n\n"
                ]

        self.uami.escribirArchivo( self.uami.urlErr, "a+", texto )
        cadRes = self.uami.ventana.getTextAreaResultado()
        cadRes += "<< Error Sintactico Encontrado >>\n"
        self.uami.ventana.escribirAreaResultado( cadRes )