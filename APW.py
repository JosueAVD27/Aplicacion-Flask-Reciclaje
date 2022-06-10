#Importamos las librerias
from flask import Flask, render_template
#Intanciar la aplicacion
app = Flask(__name__)

#Decorador para definir la ruta inicio
@app.route('/')
def index():
    return render_template('index.html')

#Decorador para definir la ruta contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

#Decorador para definir la ruta noticias
@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

#Decorador para definir la ruta sugerencias
@app.route('/sugerencias')
def sugerencias():
    return render_template('sugerencias.html')

#Decorador para definir la ruta reciclaje
@app.route('/reciclaje')
def reciclaje():
    return render_template('reciclaje.html')

#Decorador para definir la ruta Proteccion del medioambiente
@app.route('/proteccionmedio')
def proteccionmedio():
    return render_template('proteccionmedio.html')

#Decorador para definir la ruta reutilizacion de recursos
@app.route('/reutilizacionrecurso')
def reutilizacionrecurso():
    return render_template('reutilizacionrecurso.html')

#Decorador para definir la ruta Responsabilidad social
@app.route('/responsabilidadsocial')
def responsabilidadsocial():
    return render_template('responsabilidadsocial.html')

#Decorador para definir la ruta Soluciones de almacenamiento
@app.route('/solucionesalmacenamiento')
def solucionesalmacenamiento():
    return render_template('solucionesalmacenamiento.html')

        

#main del programa
if __name__ == '__main__':
    app.run(debug=True)     #debug para reiniciar el servidor