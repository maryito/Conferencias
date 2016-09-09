#!/bin/python
#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.boxlayout import  BoxLayout
from kivy.uix.gridlayout import GridLayout


class Ventana(BoxLayout):
	#Inicializamos nuestro ventana
	def __init__(self, **kwargs):
		super(Ventana, self).__init__(**kwargs)
		# asignamos la orientacion a nuestra ventana		
		self.orientation ="vertical"	
		#hacemos el llamado a la funcion crear 
		self.crear()

	def crear(self):
		#limpiamos nuestra ventana
		self.clear_widgets()	
		# Creamos un Label		
		lb = Label(text= "hola mundo ")	

		#Creamos un botones
		bt = Button(text="Presioname")		
		bt2 = Button(text= "cambiar gui")

		#Asignamos los evento a los botones
		bt.bind(on_press =self.ev_boton)
		bt2.bind(on_press = self.ev_nuevodise)

		# Agregamos los objectos a nuestra Ventana
		self.add_widget(lb)
		self.add_widget(bt)
		self.add_widget(bt2)

	def ev_boton(self, obj):
		print(" generando evento :) del nom objeto:"+obj.text)

	def ev_nuevodise(self, obj):
		self.clear_widgets()
		contendor = GridLayout(cl=3,rows=2, padding= 20, spacing= 10)
		for num in range (0,10):
			ref = "ref"+str(num)
			boton=Button( text= "Boton dinamico #"+str(num), id=ref)
			boton.bind(on_press= self.ev_bt_dinamico) 
			contendor.add_widget(boton)	
		atras = Button(text= "Regresas menu principal")
		atras.bind(on_press = self.ev_gui_inicio)

		self.add_widget(contendor)
		self.add_widget(atras)

	def ev_gui_inicio(self, obj):
		self.crear(
)
	def ev_bt_dinamico(self, obj):
		print ("id: "+obj.id, "valor: "+obj.text)
		obj.text = "cambiado x evt: "+obj.id

class Inicio2(App):
	def build(self):
		return Ventana()

if __name__ =="__main__":
	Inicio2().run()