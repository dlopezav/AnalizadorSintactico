reglas = open ('misArchivos/grammar.txt','r')
# reglas = open ('gramaticaprueba.txt','r')
NOTERMINALES = []
for regla in reglas:
    regla = regla.replace('\n','')
    regla = regla.split(" ")
    if(regla[0] not in NOTERMINALES):
        NOTERMINALES.append(regla[0])


primeros = open ('misArchivos/ResultPrimeros.txt','r')
# primeros = open ('ResultBPrimeros.txt','r')
PRIMEROS = {}
for linea in primeros:
    regla = linea.split(" ")
    no_terminal = regla[0]
    linea = linea.replace(" ","")
    split = linea[len(no_terminal)+2:-2].replace("'", "").split(',')
    PRIMEROS[no_terminal] = split



siguientes = open ('misArchivos/ResultSegundos.txt','r')
# siguientes = open ('ResultBSegundos.txt','r')
SIGUIENTES = {}
for linea in siguientes:
    regla = linea.split(" ")
    no_terminal = regla[0]
    linea = linea.replace(" ","")
    split = linea[len(no_terminal)+2:-2].replace("'", "").split(',')
    SIGUIENTES[no_terminal] = split



prediccion = open ('prediccion.txt','r')
PREDICCIONES = {}
for linea in prediccion:
    linea = linea.split("[")
    regla = linea[0][:-1]
    linea[1] = linea[1].replace("'","")
    linea[1] = linea[1].replace(" ","")
    linea[1] = linea[1].replace("]","")
    linea[1] = linea[1].replace("\n","")
    linea[1] = linea[1].split(",")
    PREDICCIONES[regla] = linea[1]



gramatica = "misArchivos/grammar.txt"
# gramatica = "gramaticaprueba.txt"
token = ""


def makeif(possible_values, isElif=False):
    construct_if = "if (toktoValtok(token)==" + '"'+possible_values[0]+'"'

    if(isElif):
        construct_if = "elif (toktoValtok(token)=="+ '"'+possible_values[0]+'"'

    if(len(possible_values)>1):
        for i in possible_values[1:]:
            construct_if+=" or " + "toktoValtok(token) == "+ '"'+i+'"'
        construct_if+="):\n"
    else:
        construct_if+="):\n"

    return construct_if

def elseImp(possible_values):
    impresion ="\telse: \n\t\terrorSintaxis(["+'"'+possible_values[0]+'"'
    if(len(possible_values)>1):
        for i in possible_values[1:]:
            impresion+=", "+'"'+i+'"'
        impresion+="]"
    else:
        impresion+="]"
    impresion+=",token)\n"
    return impresion


def createFunction(NOTERMINAL):
    return "def "+NOTERMINAL+"():\n"

SINTACTICO = ""

ident_tier = 0
for nt in NOTERMINALES:
    reglas = open (gramatica,'r')
    SINTACTICO+=createFunction(nt)
    first = False
    expected = []
    for key, value in PREDICCIONES.items():
        aux = key.replace('\n','')
        aux = aux.split(" ")                
        if(aux[0] == nt):
            SINTACTICO+= "\t"+makeif(value, first) 
            for val in value:
                if(val not in expected):
                    expected.append(val)
            regla = aux.pop(1)
            for i in aux[1:]:
                if(i in NOTERMINALES):
                    SINTACTICO+="\t\t"+i+"()\n"
                elif(i=="epsilon"):
                    SINTACTICO+="\t\thola()\n" 
                else:
                    SINTACTICO+="\t\temparejar("+'"'+i+'"'+")\n"                
            first = True
    #Sort
    SINTACTICO +=elseImp(expected)
    

print(SINTACTICO)


