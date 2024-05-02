# https://stackoverflow.com/questions/73309491/port-xxxx-is-in-use-by-another-program-either-identify-and-stop-that-program-o
# https://stackoverflow.com/questions/68012921/i-get-options-method-instead-of-post-in-flask
# https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
from flask import Flask, redirect, render_template, url_for, request, flash, session, Blueprint

import json

from flask import Flask, redirect, render_template, url_for, request, flash, session, Response
from flask_cors import CORS

from alchemyClasses import db
from controller.catalogue import catalogue
from controller.UsuarioControlador import usuario_blueprint
from alchemyClasses.Usuario import Usuario

app = Flask(__name__)
app.register_blueprint(catalogue)
app.register_blueprint(usuario_blueprint)
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ing:Developer123!@localhost:3306/usuario'
db.init_app(app)
CORS(app)

@app.route('/')
def inicioSesion():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST', 'OPTIONS'])
def login(): 
    #print(f'\n{request.method}\n')    
    if request.method == 'OPTIONS':           
        res = Response()        
        res.headers['X-Content-Type-Options'] = '*'
        return res
    if session.get('user_id') != None:
        return render_template('login.html', user=session['user_id'])    
    if request.method == 'GET':        
        return render_template('index.html')
    boton = request.form.get('registrar')
    #print(boton)
    if boton == 'registrar':
        return redirect(url_for('usuario.registrar_usuario'))
    if request.method == 'POST':   
        #print(request.json)          
        #print()
        #nombre = request.form.get('username')
        #contrasenia = request.form.get('password')
                
        nombre = request.json['nombre']
        contrasenia = request.json['contrasenia']        
        #print(f'\n{nombre}\n')
        #print(contrasenia)
    
        # for registro in Usuario.query.all():
        #     if nombre == registro.nombre and contrasenia == registro.password:
        #         flash("ERROR: Pon otro nombre!")
        #usuario = Usuario(id, nombre, contrasenia)
        encontrado = Usuario.query.filter(Usuario.nombre == nombre, Usuario.contrasenia == contrasenia).first()
        #db.session.add(usuario)        
        #db.session.commit()                
        #print(f'\n{encontrado}\n')    
        if encontrado: #Ustedes van a tener que cambiar esto, por una validación con la DB.
            session['user_id'] = nombre #definición de cookie de sesión.
            #return render_template('login.html', user=nombre)                
            return json.dumps({'nombre': nombre, 'contrasenia': contrasenia})
        flash('Invalid username or password')
        #return redirect(url_for('login'))
        return json.dumps({'error':'Invalid username or password'})


@app.route('/logout')
def logout():
    session['user_id'] = None
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
