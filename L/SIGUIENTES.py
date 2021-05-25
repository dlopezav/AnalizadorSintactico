reglas = open ('misArchivos/grammar.txt','r')
NOTERMINALES = []
for regla in reglas:
    regla = regla.replace('\n','')
    regla = regla.split(" ")
    if(regla[0] not in NOTERMINALES):
        NOTERMINALES.append(regla[0])


SIGUIENTES = {}
for nt in NOTERMINALES:
    SIGUIENTES[nt] = []

SIGUIENTES['S'] = ['EOF']

primeros = open ('primeroscalculados.txt','r')
PRIMEROS = {}
for linea in primeros:
    regla = linea.split(" ")
    no_terminal = regla[0]
    linea = linea.replace(" ","")
    split = linea[len(no_terminal)+2:-2].replace("'", "").split(',')
    PRIMEROS[no_terminal] = split
    


reglas = open ('misArchivos/grammar.txt','r')
bandera = True
while(bandera):
    start = {key: value[:] for key, value in SIGUIENTES.items()}
    for nt in NOTERMINALES:
        reglas = open ('misArchivos/grammar.txt','r')
        A = nt
        for regla in reglas:
            regla = regla.replace('\n','')
            regla = regla.split(" ")
            regla.pop(1)
            B = regla[0]
            for i in range(1, len(regla)):
                elemento = regla[i]
                if(elemento == A):
                    if(i == len(regla)-1):
                        beta = ["epsilon"]
                    else:
                        beta = regla[i+1:]
                        beta.append("epsilon")
                    result = []
                    for b in beta:
                        if(b == "epsilon"):
                            for k in SIGUIENTES[B]:
                                if(k not in SIGUIENTES[A]):
                                    SIGUIENTES[A].append(k)
                        elif(b in NOTERMINALES):
                            for j in PRIMEROS[b]:
                                
                                if(j != "epsilon" and j not in SIGUIENTES[A]):
                                    SIGUIENTES[A].append(j)
                            if("epsilon" not in PRIMEROS[b]):
                                break
                            else:
                                continue
                        else:
                            if b not in SIGUIENTES[A]:
                                SIGUIENTES[A].append(b)
                            break   
                    if('' in SIGUIENTES[A]):
                        print("ojo con la regla: ", regla)
    final = {key: value[:] for key, value in SIGUIENTES.items()} 
    if(start!=final):
        bandera = True
    else:
        bandera = False

                
for key, value in SIGUIENTES.items():
    print(key, value)