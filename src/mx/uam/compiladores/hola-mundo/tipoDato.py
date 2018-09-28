cCadena = 0
cEntero = 0
cChar = 0
cFloat = 0
cBoolean = 0

def main():

    Lista = ["h", "o", "l", "a", "hola", 13, 13.3, True, False]

    for termino in Lista:
        tipoVariable(termino, )

    global cCadena
    global cEntero
    global cChar
    global cFloat
    global cBoolean

    print
    print "numero de cadenas: ", cCadena
    print "numero de enteros: ", cEntero
    print "numero de char: ", cChar
    print "numero de float: ", cFloat
    print "numero de boolean: ", cBoolean


def tipoVariable(termino, ):

    if type(termino) == str:
        if len(termino) == 1:
            print termino, "es un caracter"
            global cChar
            cChar = cChar + 1
        else:
            print termino, " es una cadena"
            global cCadena
            cCadena = cCadena + 1
    else:
        if type(termino) == int:
            print termino, " es un entero"
            global cEntero
            cEntero = cEntero + 1
        else:
            if type(termino) == float:
                print termino, " es un float"
                global cFloat
                cFloat = cFloat + 1
            else:
                print termino, "es un Boolean"
                global cBoolean
                cBoolean = cBoolean + 1


main()
