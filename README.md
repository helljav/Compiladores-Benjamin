# Compiladores-Benjamin
Practicas de la materia de Compiladores

## Demo

### Practica 1

Contador de Palabras reservadas

<img src="https://image.ibb.co/bP8huK/practica_1.jpg" alt="practica_1" border="0">

### Practica 2

AFD (Automata Finito Determinista)

<img src="https://image.ibb.co/mtB91z/practica_2.jpg" alt="practica_2" border="0">

### Practica 3

Automata AFND y AFND-e con sus posibles caminos, los validos e invalidos

El AFND reconoce todas las combinaciones de 1 y 0 que forzosamente terminen con "01"

El AFND-e reconoce las cadenas que contengas numero impar de 0 y las cadenas donde las cadenas no puedan tener como multiplo de 3 a el numero 1

<img src="https://image.ibb.co/fWcGFf/afnd-e.jpg" alt="afnd-e" border="0">

### Practica 4

Analizador Lexicografico

<img src="https://image.ibb.co/duYuJA/1.jpg" alt="1" border="0">

### Practica 5 y 6

Analizador Lexicografico completo

<img src="https://image.ibb.co/ji6GCf/lexicografico.jpg" alt="lexicografico" border="0">


---- Palabras Reservadas ----

        PROGRAMA = "programa"
        
        SI = "si"
        
        ENTONCES = "entonces"
        
        OTRO = "otro"
        
        HAZ = "haz"
        
        MIENTRAS = "mientras"
        
        COMIENZA = "comienza"
        
        TERMINA = "termina"
        
        IMPRIME = "imprime"
        
        REPITE = "repite"
        
        HASTA = "hasta"
        
        PARA = "para"
        
        A = "a"
        

---- Tokens lexicograficos ----

        HECHO = "FIN DE ARCHIVO"
        
        EOS = "EOS"
        
        COMENTARIO = "COMENTARIO"
        
        P_RES = "PALABRA RESERVADA"
        
        CADENA = "CADENA"
        
        RELOP = "OPERADOR RELACIONAL"
        
        LOGOP = "OPERADOR LOGICO"
        
        ADDOP = "OPERADOR DE SUMA O RESTA"
        
        MULOP = "OPERADOR DE MULTIPLICACION"
        
        STRINGS = "OPERADOR DE MULTIPLICACION"
        
        ERROR = "ERROR LEXICOGRAFICO"
        
        TOKEN_INV = "TOKEN INVALIDO"
        
        RESTO_MUNDO = "RESTO DEL MUNDO"
        
        ASIGNACION = "ASIGNACION"
        
        ID = "IDENTIFICADOR"
        
        NUM_ENT = "ENTERO"
        

---- COMENTARIOS ----

{ entre llaves }

---- LEXEMAS PARA OPERADORES LOGICOS, ARITMETICOS Y RELACIONALES ----

        LT = "<"
        
        LE = "<="
        
        EQ = "=="
        
        ASG = "="
        
        GE = ">="
        
        NE = "!="
        
        NOT = "!"
        
        MAS = "+"
        
        MENOS = "-"
        
        OR = "||"
        
        MULT = "*"
        
        DIV = "/"
        
        MODULO = "%"
        
        AND = "&&"
        
