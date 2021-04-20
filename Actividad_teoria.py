import csv
from collections import Counter
arch=open('appstore_games.csv','r')
csv_reader=csv.reader(arch,delimiter=',')
next(csv_reader)
rating={}
for linea in csv_reader:
    if linea[7]=="0" and "ES" in linea[12]:
        print(linea)
    rating[linea[2]] = (linea[6],linea[4]) 
mayor_rating=dict(Counter(rating).most_common(10))
print("Links a los iconos de los 10 juegos con más calificaciones de usuarios")
for i in mayor_rating:
    print("URL de juego: ",i,mayor_rating[i][1])
arch.close()
