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



#main del programa
if __name__ == '__main__':
    app.run(debug=True)     #debug para reiniciar el servidor