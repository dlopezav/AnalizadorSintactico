from PRUEBAS import Analizador

global error
global token
error = 0
def errorSintaxis(values,token):
	global error
	values = ordenar(values)
	if("funcion_principal" not in values):
		if(error):
			hola()
		else:
			if("EOF" in token):
				fil,columna = token.split(",")[-2:]
			else:
				fil,columna = token.split(",")[-2:]
				
			
			if(token.split(",")[0][1:] in diferenciar):
				print("<"+fil+","+columna[:-1]+"> Error sintactico: se encontro: "+'"'+Lista[token.split(",")[0][1:]]+'"'+"; se esperaba: "+toStr(values)+".",end="")
			elif(token.split(",")[0][1:] in valores):
				print("<"+fil+","+columna[:-1]+"> Error sintactico: se encontro: "+'"'+token.split(",")[1]+'"'+"; se esperaba: "+toStr(values)+".",end="")
			else:
				print("<"+fil+","+columna[:-1]+"> Error sintactico: se encontro: "+'"'+token.split(",")[0][1:]+'"'+"; se esperaba: "+toStr(values)+".",end="")
	elif(not error):
		print("Error sintactico: falta funcion_principal",end="")
	error = 1

def toStr(values):
	if(values[0] not in Lista):
		concat='"'+values[0]+'"'
	else:
		concat= '"'+Lista[values[0]]+'"'
	if(len(values)>0):
		for i in values[1:]:
			if(i not in Lista):
				concat+=", "+'"'+i+'"'
			else:
				concat+=", "+'"'+Lista[i]+'"'

	return concat
	

def toktoValtok(token):
	if("EOF" not in token):
		return token.split(",")[0][1:]
	else:
		return token.split(",")[1]

Lexico = Analizador()


def emparejar(tokenEsperado):
	global error
	global token
	#print(tokenEsperado,token)
	if (toktoValtok(token) == tokenEsperado):
		if(not toktoValtok(token)=="EOF"):
			token = Lexico.next()
	else:
		errorSintaxis([tokenEsperado],token)

def S():
	if (toktoValtok(token)=="estructura" or toktoValtok(token) == "funcion" or toktoValtok(token) == "id" or toktoValtok(token) == "booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena" or toktoValtok(token) == "funcion_principal"):
		GLOBAL()
		FUNCION_PRINCIPAL()
		GLOBAL()
		emparejar("EOF")
	else: 
		errorSintaxis(["estructura", "funcion", "id", "booleano", "caracter", "entero", "real", "cadena", "funcion_principal"],token)
def GLOBAL():
	if (toktoValtok(token)=="estructura"):
		ESTRUCTURA()
		GLOBAL()
	elif (toktoValtok(token)=="funcion"):
		FUNCION()
		GLOBAL()
	elif (toktoValtok(token)=="id" or toktoValtok(token) == "booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena"):
		VAR_GLOBAL()
		GLOBAL()
	elif (toktoValtok(token)=="funcion_principal" or toktoValtok(token) == "EOF"):
		hola()
	else: 
		errorSintaxis(["estructura", "funcion", "id", "booleano", "caracter", "entero", "real", "cadena", "funcion_principal", "EOF"],token)
def FUNCION_PRINCIPAL():
	if (toktoValtok(token)=="funcion_principal"):
		emparejar("funcion_principal")
		INSTRUCCIONES()
		emparejar("fin_principal")
	else: 
		errorSintaxis(["funcion_principal"],token)
def ESTRUCTURA():
	if (toktoValtok(token)=="estructura"):
		emparejar("estructura")
		emparejar("id")
		ATRIBUTOS()
		emparejar("fin_estructura")
	else: 
		errorSintaxis(["estructura"],token)
def ATRIBUTOS():
	if (toktoValtok(token)=="id" or toktoValtok(token) == "booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena"):
		TIPO()
		DEC_VARIABLE()
		emparejar("tk_pyc")
		ATRIBUTOS()
	elif (toktoValtok(token)=="fin_estructura"):
		hola()
	else: 
		errorSintaxis(["id", "booleano", "caracter", "entero", "real", "cadena", "fin_estructura"],token)
def FUNCION():
	if (toktoValtok(token)=="funcion"):
		emparejar("funcion")
		TIPO()
		emparejar("id")
		emparejar("tk_par_izq")
		PARAMETROS()
		emparejar("tk_par_der")
		emparejar("hacer")
		INSTRUCCIONES_FUNCION()
		RETORNO()
		emparejar("fin_funcion")
	else: 
		errorSintaxis(["funcion"],token)
def PARAMETROS():
	if (toktoValtok(token)=="id" or toktoValtok(token) == "booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena"):
		TIPO()
		emparejar("id")
		PARAMETROS2()
	elif (toktoValtok(token)=="tk_par_der"):
		hola()
	else: 
		errorSintaxis(["id", "booleano", "caracter", "entero", "real", "cadena", "tk_par_der"],token)
def PARAMETROS2():
	if (toktoValtok(token)=="tk_coma"):
		emparejar("tk_coma")
		TIPO()
		emparejar("id")
		PARAMETROS2()
	elif (toktoValtok(token)=="tk_par_der"):
		hola()
	else: 
		errorSintaxis(["tk_coma", "tk_par_der"],token)
def VAR_GLOBAL():
	if (toktoValtok(token)=="id" or toktoValtok(token) == "booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena"):
		TIPO()
		DEC_VARIABLE()
		emparejar("tk_pyc")
	else: 
		errorSintaxis(["id", "booleano", "caracter", "entero", "real", "cadena"],token)
def INSTRUCCIONES():
	if (toktoValtok(token)=="leer"):
		LEER()
		INSTRUCCIONES()
	elif (toktoValtok(token)=="imprimir"):
		IMPRIMIR()
		INSTRUCCIONES()
	elif (toktoValtok(token)=="si"):
		SI()
		INSTRUCCIONES()
	elif (toktoValtok(token)=="mientras"):
		MIENTRAS()
		INSTRUCCIONES()
	elif (toktoValtok(token)=="hacer"):
		HACER_MIENTRAS()
		INSTRUCCIONES()
	elif (toktoValtok(token)=="para"):
		PARA()
		INSTRUCCIONES()
	elif (toktoValtok(token)=="seleccionar"):
		SELECCIONAR()
		INSTRUCCIONES()
	elif (toktoValtok(token)=="booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena" or toktoValtok(token) == "id"):
		DECLARACION_ASIGNACION()
		INSTRUCCIONES()
	elif (toktoValtok(token)=="romper"):
		ROMPER()
		INSTRUCCIONES()
	elif (toktoValtok(token)=="fin_principal" or toktoValtok(token) == "fin_mientras"):
		hola()
	else: 
		errorSintaxis(["leer", "imprimir", "si", "mientras", "hacer", "para", "seleccionar", "booleano", "caracter", "entero", "real", "cadena", "id", "romper", "fin_principal", "fin_mientras"],token)
def TIPO():
	if (toktoValtok(token)=="id"):
		emparejar("id")
	elif (toktoValtok(token)=="booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena"):
		PRIMITIVO()
	else: 
		errorSintaxis(["id", "booleano", "caracter", "entero", "real", "cadena"],token)
def PRIMITIVO():
	if (toktoValtok(token)=="booleano"):
		emparejar("booleano")
	elif (toktoValtok(token)=="caracter"):
		emparejar("caracter")
	elif (toktoValtok(token)=="entero"):
		emparejar("entero")
	elif (toktoValtok(token)=="real"):
		emparejar("real")
	elif (toktoValtok(token)=="cadena"):
		emparejar("cadena")
	else: 
		errorSintaxis(["booleano", "caracter", "entero", "real", "cadena"],token)
def LEER():
	if (toktoValtok(token)=="leer"):
		emparejar("leer")
		emparejar("tk_par_izq")
		IDENTIFICADOR()
		emparejar("tk_par_der")
		emparejar("tk_pyc")
	else: 
		errorSintaxis(["leer"],token)
def IMPRIMIR():
	if (toktoValtok(token)=="imprimir"):
		emparejar("imprimir")
		emparejar("tk_par_izq")
		IMPRESION()
		emparejar("tk_par_der")
		emparejar("tk_pyc")
	else: 
		errorSintaxis(["imprimir"],token)
def IMPRESION():
	if (toktoValtok(token)=="tk_par_izq" or toktoValtok(token) == "tk_menos" or toktoValtok(token) == "tk_neg" or toktoValtok(token) == "id" or toktoValtok(token) == "tk_entero" or toktoValtok(token) == "tk_real" or toktoValtok(token) == "tk_caracter" or toktoValtok(token) == "tk_cadena" or toktoValtok(token) == "verdadero" or toktoValtok(token) == "falso"):
		EXPRESION()
		IMPRESION2()
	else: 
		errorSintaxis(["tk_par_izq", "tk_menos", "tk_neg", "id", "tk_entero", "tk_real", "tk_caracter", "tk_cadena", "verdadero", "falso"],token)
def IMPRESION2():
	if (toktoValtok(token)=="tk_coma"):
		emparejar("tk_coma")
		EXPRESION()
		IMPRESION2()
	elif (toktoValtok(token)=="tk_par_der"):
		hola()
	else: 
		errorSintaxis(["tk_coma", "tk_par_der"],token)
def SI():
	if (toktoValtok(token)=="si"):
		emparejar("si")
		emparejar("tk_par_izq")
		EXPRESION()
		emparejar("tk_par_der")
		emparejar("entonces")
		INSTRUCCIONES_IF()
		SI_NO()
		emparejar("fin_si")
	else: 
		errorSintaxis(["si"],token)
def INSTRUCCIONES_IF():
	if (toktoValtok(token)=="leer"):
		LEER()
		INSTRUCCIONES_IF2()
	elif (toktoValtok(token)=="imprimir"):
		IMPRIMIR()
		INSTRUCCIONES_IF2()
	elif (toktoValtok(token)=="si"):
		SI()
		INSTRUCCIONES_IF2()
	elif (toktoValtok(token)=="mientras"):
		MIENTRAS()
		INSTRUCCIONES_IF2()
	elif (toktoValtok(token)=="hacer"):
		HACER_MIENTRAS()
		INSTRUCCIONES_IF2()
	elif (toktoValtok(token)=="para"):
		PARA()
		INSTRUCCIONES_IF2()
	elif (toktoValtok(token)=="seleccionar"):
		SELECCIONAR()
		INSTRUCCIONES_IF2()
	elif (toktoValtok(token)=="booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena" or toktoValtok(token) == "id"):
		DECLARACION_ASIGNACION()
		INSTRUCCIONES_IF2()
	elif (toktoValtok(token)=="romper"):
		ROMPER()
		INSTRUCCIONES_IF2()
	else: 
		errorSintaxis(["leer", "imprimir", "si", "mientras", "hacer", "para", "seleccionar", "booleano", "caracter", "entero", "real", "cadena", "id", "romper"],token)
def INSTRUCCIONES_IF2():
	if (toktoValtok(token)=="leer" or toktoValtok(token) == "imprimir" or toktoValtok(token) == "si" or toktoValtok(token) == "mientras" or toktoValtok(token) == "hacer" or toktoValtok(token) == "para" or toktoValtok(token) == "seleccionar" or toktoValtok(token) == "booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena" or toktoValtok(token) == "id" or toktoValtok(token) == "romper"):
		INSTRUCCIONES_IF()
	elif (toktoValtok(token)=="si_no" or toktoValtok(token) == "fin_si"):
		hola()
	else: 
		errorSintaxis(["leer", "imprimir", "si", "mientras", "hacer", "para", "seleccionar", "booleano", "caracter", "entero", "real", "cadena", "id", "romper", "si_no", "fin_si"],token)
def SI_NO():
	if (toktoValtok(token)=="si_no"):
		emparejar("si_no")
		INSTRUCCIONES_IF2()
	elif (toktoValtok(token)=="fin_si"):
		hola()
	else: 
		errorSintaxis(["si_no", "fin_si"],token)
def MIENTRAS():
	if (toktoValtok(token)=="mientras"):
		emparejar("mientras")
		emparejar("tk_par_izq")
		EXPRESION()
		emparejar("tk_par_der")
		emparejar("hacer")
		INSTRUCCIONES_MIENTRAS()
		emparejar("fin_mientras")
	else: 
		errorSintaxis(["mientras"],token)
def INSTRUCCIONES_MIENTRAS():
	if (toktoValtok(token)=="leer"):
		LEER()
		INSTRUCCIONES_MIENTRAS()
	elif (toktoValtok(token)=="imprimir"):
		IMPRIMIR()
		INSTRUCCIONES_MIENTRAS()
	elif (toktoValtok(token)=="si"):
		SI()
		INSTRUCCIONES_MIENTRAS()
	elif (toktoValtok(token)=="mientras"):
		MIENTRAS()
		INSTRUCCIONES_MIENTRAS()
	elif (toktoValtok(token)=="hacer"):
		HACER_MIENTRAS()
		INSTRUCCIONES_MIENTRAS()
	elif (toktoValtok(token)=="para"):
		PARA()
		INSTRUCCIONES_MIENTRAS()
	elif (toktoValtok(token)=="seleccionar"):
		SELECCIONAR()
		INSTRUCCIONES_MIENTRAS()
	elif (toktoValtok(token)=="booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena" or toktoValtok(token) == "id"):
		DECLARACION_ASIGNACION()
		INSTRUCCIONES_MIENTRAS()
	elif (toktoValtok(token)=="romper"):
		ROMPER()
		INSTRUCCIONES_MIENTRAS()
	elif (toktoValtok(token)=="fin_mientras"):
		hola()
	else: 
		errorSintaxis(["leer", "imprimir", "si", "mientras", "hacer", "para", "seleccionar", "booleano", "caracter", "entero", "real", "cadena", "id", "romper", "fin_mientras"],token)
def HACER_MIENTRAS():
	if (toktoValtok(token)=="hacer"):
		emparejar("hacer")
		INSTRUCCIONES_HACER_MIENTRAS()
	else: 
		errorSintaxis(["hacer"],token)
def INSTRUCCIONES_HACER_MIENTRAS():
	if (toktoValtok(token)=="leer" or toktoValtok(token) == "imprimir" or toktoValtok(token) == "si" or toktoValtok(token) == "hacer" or toktoValtok(token) == "booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena" or toktoValtok(token) == "id" or toktoValtok(token) == "seleccionar" or toktoValtok(token) == "para" or toktoValtok(token) == "romper"):
		INSTRUCCIONES_HACER_MIENTRAS2()
		INSTRUCCIONES_HACER_MIENTRAS()
	elif (toktoValtok(token)=="mientras"):
		emparejar("mientras")
		emparejar("tk_par_izq")
		EXPRESION()
		emparejar("tk_par_der")
		INSTRUCCIONES_HACER_MIENTRAS3()
	else: 
		errorSintaxis(["leer", "imprimir", "si", "hacer", "booleano", "caracter", "entero", "real", "cadena", "id", "seleccionar", "para", "romper", "mientras"],token)
def INSTRUCCIONES_HACER_MIENTRAS3():
	if (toktoValtok(token)=="hacer"):
		emparejar("hacer")
		INSTRUCCIONES()
		emparejar("fin_mientras")
		INSTRUCCIONES_HACER_MIENTRAS()
	elif (toktoValtok(token)=="tk_pyc"):
		emparejar("tk_pyc")
	else: 
		errorSintaxis(["hacer", "tk_pyc"],token)
def INSTRUCCIONES_HACER_MIENTRAS2():
	if (toktoValtok(token)=="leer"):
		LEER()
	elif (toktoValtok(token)=="imprimir"):
		IMPRIMIR()
	elif (toktoValtok(token)=="booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena" or toktoValtok(token) == "id"):
		DECLARACION_ASIGNACION()
	elif (toktoValtok(token)=="si"):
		SI()
	elif (toktoValtok(token)=="seleccionar"):
		SELECCIONAR()
	elif (toktoValtok(token)=="hacer"):
		HACER_MIENTRAS()
	elif (toktoValtok(token)=="para"):
		PARA()
	elif (toktoValtok(token)=="romper"):
		ROMPER()
	else: 
		errorSintaxis(["leer", "imprimir", "booleano", "caracter", "entero", "real", "cadena", "id", "si", "seleccionar", "hacer", "para", "romper"],token)
def PARA():
	if (toktoValtok(token)=="para"):
		emparejar("para")
		emparejar("tk_par_izq")
		EXP_PARA()
		emparejar("tk_pyc")
		EXPRESION()
		emparejar("tk_pyc")
		EXPRESION()
		emparejar("tk_par_der")
		emparejar("hacer")
		INSTRUCCIONES_PARA()
		emparejar("fin_para")
	else: 
		errorSintaxis(["para"],token)
def INSTRUCCIONES_PARA():
	if (toktoValtok(token)=="leer"):
		LEER()
		INSTRUCCIONES_PARA()
	elif (toktoValtok(token)=="imprimir"):
		IMPRIMIR()
		INSTRUCCIONES_PARA()
	elif (toktoValtok(token)=="si"):
		SI()
		INSTRUCCIONES_PARA()
	elif (toktoValtok(token)=="mientras"):
		MIENTRAS()
		INSTRUCCIONES_PARA()
	elif (toktoValtok(token)=="hacer"):
		HACER_MIENTRAS()
		INSTRUCCIONES_PARA()
	elif (toktoValtok(token)=="para"):
		PARA()
		INSTRUCCIONES_PARA()
	elif (toktoValtok(token)=="seleccionar"):
		SELECCIONAR()
		INSTRUCCIONES_PARA()
	elif (toktoValtok(token)=="booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena" or toktoValtok(token) == "id"):
		DECLARACION_ASIGNACION()
		INSTRUCCIONES_PARA()
	elif (toktoValtok(token)=="romper"):
		ROMPER()
		INSTRUCCIONES_PARA()
	elif (toktoValtok(token)=="fin_para"):
		hola()
	else: 
		errorSintaxis(["leer", "imprimir", "si", "mientras", "hacer", "para", "seleccionar", "booleano", "caracter", "entero", "real", "cadena", "id", "romper", "fin_para"],token)
def EXP_PARA():
	if (toktoValtok(token)=="booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena"):
		PRIMITIVO()
		emparejar("id")
		emparejar("tk_asig")
		EXPRESION()
	elif (toktoValtok(token)=="id"):
		emparejar("id")
		emparejar("tk_asig")
		EXPRESION()
	else: 
		errorSintaxis(["booleano", "caracter", "entero", "real", "cadena", "id"],token)
def SELECCIONAR():
	if (toktoValtok(token)=="seleccionar"):
		emparejar("seleccionar")
		emparejar("tk_par_izq")
		EXPRESION()
		emparejar("tk_par_der")
		emparejar("entre")
		CASOS()
		emparejar("fin_seleccionar")
	else: 
		errorSintaxis(["seleccionar"],token)
def CASOS():
	if (toktoValtok(token)=="caso"):
		emparejar("caso")
		EXPRESION()
		emparejar("tk_dosp")
		INSTRUCCIONES_CASOS()
		CASOS2()
	elif (toktoValtok(token)=="defecto"):
		emparejar("defecto")
		emparejar("tk_dosp")
		INSTRUCCIONES_CASOS()
	else: 
		errorSintaxis(["caso", "defecto"],token)
def CASOS2():
	if (toktoValtok(token)=="caso"):
		emparejar("caso")
		EXPRESION()
		emparejar("tk_dosp")
		INSTRUCCIONES_CASOS()
		CASOS2()
	elif (toktoValtok(token)=="defecto"):
		emparejar("defecto")
		emparejar("tk_dosp")
		INSTRUCCIONES_CASOS()
	elif (toktoValtok(token)=="fin_seleccionar"):
		hola()
	else: 
		errorSintaxis(["caso", "defecto", "fin_seleccionar"],token)
def INSTRUCCIONES_CASOS():
	if (toktoValtok(token)=="leer"):
		LEER()
		INSTRUCCIONES_CASOS()
	elif (toktoValtok(token)=="imprimir"):
		IMPRIMIR()
		INSTRUCCIONES_CASOS()
	elif (toktoValtok(token)=="si"):
		SI()
		INSTRUCCIONES_CASOS()
	elif (toktoValtok(token)=="mientras"):
		MIENTRAS()
		INSTRUCCIONES_CASOS()
	elif (toktoValtok(token)=="hacer"):
		HACER_MIENTRAS()
		INSTRUCCIONES_CASOS()
	elif (toktoValtok(token)=="para"):
		PARA()
		INSTRUCCIONES_CASOS()
	elif (toktoValtok(token)=="seleccionar"):
		SELECCIONAR()
		INSTRUCCIONES_CASOS()
	elif (toktoValtok(token)=="booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena" or toktoValtok(token) == "id"):
		DECLARACION_ASIGNACION()
		INSTRUCCIONES_CASOS()
	elif (toktoValtok(token)=="romper"):
		ROMPER()
		INSTRUCCIONES_CASOS()
	elif (toktoValtok(token)=="retornar"):
		RETORNO()
		INSTRUCCIONES_CASOS()
	elif (toktoValtok(token)=="caso" or toktoValtok(token) == "defecto" or toktoValtok(token) == "fin_seleccionar"):
		hola()
	else: 
		errorSintaxis(["leer", "imprimir", "si", "mientras", "hacer", "para", "seleccionar", "booleano", "caracter", "entero", "real", "cadena", "id", "romper", "retornar", "caso", "defecto", "fin_seleccionar"],token)
def DECLARACION_ASIGNACION():
	if (toktoValtok(token)=="booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena"):
		PRIMITIVO()
		DEC_VARIABLE()
		emparejar("tk_pyc")
	elif (toktoValtok(token)=="id"):
		emparejar("id")
		DECLARACION_ASIGNACION2()
		emparejar("tk_pyc")
	else: 
		errorSintaxis(["booleano", "caracter", "entero", "real", "cadena", "id"],token)
def DECLARACION_ASIGNACION2():
	if (toktoValtok(token)=="id"):
		emparejar("id")
		ASIGNACION()
	elif (toktoValtok(token)=="tk_punto"):
		IDESTRUC()
		ASIGNACION()
	elif (toktoValtok(token)=="tk_asig"):
		ASIGNACIONDEC()
	elif (toktoValtok(token)=="tk_asig"):
		emparejar("tk_asig")
		emparejar("id")
		CALL()
	elif (toktoValtok(token)=="tk_par_izq"):
		CALL()
	elif (toktoValtok(token)=="id"):
		DEC_VARIABLE()
	else: 
		errorSintaxis(["id", "tk_punto", "tk_asig", "tk_par_izq"],token)
def ASIGNACIONDEC():
	if (toktoValtok(token)=="tk_asig"):
		emparejar("tk_asig")
		EXPRESION()
	else: 
		errorSintaxis(["tk_asig"],token)
def DEC_VARIABLE():
	if (toktoValtok(token)=="id"):
		VARIABLE()
		DEC_VARIABLE2()
	else: 
		errorSintaxis(["id"],token)
def DEC_VARIABLE2():
	if (toktoValtok(token)=="tk_coma"):
		emparejar("tk_coma")
		VARIABLE()
		DEC_VARIABLE2()
	elif (toktoValtok(token)=="tk_pyc"):
		hola()
	else: 
		errorSintaxis(["tk_coma", "tk_pyc"],token)
def VARIABLE():
	if (toktoValtok(token)=="id"):
		emparejar("id")
		ASIGNACION()
	else: 
		errorSintaxis(["id"],token)
def ASIGNACION():
	if (toktoValtok(token)=="tk_asig"):
		emparejar("tk_asig")
		EXPRESION()
	elif (toktoValtok(token)=="tk_pyc" or toktoValtok(token) == "tk_coma"):
		hola()
	else: 
		errorSintaxis(["tk_asig", "tk_pyc", "tk_coma"],token)
def IDESTRUC():
	if (toktoValtok(token)=="tk_punto"):
		emparejar("tk_punto")
		emparejar("id")
		IDESTRUC2()
	else: 
		errorSintaxis(["tk_punto"],token)
def IDESTRUC2():
	if (toktoValtok(token)=="tk_punto"):
		emparejar("tk_punto")
		emparejar("id")
		IDESTRUC2()
	elif (toktoValtok(token)=="tk_asig" or toktoValtok(token) == "tk_pyc" or toktoValtok(token) == "tk_y" or toktoValtok(token) == "tk_o" or toktoValtok(token) == "tk_igual" or toktoValtok(token) == "tk_dif" or toktoValtok(token) == "tk_menor" or toktoValtok(token) == "tk_mayor" or toktoValtok(token) == "tk_menor_igual" or toktoValtok(token) == "tk_mayor_igual" or toktoValtok(token) == "tk_mas" or toktoValtok(token) == "tk_menos" or toktoValtok(token) == "tk_mult" or toktoValtok(token) == "tk_mod" or toktoValtok(token) == "tk_div" or toktoValtok(token) == "tk_coma" or toktoValtok(token) == "tk_par_der" or toktoValtok(token) == "tk_dosp"):
		hola()
	else: 
		errorSintaxis(["tk_punto", "tk_asig", "tk_pyc", "tk_y", "tk_o", "tk_igual", "tk_dif", "tk_menor", "tk_mayor", "tk_menor_igual", "tk_mayor_igual", "tk_mas", "tk_menos", "tk_mult", "tk_mod", "tk_div", "tk_coma", "tk_par_der", "tk_dosp"],token)
def ROMPER():
	if (toktoValtok(token)=="romper"):
		emparejar("romper")
		emparejar("tk_pyc")
	else: 
		errorSintaxis(["romper"],token)
def RETORNO():
	if (toktoValtok(token)=="retornar"):
		emparejar("retornar")
		EXPRESION()
		emparejar("tk_pyc")
	else: 
		errorSintaxis(["retornar"],token)
def CALL():
	if (toktoValtok(token)=="tk_par_izq"):
		emparejar("tk_par_izq")
		PARAMETROS_FUNCION()
		emparejar("tk_par_der")
	else: 
		errorSintaxis(["tk_par_izq"],token)
def PARAMETROS_FUNCION():
	if (toktoValtok(token)=="tk_par_izq" or toktoValtok(token) == "tk_menos" or toktoValtok(token) == "tk_neg" or toktoValtok(token) == "id" or toktoValtok(token) == "tk_entero" or toktoValtok(token) == "tk_real" or toktoValtok(token) == "tk_caracter" or toktoValtok(token) == "tk_cadena" or toktoValtok(token) == "verdadero" or toktoValtok(token) == "falso"):
		EXPRESION()
		PARAMETROS_FUNCION2()
	elif (toktoValtok(token)=="tk_par_der"):
		hola()
	else: 
		errorSintaxis(["tk_par_izq", "tk_menos", "tk_neg", "id", "tk_entero", "tk_real", "tk_caracter", "tk_cadena", "verdadero", "falso", "tk_par_der"],token)
def PARAMETROS_FUNCION2():
	if (toktoValtok(token)=="tk_coma"):
		emparejar("tk_coma")
		EXPRESION()
		PARAMETROS_FUNCION2()
	elif (toktoValtok(token)=="tk_par_der"):
		hola()
	else: 
		errorSintaxis(["tk_coma", "tk_par_der"],token)
def IDENTIFICADOR():
	if (toktoValtok(token)=="id"):
		emparejar("id")
		IDENTIFICADOR2()
	else: 
		errorSintaxis(["id"],token)
def IDENTIFICADOR2():
	if (toktoValtok(token)=="tk_punto"):
		emparejar("tk_punto")
		emparejar("id")
		IDENTIFICADOR2()
	elif (toktoValtok(token)=="tk_par_der"):
		hola()
	else: 
		errorSintaxis(["tk_punto", "tk_par_der"],token)
def EXPRESION():
	if (toktoValtok(token)=="tk_par_izq" or toktoValtok(token) == "tk_menos" or toktoValtok(token) == "tk_neg" or toktoValtok(token) == "id" or toktoValtok(token) == "tk_entero" or toktoValtok(token) == "tk_real" or toktoValtok(token) == "tk_caracter" or toktoValtok(token) == "tk_cadena" or toktoValtok(token) == "verdadero" or toktoValtok(token) == "falso"):
		VALOR()
		OPERADOR()
	else: 
		errorSintaxis(["tk_par_izq", "tk_menos", "tk_neg", "id", "tk_entero", "tk_real", "tk_caracter", "tk_cadena", "verdadero", "falso"],token)
def OPERADOR():
	if (toktoValtok(token)=="tk_y"):
		emparejar("tk_y")
		EXPRESION()
	elif (toktoValtok(token)=="tk_o"):
		emparejar("tk_o")
		EXPRESION()
	elif (toktoValtok(token)=="tk_igual"):
		emparejar("tk_igual")
		EXPRESION()
	elif (toktoValtok(token)=="tk_dif"):
		emparejar("tk_dif")
		EXPRESION()
	elif (toktoValtok(token)=="tk_menor"):
		emparejar("tk_menor")
		EXPRESION()
	elif (toktoValtok(token)=="tk_mayor"):
		emparejar("tk_mayor")
		EXPRESION()
	elif (toktoValtok(token)=="tk_menor_igual"):
		emparejar("tk_menor_igual")
		EXPRESION()
	elif (toktoValtok(token)=="tk_mayor_igual"):
		emparejar("tk_mayor_igual")
		EXPRESION()
	elif (toktoValtok(token)=="tk_mas"):
		emparejar("tk_mas")
		EXPRESION()
	elif (toktoValtok(token)=="tk_menos"):
		emparejar("tk_menos")
		EXPRESION()
	elif (toktoValtok(token)=="tk_mult"):
		emparejar("tk_mult")
		EXPRESION()
	elif (toktoValtok(token)=="tk_mod"):
		emparejar("tk_mod")
		EXPRESION()
	elif (toktoValtok(token)=="tk_div"):
		emparejar("tk_div")
		EXPRESION()
	elif (toktoValtok(token)=="tk_coma" or toktoValtok(token) == "tk_par_der" or toktoValtok(token) == "tk_pyc" or toktoValtok(token) == "tk_dosp"):
		hola()
	else: 
		errorSintaxis(["tk_y", "tk_o", "tk_igual", "tk_dif", "tk_menor", "tk_mayor", "tk_menor_igual", "tk_mayor_igual", "tk_mas", "tk_menos", "tk_mult", "tk_mod", "tk_div", "tk_coma", "tk_par_der", "tk_pyc", "tk_dosp"],token)
def VALOR():
	if (toktoValtok(token)=="tk_par_izq"):
		emparejar("tk_par_izq")
		EXPRESION()
		emparejar("tk_par_der")
	elif (toktoValtok(token)=="id"):
		IDCALL()
	elif (toktoValtok(token)=="tk_entero" or toktoValtok(token) == "tk_real" or toktoValtok(token) == "tk_caracter" or toktoValtok(token) == "tk_cadena"):
		NUMERO_PALABRA()
	elif (toktoValtok(token)=="verdadero" or toktoValtok(token) == "falso"):
		BOOLEANO()
	elif (toktoValtok(token)=="tk_menos"):
		emparejar("tk_menos")
		VALOR()
	elif (toktoValtok(token)=="tk_neg"):
		emparejar("tk_neg")
		VALOR()
	else: 
		errorSintaxis(["tk_par_izq", "id", "tk_entero", "tk_real", "tk_caracter", "tk_cadena", "verdadero", "falso", "tk_menos", "tk_neg"],token)
def NUMERO_PALABRA():
	if (toktoValtok(token)=="tk_entero"):
		emparejar("tk_entero")
	elif (toktoValtok(token)=="tk_real"):
		emparejar("tk_real")
	elif (toktoValtok(token)=="tk_caracter"):
		emparejar("tk_caracter")
	elif (toktoValtok(token)=="tk_cadena"):
		emparejar("tk_cadena")
	else: 
		errorSintaxis(["tk_entero", "tk_real", "tk_caracter", "tk_cadena"],token)
def BOOLEANO():
	if (toktoValtok(token)=="verdadero"):
		emparejar("verdadero")
	elif (toktoValtok(token)=="falso"):
		emparejar("falso")
	else: 
		errorSintaxis(["verdadero", "falso"],token)
def IDCALL():
	if (toktoValtok(token)=="id"):
		emparejar("id")
		IDCALL2()
	else: 
		errorSintaxis(["id"],token)
def IDCALL2():
	if (toktoValtok(token)=="tk_punto"):
		IDESTRUC()
	elif (toktoValtok(token)=="tk_par_izq"):
		CALL()
	elif (toktoValtok(token)=="tk_y" or toktoValtok(token) == "tk_o" or toktoValtok(token) == "tk_igual" or toktoValtok(token) == "tk_dif" or toktoValtok(token) == "tk_menor" or toktoValtok(token) == "tk_mayor" or toktoValtok(token) == "tk_menor_igual" or toktoValtok(token) == "tk_mayor_igual" or toktoValtok(token) == "tk_mas" or toktoValtok(token) == "tk_menos" or toktoValtok(token) == "tk_mult" or toktoValtok(token) == "tk_mod" or toktoValtok(token) == "tk_div" or toktoValtok(token) == "tk_coma" or toktoValtok(token) == "tk_par_der" or toktoValtok(token) == "tk_pyc" or toktoValtok(token) == "tk_dosp"):
		hola()
	else: 
		errorSintaxis(["tk_punto", "tk_par_izq", "tk_y", "tk_o", "tk_igual", "tk_dif", "tk_menor", "tk_mayor", "tk_menor_igual", "tk_mayor_igual", "tk_mas", "tk_menos", "tk_mult", "tk_mod", "tk_div", "tk_coma", "tk_par_der", "tk_pyc", "tk_dosp"],token)
def INSTRUCCIONES_FUNCION():
	if (toktoValtok(token)=="leer"):
		LEER()
		INSTRUCCIONES_FUNCION()
	elif (toktoValtok(token)=="imprimir"):
		IMPRIMIR()
		INSTRUCCIONES_FUNCION()
	elif (toktoValtok(token)=="si"):
		SI()
		INSTRUCCIONES_FUNCION()
	elif (toktoValtok(token)=="mientras"):
		MIENTRAS()
		INSTRUCCIONES_FUNCION()
	elif (toktoValtok(token)=="hacer"):
		HACER_MIENTRAS()
		INSTRUCCIONES_FUNCION()
	elif (toktoValtok(token)=="para"):
		PARA()
		INSTRUCCIONES_FUNCION()
	elif (toktoValtok(token)=="seleccionar"):
		SELECCIONAR()
		INSTRUCCIONES_FUNCION()
	elif (toktoValtok(token)=="booleano" or toktoValtok(token) == "caracter" or toktoValtok(token) == "entero" or toktoValtok(token) == "real" or toktoValtok(token) == "cadena" or toktoValtok(token) == "id"):
		DECLARACION_ASIGNACION()
		INSTRUCCIONES_FUNCION()
	elif (toktoValtok(token)=="romper"):
		ROMPER()
		INSTRUCCIONES_FUNCION()
	elif (toktoValtok(token)=="retornar"):
		hola()
	else: 
		errorSintaxis(["leer", "imprimir", "si", "mientras", "hacer", "para", "seleccionar", "booleano", "caracter", "entero", "real", "cadena", "id", "romper", "retornar"],token)



def main():
	global token
	token = Lexico.next()
	S()
	if(not error):
		if(toktoValtok(token)!="EOF"):
			errorSintaxis(["EOF"],token)
		else:
			print("El analisis sintactico ha finalizado exitosamente.",end="")

def hola():
	a = 2

def ordenar(values):
	ordenado = []
	for key, value in Lista.items():
		for val in values:
			if(key==val):
				ordenado.append(val)
				break
	for reservada in reservadas:
		for val in values:
			if(reservada==val):
				ordenado.append(val)
				break
	return ordenado



Lista = {'tk_mas':"+", 'tk_menos':"-", 'tk_mult':"*", 'tk_div':"/", 'tk_mod':"%", 'tk_asig':"=", 'tk_menor': "<",
            'tk_mayor':">",'<=':"tk_menor_igual",'tk_mayor_igual':">=",'tk_igual':"==",'tk_y':"&&", 'tk_o':"||",
            'tk_dif':"!=",'tk_neg':"!", 'tk_dosp':":", 'tk_pyc':";",'tk_coma':",",'tk_punto':".", 'tk_par_izq':"(",
            'tk_par_der':")",'id':"identificador",'tk_entero':"valor_entero",'tk_real':"valor_real",'tk_caracter':"valor_caracter",
			'tk_cadena':"valor_cadena"}

reservadas = ['funcion_principal', 'fin_principal',
              'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'entonces', 'fin_si', 'si_no', 'mientras', 'hacer', 'fin_mientras', 
              'para', 'fin_para', 'seleccionar', 'entre', 'caso', 'romper', 'defecto', 'fin_seleccionar',
              'estructura', 'fin_estructura', 'funcion','fin_funcion','retornar','falso','verdadero','EOF']

diferenciar = {'tk_mas':"+", 'tk_menos':"-", 'tk_mult':"*", 'tk_div':"/", 'tk_mod':"%", 'tk_asig':"=", 'tk_menor': "<",
            'tk_mayor':">",'<=':"tk_menor_igual",'tk_mayor_igual':">=",'tk_igual':"==",'tk_y':"&&", 'tk_o':"||",
            'tk_dif':"!=",'tk_neg':"!", 'tk_dosp':":", 'tk_pyc':";",'tk_coma':",",'tk_punto':".", 'tk_par_izq':"(",
            'tk_par_der':")"}

valores = {
	'id':"identificador",'tk_entero':"valor_entero",'tk_real':"valor_real",'tk_caracter':"valor_caracter",
			'tk_cadena':"valor_cadena"
}
main()

