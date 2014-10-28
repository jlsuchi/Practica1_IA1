import Operaciones
import Operando
import random

#Variables
cl_Operacion = Operaciones.Operaciones 
n = 0
m = 0
sumatoria = 0
Listado_Tetas = []

#Encabezado
print ("Juan Luis Suchi Martinez   200818843")
print ("******************  Practica 1  *********************")
print('Ingrese Cadena de entrada:') # Se pide que ingrese la cadena de entrada """

cadena = input() # obtiene la cadena ingresada



def suma():
	operacion = 0
	i = 0
	while i < m:
		for j in range(n):
			# Se operan las X y se actualiza el valor de teta
			operacion = operacion + Listado_Tetas[j]*cl_Operacion.matrizX[i][j]
			#print(operacion)
		operacion = operacion - cl_Operacion.listaY[i]# aqui restamos a y 
		operacion = operacion*operacion # aqui elevamos al cuadrado 
		#print(operacion) # y en teoria ya esta entonces estos tengo que sumarlos todos para dividirlo por 1/2m
		operacion = (1/(2*m)) * operacion
		i = i+1
	print(operacion)
	cl_Operacion.operacionA = cl_Operacion.operacion
	cl_Operacion.operacion = operacion
	
#----------------------------------------------	
def gradiente(Valor):
	#hacemos lo del gradiente y le voy poniendo nuevos valores a las tetas
	for j in range(n):
		Listado_Tetas[j] = Listado_Tetas[j]-Valor*cl_Operacion.operacion
		
if cadena != "a":
	lista = cadena.split(" ")
	if len(lista) == 5:
		VarX = lista[0]  
		VarY = lista[1]
		cl_Operacion.leerArchivoY(VarY)
		cl_Operacion.leerAchivoX(VarX)  #print(cl_Operacion.filasX)
		print ("\n")
		alfa = float(lista[2])
		iteraciones = float(lista[3])
		tolerancia = float(lista[4])
		n = cl_Operacion.cantidadX 
		m = cl_Operacion.filasX
		i = 0
		while i<= n: #Se delimito Teta por cada x, en la matriz	
			Listado_Tetas.append(random.uniform(0,1))
			i = i + 1
		
		#--------------- Se operan los archivos --------------------------
		archivo=open('Archivo.csv','a')
		archivo.write('iteracion, costo \n')
		w = 0
		while w < iteraciones:
			suma()
			gradiente(alfa)
			if tolerancia >= (cl_Operacion.operacion - cl_Operacion.operacionA): #Tolerancia se compara con la de costo del valor anterior
				break
			else:
				#Se escribe en el archivo			
				archivo.write(str(w)+','+str(cl_Operacion.operacion)+'\n')							
			w=w+1
		archivo.close()
		#Se imprime los valores finales de teta
		print ("\n")
		for g in range(n):
			print('Valor de Teta'+str(g)+':'+str(Listado_Tetas[g]))
			#print('Valor'+str(g)+':'+str(Listado_Tetas[z]))
	else:
		print("La cadena de entrada es incorrecta, debe ingresar 5 parametros")
