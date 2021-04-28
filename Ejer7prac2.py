nombres="""'Agustin','Alan','Andrés','Ariadna','Bautista','CAROLINA','CESAR','David','Diego','Dolores','DYLAN','ELIANA','Emanuel','Fabián','Facundo','Facundo','FEDERICO','FEDERICO','GONZALO','Gregorio','Ignacio','Jonathan','Jonathan','Jorge','JOSE','JUAN','Juan','Juan','Julian','Julieta','LAUTARO','Leonel','LUIS','Luis','Marcos','María','MATEO','Matias','Nicolás','NICOLÁS','Noelia','Pablo','Priscila','TOMAS','Tomás','Ulises','Yanina'"""
notas1="""81,60,72,24,15,91,12,70,29,42,16,3,35,67,10,57,11,69,12,77,13,86,48,65,51,41,87,43,10,87,91,15,44,85,73,37,42,95,18,7,74,60,9,65,93,63,74"""
notas2="""30,95,28,84,84,43,66,51,4,11,58,10,13,34,96,71,86,37,64,13,8,87,14,14,49,27,55,69,77,59,57,40,96,24,30,73,95,19,47,15,31,39,15,74,33,57,10"""
nombres=nombres.replace("'","")
nombres=nombres.replace(" ","")
nombres=nombres.split(",")
notas1=notas1.split(",")
notas2=notas2.split(",")
alumnos={}
notas1 = list(map(lambda x: int(x), notas1))
notas2 = list(map(lambda x: int(x), notas2))
pares_notas=list(zip(notas1,notas2))
nota_final=list(map(lambda x: x[0] + x[1],pares_notas))
suma=0
i=0
for i in nota_final:   #Sumo todos los valores para después sacar el promedio
    suma=suma + i
prom=0 if len(alumnos)==0 else suma / len(alumnos)
for i in range(len(alumnos)):  #Informa quienes obtuvieron nota menor al promedio
    if(alumnos[nombres[i]]<prom):
        print("El alumno:" + nombres[i] + " obtuvo una nota menor al promedio")


