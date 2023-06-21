#Importamos las librerias
from flask import Flask, redirect, render_template, request, url_for, session
#from django.shortcuts import render
#from django.contrib.auth.forms import UserChangeForm
#Intanciar la aplicacion
app = Flask(__name__)

app.secret_key = 'your_secret_key'

#Array donde almacenaremos los datos
lista_contactos = []
lista_sugerencias = []

#Decorador para definir la ruta inicio
@app.route('/')
#Crea la funcion para llamar a la pagina de inicio
def index():
    return render_template('index.html')

#Decorador para definir la ruta contacto
@app.route('/contacto')
#Crea la funcion para llamar a la pagina de contacto
def contacto():
    return render_template('contacto.html', lista_contactos = lista_contactos)

#Decorador para definir la ruta noticias
@app.route('/noticias')
#Crea la funcion para llamar a la pagina de noticias
def noticias():
    return render_template('noticias.html')

#Decorador para definir la ruta sugerencias
@app.route('/sugerencias')
#Crea la funcion para llamar a la pagina de sugerencias
def sugerencias():
    return render_template('sugerencias.html', lista_sugerencias = lista_sugerencias)

#Decorador para definir la ruta reciclaje
@app.route('/reciclaje')
#Crea la funcion para llamar a la pagina de reciclaje
def reciclaje():
    return render_template('reciclaje.html')

#Decorador para definir la ruta Proteccion del medioambiente
@app.route('/proteccionmedio')
#Crea la funcion para llamar a la pagina de proteccion medioambiente
def proteccionmedio():
    return render_template('proteccionmedio.html')

#Decorador para definir la ruta reutilizacion de recursos
@app.route('/reutilizacionrecurso')
#Crea la funcion para llamar a la pagina de reutilizacion de recursos
def reutilizacionrecurso():
    return render_template('reutilizacionrecurso.html')

#Decorador para definir la ruta Responsabilidad social
@app.route('/responsabilidadsocial')
#Crea la funcion para llamar a la pagina de responsabilidades sociales
def responsabilidadsocial():
    return render_template('responsabilidadsocial.html')

#Decorador para definir la ruta Soluciones de almacenamiento
@app.route('/solucionesalmacenamiento')
#Crea la funcion para llamar a la pagina de soluciones almacenamiento
def solucionesalmacenamiento():
    return render_template('solucionesalmacenamiento.html')

#Decorador para definir la ruta de la lista de contactos
@app.route('/admin')
#Crea la funcion para llamar a la pagina de administrador
def admin():
    if 'logged_in' in session and session['logged_in']:
        return render_template('admin.html', lista_contactos = lista_contactos, lista_sugerencias = lista_sugerencias)
    else:
        return redirect(url_for('login'))

#Decorador para definir la ruta Soluciones de almacenamiento
@app.route('/login')
#Crea la funcion para llamar a la pagina del login
def login():
    return render_template('login.html')

#Controlador de la ruta para borrar los datos de la tabla
@app.route('/ingresar', methods=['POST'])
#Crea la funcion para el ingreso del login de administrador
def ingresar():
    """ Crea la fincion ingresar()
            Parametros
            --------------------------------------
            usuario : str
                admin@gmail.com
            contrasenia : str
                admin
            login_correo : str
            login_contrasenia : str
            
            Retorna
            --------------------------------------
            redireccion : admin
                redirecciona a la pagina de admin
            
            redireccion : login
                redirecciona a la pagina de login
        """ 
    usuario = 'admin@gmail.com'
    contrasenia = 'admin'
    if request.method == 'POST':
        login_correo = request.form['login_correo'] 
        login_contrasenia = request.form['login_contrasenia']  
        if login_correo == usuario and login_contrasenia == contrasenia:
            # Comienza la sesion con el nombre de usuario
            session['logged_in'] = True
            session['login_correo'] = login_correo
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('login'))



#Controlador de la ruta de envio de datos
@app.route('/enviarContacto', methods=['POST']) 
               
def enviarContacto(): 
    """ Crea la fincion enviarContacto()
            Parametros
            --------------------------------------
            ingreso_nombre : str
            ingreso_apellido : str
            ingreso_correo : str
            ingreso_telefono : num 
            ingreso_motivacion : str
            
            Retorna
            --------------------------------------
            redireccion : contacto
                redirecciona a la pagina de contacto
            
            str
                envia la informacion a el formulario de destino
            redireccion : contacto
                redirecciona a la pagina de contacto
        """                                                      
    if request.method == 'POST':                                            
        ingreso_nombre = request.form['ingreso_nombre']                     
        ingreso_apellido = request.form['ingreso_apellido']                 
        ingreso_correo = request.form['ingreso_correo']              
        ingreso_telefono = request.form['ingreso_telefono'] 
        ingreso_motivacion = request.form['ingreso_motivacion']      
        #Crea la condicion de que no guarde el registro cuando los campos estan vacios
        if ingreso_nombre == '' or ingreso_apellido == '' or ingreso_correo == '' or ingreso_telefono == '' or ingreso_motivacion == '':            
            return redirect(url_for('contacto'))                       
        else:
            #Agrega a la lista los campos llenos
            lista_contactos.append({'ingreso_nombre': ingreso_nombre, 'ingreso_apellido': ingreso_apellido, 'ingreso_correo': ingreso_correo, 'ingreso_telefono': ingreso_telefono, 'ingreso_motivacion': ingreso_motivacion })
            #messagebox.showinfo('Titulo', 'Informacion')
            return redirect(url_for('contacto'))


#Controlador de la ruta para borrar los datos de la tabla
@app.route('/borrar', methods=['POST'])
def borrar():
    """ Borra la lista de los contactos()
            Parametros
            --------------------------------------
            lista_contactos : str
            
            Retorna
            --------------------------------------
            redireccion : admin
                redirecciona a la pagina de admin
            
            clear
                limpia la lista de contactos
        """
    if request.method == 'POST':                      
        if lista_contactos == []:                         
            return redirect(url_for('admin'))               
        else:
            lista_contactos.clear()                           
            return redirect(url_for('admin'))         


#Controlador de la ruta de envio de datos
@app.route('/enviarSugerencia', methods=['POST']) 
               
def enviarSugerencia(): 
    """ Crea la fincion enviarSugerencia()
            Parametros
            --------------------------------------
            ingreso_nombres : str
            ingreso_correo_S : str
            sugerencias : str
            
            Retorna
            --------------------------------------
            redireccion : sugerencias
                redirecciona a la pagina de sugerencias
            
            str
                envia la informacion a el formulario de destino
            redireccion : sugerencias
                redirecciona a la pagina de sugerencias
        """                                                      
    if request.method == 'POST':                                            
        ingreso_nombres = request.form['ingreso_nombres']                     
        ingreso_correo_S = request.form['ingreso_correo_S']                 
        sugerencias = request.form['sugerencias']                   
        #Crea la condicion de que no guarde el registro cuando los campos estan vacios
        if ingreso_nombres == '' or ingreso_correo_S == '' or sugerencias == '':            
            return redirect(url_for('sugerencias'))                       
        else:
            #Agrega a la lista los campos llenos
            lista_sugerencias.append({'ingreso_nombres': ingreso_nombres, 'ingreso_correo_S': ingreso_correo_S, 'sugerencias': sugerencias})
            return redirect(url_for('sugerencias'))

#Controlador de la ruta para borrar los datos de la tabla
@app.route('/borrar2', methods=['POST'])
def borrar2():
    """ Borra la lista de los sugerencias()
            Parametros
            --------------------------------------
            lista_sugerencias : str
            
            Retorna
            --------------------------------------
            redireccion : admin
                redirecciona a la pagina de admin
            
            clear
                limpia la lista de contactos
        """
    if request.method == 'POST':                      
        if lista_sugerencias == []:                         
            return redirect(url_for('admin'))               
        else:
            lista_sugerencias.clear()                           
            return redirect(url_for('admin'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

#main del programa
if __name__ == '__main__':
    app.run(debug=True)     #debug para reiniciar el servidor