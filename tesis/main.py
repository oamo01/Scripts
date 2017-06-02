from flask import Flask
from flask import render_template
from flask import request
import forms
import minimalmodbus
import time



port='/dev/tty.wchusbserial14220'
nodo=2
variador = minimalmodbus.Instrument(port, nodo)
variador

def Activar():
	variador
#	time.sleep(1)
	variador.write_register(9,2) #Parametro b000=0002
	variador
	variador.write_register(15,4) #Parametro b004=0004
#	time.sleep(1)
	variador
#	variador.write_register(125,2) #Parametro A164=0002

def Desactivar():
#	time.sleep(1)
	variador
	variador.write_register(9,0) #Parametro b000=0000
	variador
#	time.sleep(1)
	variador.write_register(15,0) #Parametro b004=0000
#	variador.write_register(125,3) #Parametro A164=0003

def Arrancar():
	variador.write_register(257,1,0) #

def Conversion(flujo):
	c=60
	b=5.02
	d=(flujo*c)/b
	e=round(d,2)
	f= e*100
	g= int(f)
	return g

def EscribirFrecuencia(registro,frecuencia):
	Activar()
	time.sleep(1)
	variador.write_register(registro,frecuencia) 
	time.sleep(1)
	Desactivar()




app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
	comment_form = forms.CommentForm(request.form)
	if request.method == 'POST' and comment_form.validate():
		variador
		a = comment_form.username.data
		f = Conversion(a)
		EscribirFrecuencia(258,f)

		

	
	title = "LABINTAHP"
	return render_template('index.html', title = title, form = comment_form )

if __name__ == '__main__':
	app.run(debug = True, port=8000)
#	app.run(debug = True, host=10.8.0.10, port=8000)

