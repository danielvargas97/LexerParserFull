# Ejercicio Parser V2 + Entrada y salida por Archivo.
Segunda versión del LexerParser. Se usa la notación posfija para ello y se implementa la lectura y escritura por archivo.

## Enunciado:
Teniendo como base un programa que posee un lexer y un parser que realiza operaciones aritméticas en notación infija, escribir un equivalente en notación posfija.

## Solución:
Se modifica el lexer para soportar una gramática posfija. Por ejemplo [suma] := [expresion1] + [expresion2] pasa a notación posfija a ser [suma] := [expresion1] [expresion2] +.

## Ejemplo:
### Entrada:
10 5 * 12 /

### Salida:
4


## Integrantes:
* Jhonathan Daniel Rojas Zora - 20151020041
* David Santiago Garces Benitez - 20151020032
* Daniel Alfonso Vargas Ortiz - 20152020009
