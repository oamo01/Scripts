#!/usr/bin/env python

import minimalmodbus
import os
import time

def Menu():
	os.system('clear')
	print "1] Leer frecuencia"
	print "2] Escribir frecuencia"
	print "3] Salir"

	opcionMenu = input("Inserta un valor")

	if opcionMenu==1:
		os.system('clear')
		LeerFrecuencia(291)
		Arrancar()
		Menu()	
	elif opcionMenu==2:
		os.system('clear')
		print 'Escribe la frecuencia deseada (0 a 60)'
		F=input()
		EscribirFrecuencia(258,F*10)
		Menu()
	elif opcionMenu==3:
		quit ()
	else:
		Menu()

#	def Inicio(port, nodo):
#	print variador
#	Activar()

def LeerFrecuencia(registro):
	Activar()
	loop=1
	while loop == 1:
		leer_frec = variador.read_register(registro, 2) # Registernumber, number of decimals
		time.sleep(1)	

def EscribirFrecuencia(registro,frecuencia):
	variador.write_register(registro,frecuencia) 
	Desactivar()

def Activar():
	variador.write_register(9,2) #Parametro b000=0002
	variador.write_register(15,4) #Parametro b004=0004
	variador.write_register(125,2) #Parametro A164=0002

def Desactivar():
	variador.write_register(15,0) #Parametro b004=0000
	variador.write_register(9,0) #Parametro b000=0000
	variador.write_register(125,3) #Parametro A164=0003

def Arrancar():
	variador.write_register(257,1,0) #Arrancar


port='/dev/ttyUSB0'
nodo=2
variador = minimalmodbus.Instrument(port, nodo)	
print variador
Menu()

