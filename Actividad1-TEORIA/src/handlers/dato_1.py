import csv
import json
from collections import Counter
def start():
	"""abro archivo de datos y creo el archivo donde guardar las palabras"""
	arch=open('C:\\Users\\Alumno\\Archivos\\Actividad1-TEORIA\\salud.csv','r',encoding='UTF-8')
	csv_reader=csv.reader(arch,delimiter=',')
	arch_2=open('Provincias.txt','w+')
	next(csv_reader)
	contador={}
	datos=[]
	for linea in csv_reader:
		if not linea[3] in contador:
			contador[linea[3]]=linea[9]
		else:
			contador[linea[3]]=int(contador[linea[3]])+ int(linea[9])
	cont=dict(Counter(contador).most_common(15))
	for i in cont:
		datos.append(i)
	json.dump(datos,arch_2)
	arch.close()
	arch_2.close()