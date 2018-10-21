class Archivo(object):

    def crearArchivo( self, url ):
        # Modo "w+" con la ubicacion del puntero Al INICIO
        # Escritura y lectura. 
        # Sobreescribe el archivo si existe. Crea el archivo si no existe
        archivo = open( url, "w+")
        self.agregarTexto( url )

    ##
    # agrega texto al archivo
    ##
    def agregarTexto( self, url ):

        # Modo "a+" agregado con lectura y escritura 
        # con la ubicacion del puntero: 
        # Si el archivo existe, al final de este. 
        # Si el archivo no existe, al comienzo
        archivo = open( url, "a+")

        archivo.write("\nNueva linea")

        Nuevo_final_de_archivo = archivo.tell()
        archivo.seek( Nuevo_final_de_archivo )

        self.leerArchivo( url )

    ##
    # agrega Lineas de texto al archivo
    ##
    def agregarTextoPorLineas( self, url):
        
        archivo = open( url, "a+")

        lineas = [
                  "linea\n",
                  "linea\n",
                  "linea\n"
                ]

        archivo.writelines( lineas )

        Nuevo_final_de_archivo = archivo.tell()
        archivo.seek( Nuevo_final_de_archivo )

        self.leerArchivo( url )

    ##
    # Lee contenido de forma completa
    ##
    def leerArchivo( self, url ):
        archivo = open( url, "r")
        contenido = archivo.read()
        indice = archivo.tell()
        print contenido, "\n El indice ya recorrido es:", indice

    ##
    # Lee contenido haciendo pruebas
    ##
    def propiedadesLeer( self, url ):

        # El modo "r" --> Solo Lectura de contenido
        # Ubicacion del puntero del archivo: Al INICIO
        archivo = open( url, "r")

        # "tell() --> regresa la posicion del puntero"
        puntero = archivo.tell()
        print "puntero al momento de abrir archivo: ", puntero, "\n"

        # Se lee el archivo por cachos, el puntero se mueve conforme avanza
        contenido = archivo.read(1)
        print "Parcialidad de contenido"
        print contenido

        print

        contenido = archivo.read(2)
        print "Parcialidad de contenido"
        print contenido

        print

        # Se mueve el puntero a la posicion dada
        archivo.seek(0)
        puntero = archivo.tell()
        print "La posicion del puntero reseteada: ", puntero
        contenido = archivo.read()
        print "Contenido Completo"
        indice = archivo.tell()
        print contenido, "\n El indice ya recorrido es:", indice

        print

        print "Validacion de Archivo vacio"
        archivo = open( "vacio.txt", "r")
        contenido = archivo.read()

        if archivo.tell() > 0:
            print contenido
        else:
            print "Resultado = Texto vacio"
        
        self.cerrarArchivo( "vacio.txt" )

    ##
    # Metodo para cerrar el archivo
    ##
    def cerrarArchivo( self, url):
        archivo = open( url, "r") 
        contenido = archivo.read()
    
        archivo.close()


    ##
    # Metodo principal del Programa
    ##
    def main( self ):

        print "\n*** ARCHIVO DE TEXTO CON LEIDA COMPLETA ***\n"
        self.leerArchivo( "LeerDocumentoCompleto.txt" )
        self.cerrarArchivo( "LeerDocumentoCompleto.txt" )
        
        print "\n*** ARCHIVO DE TEXTO CON LEIDA DE PRUEBAS ***\n"
        self.propiedadesLeer( "LeerPruebas.fte" )
        self.cerrarArchivo( "LeerPruebas.fte" )

        print "\n*** AGREGAR TEXTO a \"agregarTextoLineas.fte\" ***"
        self.agregarTextoPorLineas( "agregarTexto_Lineas.fte" )
        self.cerrarArchivo( "agregarTexto_Lineas.fte" )

        print "\n*** AGREGAR TEXTO a \"agregarTexto.fte\" ***"
        self.agregarTexto( "agregarTexto.fte" )
        self.cerrarArchivo( "agregarTexto.fte" )

        print "\n*** CREAR ARCHIVO DE TEXTO  \"TextoCreado.txt\" ***"
        self.crearArchivo( "TextoCreado.txt" )
        self.cerrarArchivo( "TextoCreado.txt" )
        
obj = Archivo()
obj.main()