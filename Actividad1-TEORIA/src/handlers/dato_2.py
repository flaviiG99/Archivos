import json
import csv
from collections import Counter
def start():  
	"""Abro archivo de datos y creo archivo que va a tener las palabras.
	Se obtendrán las 20 marcas de vehiculos que más utilizan nafta"""
	archivo=open('Vehiculos.csv','r+')
	csv_reader=csv.reader(archivo,delimiter=';')
	next(csv_reader)
	archivo_2=open('Marcas.txt','w+')
	contador={}
	for linea in csv_reader:
		if linea[7]=="NAFTA":
			if not linea[0] in contador:
				contador[linea[0]]=1
			else:
				contador[linea[0]]+=1
	cont=dict(Counter(contador).most_common(20))
	datos=[]
	for i in cont:
		datos.append(i)
	json.dump(datos,archivo_2)
	archivo.close()
	archivo_2.close()