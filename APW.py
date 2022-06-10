#Importamos las librerias
from flask import Flask, redirect, render_template, request, url_for
#Intanciar la aplicacion
app = Flask(__name__)

#Array donde almacenaremos los datos
lista_contactos = []

#Decorador para definir la ruta inicio
@app.route('/')
def index():
    return render_template('index.html')

#Decorador para definir la ruta contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html', lista_contactos = lista_contactos)

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

#Decorador para definir la ruta Soluciones de almacenamiento
@app.route('/listaContacto')
def listaContacto():
    return render_template('listaContacto.html', lista_contactos = lista_contactos)

#Controlador de la ruta de envio de datos
@app.route('/enviarContacto', methods=['POST'])                             
def enviarContacto():                                                       #crea la funcion enviar
    if request.method == 'POST':                                            #Condicion que solicita que el metodo sea igual a post
        ingreso_nombre = request.form['ingreso_nombre']                     #Extrae los datos ingresados en el input de la descripcion de la tarea
        ingreso_apellido = request.form['ingreso_apellido']                 #Extrae los datos ingresados en el input del correo electronico
        ingreso_correo = request.form['ingreso_correo']                     #Extrae los datos ingresados en el input de la prioridad
        ingreso_telefono = request.form['ingreso_telefono']                 #Extrae los datos ingresados en el input de la prioridad
        ingreso_motivacion = request.form['ingreso_motivacion']             #Extrae los datos ingresados en el input de la prioridad
        #Crea la condicion de que no guarde el registro cuando el campo de la tarea y el del correo estan vacios
        if ingreso_nombre == '' or ingreso_apellido == '' or ingreso_correo == '' or ingreso_telefono == '' or ingreso_motivacion == '':            
            return redirect(url_for('contacto'))                       
        else:
            #Agrega a la lista los campos llenos
            lista_contactos.append({'ingreso_nombre': ingreso_nombre, 'ingreso_apellido': ingreso_apellido, 'ingreso_correo': ingreso_correo, 'ingreso_telefono': ingreso_telefono, 'ingreso_motivacion': ingreso_motivacion })
            return redirect(url_for('contacto'))

#main del programa
if __name__ == '__main__':
    app.run(debug=True)     #debug para reiniciar el servidor