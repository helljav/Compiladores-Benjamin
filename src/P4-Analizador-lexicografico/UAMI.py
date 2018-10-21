from ALEX import Alex
class Uami(object):

    def __init__( self ):
        
        # un variable tipo fopen para abrir el archivo 
        self.f_tpl = ""
        # Cadena para crear el archivo Error (*.err)
        self.err = ""
        # Cadena para crear el archivo tupla (*.tpl)
        self.lineas = 0

    def crearArchivos( self, URL, contenido_GUI ):

        # Eliminar nombre de archivo abierto y guararlo en lista
        lista = str(URL).split("/")
        lista = lista[0:len(lista)-1]
        
        # Generar la url a nivel de la carpeta origen del archivo abierto
        URL = '/'.join(str(e) for e in lista) + "/"
        print URL
        
        # Creacion de los Archivos
        self.f_tpl = open( URL + "/tupla.tpl", "w+")
        self.err = open( URL + "/error.err", "w+")

        # Agregar contenido a los archivos
        self.f_tpl.write("tupla")
        self.err.write("errores")
    
    def cierraArchivo( self ):
        self.f_tpl.close()
        self.err.close()
    
    def iniciaCompilacion( self, URL, contenido_GUI ):
        alex = Alex(contenido_GUI)
        # self.crearArchivos( URL, contenido_GUI )
        # self.cierraArchivo()