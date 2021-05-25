reglas = open ('misArchivos/grammar.txt','r')
NOTERMINALES = []
for regla in reglas:
    regla = regla.replace('\n','')
    regla = regla.split(" ")
    if(regla[0] not in NOTERMINALES):
        NOTERMINALES.append(regla[0])


primeros = open ('primeroscalculados.txt','r')
PRIMEROS = {}
for linea in primeros:
    regla = linea.split(" ")
    no_terminal = regla[0]
    linea = linea.replace(" ","")
    split = linea[len(no_terminal)+2:-2].replace("'", "").split(',')
    PRIMEROS[no_terminal] = split


def PRIMEROSDERECHA(beta):
    primerosB = []
    for elemento in beta: 
        if(elemento not in NOTERMINALES):
            if(elemento not in primerosB):
                primerosB.append(elemento)
            break
        if(elemento in NOTERMINALES):
            for i in PRIMEROS[elemento]:
                if(i not in primerosB and i != "epsilon"):
                    primerosB.append(i)
            if("epsilon" in PRIMEROS[elemento]):
                if(len(beta) == 1 and "epsilon" not in primerosB):
                    primerosB.append("epsilon")
                    break
                else:
                    continue
            else:
                break
            for i in PRIMEROS[elemento]:
                if(i not in primerosB and i != "epsilon"):
                    primerosB.append(i)
                primerosB.append("epsilon")
    return primerosB


siguientes = open ('segundoscalculados.txt','r')
SIGUIENTES = {}
for linea in siguientes:
    regla = linea.split(" ")
    no_terminal = regla[0]
    linea = linea.replace(" ","")
    split = linea[len(no_terminal)+2:-2].replace("'", "").split(',')
    SIGUIENTES[no_terminal] = split


PREDICCIONES = {}
reglas = open ('misArchivos/grammar.txt','r')
for regla in reglas:
    regla = regla.replace('\n','')
    PREDICCIONES[regla] = []



reglas = open ('misArchivos/grammar.txt','r')
for regla in reglas:
    regla = regla.replace('\n','')
    reglaAux = regla.split(" ")
    reglaAux.pop(1)
    if("epsilon" in PRIMEROSDERECHA(reglaAux[1:])):
        for i in PRIMEROSDERECHA(reglaAux[1:]):
            if(i != "epsilon" and i not in PREDICCIONES[regla]):
                PREDICCIONES[regla].append(i)
        for i in SIGUIENTES[reglaAux[0]]:
            if(i != "epsilon" and i not in PREDICCIONES[regla]):
                PREDICCIONES[regla].append(i)
        
    else:
        # print(regla)
        for i in PRIMEROSDERECHA(reglaAux[1:]):
            if(i != "epsilon" and i not in PREDICCIONES[regla]):
                PREDICCIONES[regla].append(i)



# print(PRIMEROS)
# print(SIGUIENTES)
for key, value in PREDICCIONES.items():
    print(key, value)

