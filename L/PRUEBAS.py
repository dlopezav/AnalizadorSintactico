
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
              , 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'
              , 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

reservadas = ['booleano', 'caracter', 'entero', 'real', 'cadena', 'funcion_principal', 'fin_principal',
              'leer', 'imprimir', 'si', 'entonces', 'fin_si', 'si_no', 'mientras', 'hacer', 'fin_mientras', 
              'para', 'fin_para', 'seleccionar', 'entre', 'caso', 'romper', 'defecto', 'fin_seleccionar',
              'estructura', 'fin_estructura', 'funcion','retornar','fin_funcion','verdadero','falso']

comentario = ['//', '/*', '*/']

todo = abc + ABC

	
tk_sim= {'+':"tk_mas", '-':"tk_menos", '*':"tk_mult", '/':"tk_div", '%':"tk_mod", '=':"tk_asig", '<': "tk_menor",
            '>':"tk_mayor",'<=':"tk_menor_igual",'>=':"tk_mayor_igual",'==':"tk_igual",'&&':"tk_y", '||':"tk_o",
            '!=':"tk_dif",'!':"tk_neg", ':':"tk_dosp", ';':"tk_pyc",',':"tk_coma",'.':"tk_punto", '(':"tk_par_izq",
            ')':"tk_par_der"}

tk_simind= {'|':"or",'&':"and"}

tk_dato = {'verdadero':"tk_booleano", 'falso':"tk_booleano", 'int':"tk_entero", 'real':"tk_real",
            'cadena':"tk_cadena", 'caracter':"tk_caracter"}
    
numero = ['1','2','3','4','5','6','7','8','9','0']
malasletras = ['ñ','Ñ','\\']
salto = ['\n']

caracter = abc + ABC + [' '] + ['_'] + numero
palabra = abc + ABC + ['_'] + numero
state = 0
fil=0
fila = 0
columna = 0

word = ''
final = ''
bandera = 0
safe = True
#PASANDO POR CADA UNA DE LAS FILA
class Analizador():
    def __init__(self):
        self.frases = self.lexico()
        self.idx = 0

    def next(self):
        self.idx +=1
        return self.frases[self.idx-1]

    def error(self, X, Y):
        ad = '>>> Error lexico (linea: '+ str(X) + ', posicion: '+ str(Y) +')'
        return ad

    def reserv(self,word, X, Y):
        ad = '<'+word+','+ str(X) +','+ str(Y) + '>'+'\n'
        return ad

    def lexema(self,tk, word, X, Y):
        ad = '<'+tk+','+ word +','+ str(X) +','+ str(Y) +'>'+'\n'
        return ad

    def token(self,tk, X, Y):
        ad = '<'+tk+','+ str(X) +','+ str(Y) +'>'+'\n'
        return ad

    def lexico(self):
        state = 0
        fil=0
        fila = 0
        columna = 0

        word = ''

        final = ''
        bandera = 0
        safe = True
        #PASANDO POR CADA UNA DE LAS FILA
        frases = open ('entrada.txt','r')

        for frase in frases:
            frase = frase.replace('\n','')
            simbolo = 0
            fila+=1
        #PASANDO POR CADA UNO DE LOS ELEMENTOS
            while(simbolo < len(frase)):
                if(state == 0):
                    columna = simbolo
                    #
                    if(frase[simbolo] in todo):
                        fil = fila
                        state = 1
                        word+=frase[simbolo]
                        simbolo+=1
                        
                    elif(frase[simbolo] == ' ' or frase[simbolo]=='\t'):
                        fil = fila
                        simbolo+=1
                        
                    elif(frase[simbolo] == "'"):
                        fil = fila
                        word+=frase[simbolo]
                        simbolo+=1
                        state = 2
                        
                    elif(frase[simbolo] == '"'):
                        fil = fila
                        word+=frase[simbolo]
                        simbolo+=1
                        state = 5
                        
                    elif(frase[simbolo] in numero):
                        fil = fila
                        word+=frase[simbolo]
                        simbolo+=1
                        state = 7
                        
                    elif(frase[simbolo] == '/'):
                        fil = fila
                        simbolo+=1
                        state = 10
                        
                    elif(frase[simbolo] in tk_sim or frase[simbolo] in tk_simind):
                        fil = fila
                        word+=frase[simbolo]
                        simbolo+=1
                        state = 14
                    elif(frase[simbolo] == ' '):
                        simbolo+=1
                    else:
                        fil = fila
                        final+=self.error(fil, columna+1)
                        bandera = 1
                        break;
                    
                #Palabras reservadas o ID's
                elif(state == 1):
                    if(frase[simbolo] in palabra):
                        word+=frase[simbolo]
                        simbolo += 1
                    elif(word in reservadas):
                        final+=self.reserv(word,fil,columna+1)
                        word = ''
                        state = 0
                    elif(frase[simbolo] in malasletras):
                        final+=self.lexema('id',word,fil,columna+1)
                        fil+=len(word)
                        final+=self.error(fil, columna+1)
                        bandera = 1
                        break;
                    else:
                        final+=self.lexema('id',word,fil,columna+1)
                        word = ''
                        state = 0
                #3 Caracteres
                elif(state == 2):
                    if(frase[simbolo] in caracter):
                        word+=frase[simbolo]
                        state = 3
                        simbolo += 1
                    elif(frase[simbolo] == '\\'):
                        word+=frase[simbolo]
                        state = 4
                        simbolo += 1
                    else:
                        final+=self.error(fil, columna+1)
                        bandera = 1
                        break;
                #4 caracter bien
                elif(state == 3):
                    if(frase[simbolo]=="'"):
                        word+=frase[simbolo]
                        simbolo += 1
                        final+=self.lexema(tk_dato['caracter'],word,fil,columna+1)
                        word=''
                        state = 0
                    else:
                        final+=self.error(fil, columna+1)
                        bandera = 1
                        break;
                #5 caracter \n
                elif(state == 4):
                    if(frase[simbolo]=='n'):
                        word+=frase[simbolo]
                        simbolo += 1
                        state = 3
                    else:
                        final+=self.error(fil, columna+1)
                        bandera = 1
                        break;
                #6 String
                elif(state == 5):
                    if(frase[simbolo] in caracter):
                        word+=frase[simbolo]
                        state = 5
                        simbolo += 1
                    elif(frase[simbolo] == '\\'):
                        word+=frase[simbolo]
                        state = 6
                        simbolo += 1
                    elif(frase[simbolo] == '"'):
                        word+=frase[simbolo]
                        simbolo += 1
                        final+=self.lexema(tk_dato['cadena'], word,fil,columna+1)
                        state = 0
                        word=''
                    else:
                        final+=self.error(fil, columna+1)
                        bandera = 1
                        break;
                #7 String - \n
                elif(state == 6):
                    if(frase[simbolo]=='n'):
                        word+=frase[simbolo]
                        simbolo += 1
                        state = 5
                    else:
                        final+=self.error(fil, columna+1)
                        bandera = 1
                        break;
                #8 Entero o Double - \n
                elif(state == 7):
                    if(frase[simbolo] in numero):
                        word+=frase[simbolo]
                        simbolo += 1
                        state = 7
                    elif(frase[simbolo] == '.'):
                        word+=frase[simbolo]
                        simbolo += 1
                        state = 8
                    else:
                        final+=self.lexema(tk_dato['int'], word,fil,columna+1)
                        word = ''
                        state = 0
                #9 INT - \n
                elif(state == 8):
                    if(frase[simbolo] in numero):
                        word+=frase[simbolo]
                        simbolo += 1
                        state = 9
                    else:
                        final+=self.lexema(tk_dato['int'], word,fil,columna+1)
                        word = ''
                        state = 0
                #10 Verificación Double
                elif(state == 9):
                    if(frase[simbolo] in numero):
                        word+=frase[simbolo]
                        simbolo += 1
                        state = 9
                    else:
                        final+=self.lexema(tk_dato['real'], word,fil,columna+1)
                        word = ''
                        state = 0
                #11  Comentarios
                elif(state == 10):
                    if(frase[simbolo] == '/'):
                        simbolo += 1
                        state = 11
                    elif(frase[simbolo] == '*'):
                        safe = False
                        state = 12
                        simbolo += 1
                    else:
                        word += '/'
                        final+=self.token(tk_sim[word],fil,columna+1)
                        word=''
                        state = 0
                #12 // Comentarios //
                elif(state == 11):
                    if(simbolo+1==len(frase)):
                        state = 0
                        simbolo += 1
                    else:
                        simbolo += 1
                        state = 11
                #13 Comentarios /*
                elif(state == 12):
                    if(frase[simbolo] == '*'):
                        simbolo += 1
                        state = 13
                    else:
                        simbolo += 1
                        state = 12
                #14 Comentarios cierre /*
                elif(state == 13):
                    if(frase[simbolo] == '/'):
                        state = 0
                        simbolo += 1
                        safe = True
                    else: 
                        state = 12
                #15 Simbolos
                elif(state == 14):
                    if(word+frase[simbolo] in tk_sim):
                        word+=frase[simbolo]
                        final+=self.token(tk_sim[word],fil,columna+1)
                        word = ''
                        state = 0
                        simbolo += 1
                    elif(word in tk_sim): 
                        final+=self.token(tk_sim[word],fil,columna+1)
                        word = ''
                        state = 0
                    elif(word in tk_simind):
                        final+=self.error(fil, columna+1)+'\n'
                        bandera = 1
                        break;
                    else:
                        word = ''
                        state = 0
                        
                #PALABRAS SOLAS VERIFICACIÓN
                if(simbolo==len(frase)):
                    if(state == 1 ):
                        if(word in reservadas):
                            final+=self.reserv(word,fil,columna+1)
                            word = ''
                        else:
                            final+=self.lexema('id',word,fil,columna+1)
                            word = ''
                        state = 0
                        word = ''
                    elif(state == 8):
                        final+=self.lexema(tk_dato['int'], word,fil,columna+1)
                        state = 0
                        word = ''
                    elif(state == 9):
                        final+=self.lexema(tk_dato['real'], word,fil,columna+1)
                        state = 0
                        word = ''
                    elif(state == 14):
                        final+=self.token(tk_sim[word],fil,columna+1)
                        word=''
                        state = 0
                    elif(state == 7):
                        final+=self.lexema(tk_dato['int'], word,fil,columna+1)
                        word = ''
                        state = 0
                    elif(state == 2 and word == "'"):
                        final+=self.error(fil, columna+1)
                        bandera = 1
                        break;
                    elif(state == 3):
                        final+=self.error(fil, columna+1)
                        bandera = 1
                        break;
                    elif(state == 10):
                        word += '/'
                        final+=self.token(tk_sim[word],fil,columna+1)
                        word=''
                        state = 0
                
            if bandera == 1:
                break;
        final = final.split('\n')[:-1]
        return final

