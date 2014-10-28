import Operaciones
cl_Operaciones = Operaciones.Operando

#encabezado
print ("Juan Luis Suchi Martinez   200818843")
print ("******************  Practica 1  *********************")

def leerArchivo():
    #Se verifica el que exista el archivo
	try:
		f = open('archivo.txt',w)
	except:
		print('El archivo seleccionado no existe')			
print('Ingrese Cadena de entrada:') # Se pide que ingrese la cadena de entrada """


cadena_entrada = input() # Se obtiene la cadena de entrada """
if cadena_entrada != "a":
	#print(cadena_entrada)
	lista = cadena_entrada.split(" ")   
	if len(lista) == 5:  # la cadena de entrada solo debe tener 5 parametros
		VarX = lista[0]
		VarY = lista[1]
		cl_Operaciones.leerArchivoY(VarY)
		cl_Operaciones.leerAchivoX(VarX)
		#print(cl_Operaciones.filasX)
		alfa = lista[2]
		iteraciones = lista[3]
		tolerancia = lista[4]
		#print(VarX + ' ' + VarY+' '+alfa+' '+ iteraciones+' '+tolerancia+' ')
	else:
		print('La cadena de entrada debe tener 5 parametros')
		
