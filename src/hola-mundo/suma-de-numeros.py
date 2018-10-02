def main():

    while True:
        try:
            a = int(input("variable a: "))
            b = int(input("variable b: "))
            break
        except:
            print("Los valores de las variables deben ser enteros")
    
    c = suma( a, b)

    print "resultado: ", c

def suma( ope1, ope2 ):

    resultado =ope1 + ope2
    return resultado

main()
            