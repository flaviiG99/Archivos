import PySimpleGUI as sg 
def build():
	"""layout de la ventana del menu"""
	tam=(40,2)
	Layout=[[sg.Text(" "*25+"¿Qué datos analizamos?")],[sg.Button("Vigilancia de infecciones respiratorias agudas",key="-dato1-",size=tam)],[sg.Button("Datos vehiculares",key="-dato2-",size=tam)],[sg.Text(" ")],[sg.Button("Salir",key="-exit-",size=tam)]]
	window=sg.Window('',layout=Layout,no_titlebar=True)
	return window
