#!/bin/python

from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner 
from kivy.uix.textinput import TextInput 

from kivy.uix.button import Button

class Ventana(ScreenManager):
	def cambiar(self):
		self.ids.nombre.text = " estamos en el flisol panama con kivy"
		#print (" estoy funcionando dese python")
class Flisol(GridLayout):
	def __init__(self, **kwargs):
		super(Flisol,self).__init__(**kwargs)
		self.cols = 4
		self.crear()
	def crear(self):
		for num in xrange(1,5):
			ref = ""+str(num)
			idNom="Nom"+ref	
			idSpi="So"+ref

			lb = Label(text=" Nombre #"+ref)
			ti = TextInput(id="idNom",text="flisol"+ref)

			lb2= Label(text="Sistema Operativo:")
			valor= ["Linux","Mac","Windows","Movil"]

			sp= Spinner(id=idSpi, text="elija", values=valor)
			self.add_widget(lb)
			self.add_widget(ti)
			self.add_widget(lb2)
			self.add_widget(sp)	
		bt =Button(text=" GENERAR")
		bt.bind(on_press= self.generar)
		self.add_widget(bt)
	def generar(self, obj):
		print (" buton precionado")

class MainApp(App):	
	def build(self):
		return Ventana()

if __name__ == "__main__":
	MainApp().run()	