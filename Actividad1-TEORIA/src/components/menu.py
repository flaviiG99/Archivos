import PySimpleGUI as sg 
from src.windows import menu
from src.handlers import dato_1 as dato1
from src.handlers import dato_2 as dato2
def start():
	"""ejecucion de la ventana del menú"""
	window=loop()
	window.close()
def loop():
	"""loop de la ventana"""
	window=menu.build()
	while True:
		event,values=window.read()
		if event in ("Salir","-exit-"):
			break
		if event=="-dato1-":
			window.hide()
			dato1.start()
			sg.Popup("Se obtuvieron las 15 provincias con más casos de infecciones respiratorias <<resultado en archivo 'provincias'>>",no_titlebar=True)
			window.un_hide()
		if event=="-dato2-":
			window.hide()
			dato2.start()
			sg.Popup("Se obtuvieron las 20 marcas que más utilizan nafta <<resultado en archivo 'Marcas'>>",no_titlebar=True)
			window.un_hide()
	return window