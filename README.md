# Compilador Uami
Este es un compilador que se desarrollo por alumnos de la carrera de computacion en la universidad autonoma metropolitana durante el curso de compiladores impartido por el Dr. Benjamin Moreno Montiel para fines de aprendizaje acerca de el procedimiento de compilacion que hacen los lenguajes de programacion 

## Practicas del curso
   1. Contador de palabras
   2. Automata Finito Determinista
   3. Automata Finito No Determinista 
   4. Analizador Lexicografico v1
   5. Analizador Lexicografico v2
   6. Analizador Lexicografico Final
   7. Analizador Sintactico

### Demos

##### *1.- Contador de palabras*
![contador de palabras](https://image.ibb.co/bP8huK/practica_1.jpg)

##### *2.- Automata Finito Determinista*
![contador de palabras](https://image.ibb.co/mtB91z/practica_2.jpg)

##### *3.- Automata Finito No Determinista*

Automata AFND y AFND-e con sus posibles caminos, los validos e invalidos
El AFND reconoce todas las combinaciones de 1 y 0 que forzosamente terminen con "01"

El AFND-e reconoce las cadenas que contengas numero impar de 0 y las cadenas donde las cadenas no puedan tener como multiplo de 3 a el numero 1

![contador de palabras](https://image.ibb.co/fWcGFf/afnd-e.jpg)

##### *4.- Analizador Lexicografico v1*
![contador de palabras](https://image.ibb.co/duYuJA/1.jpg)

##### *6.- Analizador Lexicografico Final*
![contador de palabras](https://image.ibb.co/ji6GCf/lexicografico.jpg)

##### *7.- Analizador Sintactico*

##### Informacion de compilador Uami

**PALABRAS RESERVADAS** usadas en el compilador uami 

Num | Palabra Reservada |
---|:---:|
1| programa |
2| si |
3| entonces |
4| otro |
5| haz |
6| mientras |
7| comienza |
8| termina |
9| imprime |
10| repite |
11| hasta |
12| para |
13| a |
        
**TOKENS LEXICOGRAFICOS** usadas en el compilador uami 

Num | TOKENS | DESCRIPCION 
---|:---:|:----:
1| HECHO | FIN DE ARCHIVO
2| COMENTARIO | COMENTARIO
3| P_RES | PALABRA RESERVADA
4| STRINGS | CADENA DE CARACTERES
5| RELOP | OPERADOR RELACIONAL
6| LOGOP | OPERADOR LOGICO
7| SUMA | OPERADOR DE SUMA
8| RESTA | OPERADOR DE RESTA
9| MULTIPLICACION | OPERADOR DE MULTIPLICACION
10| DIVISION | OPERADOR DE DIVISION
11| MODULO | OPERADOR DE MODULO
12| ASIGNACION | ASIGNACION
13| ERROR_SINTACTICO | ERROR_SINTACTICO
14| TOKEN_INV | TOKEN INVALIDO
15| RESTO_MUNDO | RESTO DEL MUNDO
16| ERROR | ERROR LEXICOGRAFICO
17| ID | IDENTIFICADOR
18| NUM_ENT | ENTERO
19| DELIMITADOR | DELIMITADORES

**OPERADORES ARITMETICOS** usadas en el compilador uami 

Num | TOKEN | SIMBOLO  
---|:---:|:----:
1| SUMA | `+`
2| RESTA | `-`
3| MULTIPLICACION | `*` 
4| DIVISION | `/`
5| MODULO | `%`
6| ASIGNACION | `=`

**OPERADORES LOGICOS** usadas en el compilador uami 

Num | TOKEN | SIMBOLO | DESCRIPCION
---|:---:|:----:| :----:
1| LOGOP | `!` | NEGACION
2| LOGOP | `&&` | AND
3| LOGOP | `||` | OR

**OPERADORES RELACIONALES** usadas en el compilador uami 

Num | TOKEN | SIMBOLO | DESCRIPCION
---|:---:|:----:| :----:
1| RELOP | `!=` | DISTINTO
2| RELOP | `==` | IGUAL
3| RELOP | `<` | MENOR
4| RELOP | `<=` | MENOR IGUAL
5| RELOP | `>` | MAYOR
6| RELOP | `>=` | MAYOR IGUAL

**DELIMITADORES** usadas en el compilador uami 

Num | TOKEN | SIMBOLO | DESCRIPCION
---|:---:|:----:| :----:
1| DELIMITADOR	 | `\n` | SALTO DE LINEA
2| DELIMITADOR	 | `\t` | TABULADOR

**RESTO DEL MUNDO** usadas en el compilador uami 

Num | TOKEN | SIMBOLO | DESCRIPCION
---|:---:|:----:| :----:
1| RESTO_MUNDO	 | `;` | PUNTO Y COMA
2| RESTO_MUNDO	 | `,` | COMA
3| RESTO_MUNDO	 | `(` | PARENTESIS QUE ABIERTO
4| RESTO_MUNDO	 | `)` | PARENTESIS QUE CIERRA

**CADENAS, IDENTIFICADORES Y COMENTARIOS** usadas en el compilador uami 

TIPO | TOKEN | FORMA | EJEMPLO
---|:---:|:----:| :----:
CADENAS         | STRINGS	 | CUALQUIER CARACTER ENTRE COMILLAS | "cadena"
IDENTIFICADORES | ID	     | EMPIEZA CON ALGUNA LETRA Ó GUION BAJO, DESPUES ADMITE LETRA, GUION BAJO Y NUMERO   | _identificador123
COMENTARIOS     | COMENTARIO | CUALQUIER CARACTER ENTRE LLAVES   | { comentario }