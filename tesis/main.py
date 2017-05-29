from flask import Flask
from flask import render_template
from flask import request
import forms
import minimalmodbus

#port='/dev/ttyUSB0'
#nodo=2
#variador = minimalmodbus.Instrument(port, nodo)	

def Activar():
	variador.write_register(9,2) #Parametro b000=0002
	variador.write_register(15,4) #Parametro b004=0004
	variador.write_register(125,2) #Parametro A164=0002

def Desactivar():
	variador.write_register(15,0) #Parametro b004=0000
	variador.write_register(9,0) #Parametro b000=0000
	variador.write_register(125,3) #Parametro A164=0003

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
	variador.write_register(registro,frecuencia) 
	Desactivar()




app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
	comment_form = forms.CommentForm(request.form)
	if request.method == 'POST' and comment_form.validate():
		a = comment_form.username.data
		print a
		f = Conversion(a)
		print f
		#EscribirFrecuencia(258,f)

		

	
	title = "LABINTAHP"
	return render_template('index.html', title = title, form = comment_form )

if __name__ == '__main__':
	app.run(debug = True, port=8000)
#	app.run(debug = True, host=10.8.0.10, port=8000)

