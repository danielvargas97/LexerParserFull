import lexer_rules
import parser_rules
import os

from ply.lex import lex
from ply.yacc import yacc


"""
Escogemos archivo de entrada
"""
ruta = os.path.dirname(os.path.realpath(__file__))
print("Ruta Actual: "+ruta)
archivos = os.listdir(ruta)

k = 0
print("Archivos actuales en la carpeta: "+ruta)
for x in archivos:
    print(str(k) + " : " + x)
    k = k + 1


archivoSelec = int(input("Escriba el numero para seleccionar la entrada: "))
rutaEntrada = os.path.join(ruta,archivos[archivoSelec])
archIn = open(rutaEntrada,'r')
entrada = archIn.readlines()
salida = []


lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules)

for elem in entrada:
    expression = parser.parse(elem,lexer)
    salida.append(expression)
    print(expression)

rutaSalida = os.path.join(ruta,"salidas.out")
archOut = open(rutaSalida,'w')
for result in salida:
    archOut.write(str(result)+"\n")    
archOut.close()

    
