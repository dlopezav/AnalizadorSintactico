reglas = open ('misArchivos/grammar.txt','r')
NOTERMINALES = []
for regla in reglas:
    regla = regla.replace('\n','')
    regla = regla.split(" ")
    if(regla[0] not in NOTERMINALES):
        NOTERMINALES.append(regla[0])

PRIMEROS = {}

for nt in NOTERMINALES:
    PRIMEROS[nt] = []

bandera = True
a = 0
while(bandera):
    start = {key: value[:] for key, value in PRIMEROS.items()}
    for nt in NOTERMINALES:
        reglas = open ('misArchivos/grammar.txt','r')
        for regla in reglas:
            regla = regla.replace('\n','')
            regla = regla.split(" ")
            regla.pop(1)
            if(regla[0]==nt):
                for elemento in regla:                    
                    if(elemento not in NOTERMINALES):
                        if(elemento not in PRIMEROS[nt]):
                            PRIMEROS[nt].append(elemento)
                        break
                    if(elemento in NOTERMINALES and elemento != nt):
                        if("epsilon" not in PRIMEROS[elemento]):
                            for i in PRIMEROS[elemento]:
                                if(i not in PRIMEROS[nt]):
                                    PRIMEROS[nt].append(i)
                            break
                        else:
                            for i in PRIMEROS[elemento]:
                                if(i not in PRIMEROS[nt] and i != "epsilon"):
                                    PRIMEROS[nt].append(i)
                            if(len(regla) == 2 and "epsilon" not in PRIMEROS[nt]):
                                PRIMEROS[nt].append("epsilon")
                        for i in PRIMEROS[elemento]:
                            if(i not in PRIMEROS[nt] and i != "epsilon"):
                                PRIMEROS[nt].append(i)

                            
    final = {key: value[:] for key, value in PRIMEROS.items()}
    if(start!=final):
        bandera = True
    else:
        bandera = False
for key, value in PRIMEROS.items():
    print(key, value)

                
