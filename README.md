# Compilador Uami
Este es un compilador que se desarrollo por alumnos de la carrera de computacion en la universidad autonoma metropolitana durante el curso de compiladores impartido por el Dr. Benjamin Moreno Montiel para fines de aprendizaje acerca de el procedimiento de compilacion que hacen los lenguajes de programacion 

## Practicas del curso

El compilador uami desarrollado en el curso cuenta de las siguientes practicas

   1. Contador de palabras
   2. Automata Finito Determinista
   3. Automata Finito No Determinista 
   4. Analizador Lexicografico v1
   5. Analizador Lexicografico v2
   6. Analizador Lexicografico Final
   7. Analizador Sintactico v1
   8. Analizador Sintactico Final
   9. Codigo Intermedio y Generador de errores

### Demos

##### *1.- Contador de palabras*
![contador de palabras](https://image.ibb.co/bP8huK/practica_1.jpg)

##### *2.- Automata Finito Determinista*
![automata finito determinista](https://image.ibb.co/mtB91z/practica_2.jpg)

##### *3.- Automata Finito No Determinista*

Automata AFND y AFND-e con sus posibles caminos, los validos e invalidos
El AFND reconoce todas las combinaciones de 1 y 0 que forzosamente terminen con "01"

El AFND-e reconoce las cadenas que contengas numero impar de 0 y las cadenas donde las cadenas no puedan tener como multiplo de 3 a el numero 1

![automata finito no determinista](https://image.ibb.co/fWcGFf/afnd-e.jpg)

##### *4.- Analizador Lexicografico v1*
![analizador lexicografico](https://image.ibb.co/duYuJA/1.jpg)

##### *6.- Analizador Lexicografico Final*
![analizador lexicografico](https://image.ibb.co/ji6GCf/lexicografico.jpg)

##### *7.- Analizador Sintactico V1*
![analizador sintactico](https://i.ibb.co/FH8gHch/Analizador-lexicografico-final.jpg)

##### *8.- Analizador Sintactico Final*
![analizador sintactico](https://i.ibb.co/G5PQbWx/Analizador-lexicografico.jpg)

##### *9.- Generador de errores y Generador de codigo intermedio*
![compiladores uam benjamin](https://i.ibb.co/RPcPDKg/Compiladores-uam-benjamin.jpg)

##### Informacion de compilador Uami

**PALABRAS RESERVADAS** 

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
        
**TOKENS LEXICOGRAFICOS** 

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

**TOKENS CODIGO INTERMEDIO**

NUM| TOKEN | DESCRIPCION
----|:----:|:----:
1  | VALOR_I        |   "lvalue", cargar valor
2  | VALOR_D        |   "rvalue", leer valor
3  | PUSH           |   "push", agregar
4  | ASIGN          |   ":=", asignar valor
5  | ETIQUETA       |   "label", etiqueta
6  | VE_A           |   "goto", ve a
7  | SI_FALSO_VE_A  |   "gofalse", si es falso ve a
8  | ESCRIBE        |   "write", escribe
9  | IMPRIME        |   "print", imprime
10 | HALT           |   "halt", fin de archivo

**OPERADORES ARITMETICOS** 

Num | TOKEN | SIMBOLO  
---|:---:|:----:
1| SUMA | `+`
2| RESTA | `-`
3| MULTIPLICACION | `*` 
4| DIVISION | `/`
5| MODULO | `%`
6| ASIGNACION | `=`

**OPERADORES LOGICOS** 

Num | TOKEN | SIMBOLO | DESCRIPCION
---|:---:|:----:| :----:
1| LOGOP | `!` | NEGACION
2| LOGOP | `&&` | AND
3| LOGOP | `||` | OR

**OPERADORES RELACIONALES** 

Num | TOKEN | SIMBOLO | DESCRIPCION
---|:---:|:----:| :----:
1| RELOP | `!=` | DISTINTO
2| RELOP | `==` | IGUAL
3| RELOP | `<` | MENOR
4| RELOP | `<=` | MENOR IGUAL
5| RELOP | `>` | MAYOR
6| RELOP | `>=` | MAYOR IGUAL

**DELIMITADORES** 

Num | TOKEN | SIMBOLO | DESCRIPCION
---|:---:|:----:| :----:
1| DELIMITADOR	 | `\n` | SALTO DE LINEA
2| DELIMITADOR	 | `\t` | TABULADOR
3| DELIMITADOR	 | ` ` | ESPACIO

**RESTO DEL MUNDO** 

Num | TOKEN | SIMBOLO | DESCRIPCION
---|:---:|:----:| :----:
1| RESTO_MUNDO	 | `;` | PUNTO Y COMA
2| RESTO_MUNDO	 | `,` | COMA
3| RESTO_MUNDO	 | `(` | PARENTESIS QUE ABIERTO
4| RESTO_MUNDO	 | `)` | PARENTESIS QUE CIERRA

**FORMA DE CADENAS, IDENTIFICADORES Y COMENTARIOS**

TIPO | TOKEN | FORMA | EJEMPLO
---|:---:|:----:| :----:
CADENAS         | STRINGS	 | CUALQUIER CARACTER ENTRE COMILLAS | "cadena"
IDENTIFICADORES | ID	     | EMPIEZA CON ALGUNA LETRA Ó GUION BAJO, DESPUES ADMITE LETRA, GUION BAJO Y NUMERO   | _identificador123
COMENTARIOS     | COMENTARIO | CUALQUIER CARACTER ENTRE LLAVES   | { comentario }

**ENUNCIADOS ACEPTADOS**

ENUNCIADO | FORMA | DESCRIPCION
:---:|:---:|:----:
ENCABEZADO      | `programa identificador;`    | Encabezado del programa
ESTRUCTURA      | `comienza enunciado termina` | Determina bloques de codigo, acepta de 1 o n enunciados
ASIGNACION      | `identificador = expresion;` | Funciona igual a una asignacion
IMPRIME         | `imprime("cadena",expresion);` | Debe empezar con una cadena y acepta 0 o n expresiones
CONDICIONAL     | `si expresion entonces enunciado otro enunciado` | Funciona igual que un if-else, con el valor otro opcional 
PARA            | `para Identificador = expresion a expresion haz enunciado` | Funcion igual a un ciclo for
MIENTRAS        | `mientras expresion haz enunciado` | Funcion igual a un while
REPITE          | `repite enunciado hasta expresion;`| Funcion igual a un Do While

**CODIGO EJEMPLO**

```
programa prueba;
    { Estructura }
    comienza
        { asignacion }
        a1 = 23 * 21;

        { Condicional }
        si variable + 1 == 2 entonces
            a1 = 23 * 21;
        otro
            a1 = 23 + 21;

        { Mientras }
        mientras 12 < 20 haz
            a1 = 23 + 21;

        { Para }
        para i=0 a i==12 haz
            a1 = 23 + 21;

        { Repite }
        repite a1 = 23 + 21;
        hasta i <= 2;

        { Impresion }
        imprime("num1 = %d, y num2 = %d", hola, 1 );

    termina
```