class Operaciones:
	
	#Variables
	
	filasX = 0
	matrizX = []
	cantidadX = 0
	listaY = []
	operacion = 0
	operacionA = 0
	
	#"""      Metodo 1          """
	def leerArchivosP(archivo):
		contador1= 0
		
   # """           Metodo2                 """
	def leerArchivoY(archivo1):
	   #  se utiliza una lista, para la variable x
		archivoY=open(archivo1,'r')
		lineaY=archivoY.readline() 		
		while lineaY!="":			
			#print(lineaY)    se imprimen los valores del archivo Y
			lineaY = lineaY.replace("\n", "")
			Operaciones.listaY.append(float(lineaY))
			lineaY=archivoY.readline()			
		archivoY.close()
		# se obtiene el valor de X, se llena la primera matriz
		Operaciones.filasX = len(Operaciones.listaY)

   # """       Metodo 3     """
	def leerAchivoX(archivo):
		contador = 0
		# Se crea una matriz
		Operaciones.matrizX = [] 
		try:
			archivoX=open(archivo,'r')
			linea=archivoX.readline()
			linea = linea.replace("\n", "")
			listaTX = linea.split(",") 
			# Se obtiene el numero de columnas den X
			Operaciones.cantidadX = len(listaTX) 
			for i in range(Operaciones.filasX):
				Operaciones.matrizX.append([])
				for j in range(Operaciones.cantidadX):
					Operaciones.matrizX[i].append(None)
					
	         # Se inserta en la matriz
			i = 0;
			for x in listaTX:								
				Operaciones.matrizX[0][i] = float(x)
				i = i + 1
			#---------------------------------------------------------		
			while linea!="":
				contador = contador + 1    #print(linea)   se imprime los valores del archivo xs
				linea=archivoX.readline()
				linea = linea.replace("\n", "")
				listaTX = linea.split(",")
				# Se inserta en la matriz
				i = 0;
				if contador < Operaciones.filasX:
					for x in listaTX:								
						Operaciones.matrizX[contador][i] = float(x)
						i = i + 1
			archivoX.close()
		except:
			print('El archivo seleccionado es invalido'+ archivo)			
		
