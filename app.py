from flask import Flask, redirect, render_template, url_for, request, flash, session

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

@app.route('/')
def hello_world():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():    
    if session.get('user_id') != None:
        return render_template('login.html', user=session['user_id'])    
    if request.method == 'GET':        
        return render_template('index.html')
    boton = request.form.get('registrar')
    print(boton)
    if boton == 'registrar':
        return redirect(url_for('usuario.registrar_usuario'))
    nombre = request.form.get('username')
    contrasenia = request.form.get('password')
    print(nombre)
    print(contrasenia)
    id = 1
    for registro in Usuario.query.all():
        id += 1
        if nombre == registro.nombre:
            flash("ERROR: Pon otro nombre!")
    usuario = Usuario(id, nombre, contrasenia)
    db.session.add(usuario)        
    db.session.commit()        
    encontrado = Usuario.query.filter(Usuario.nombre == nombre, Usuario.contrasenia == contrasenia).first()
    if encontrado != None: #Ustedes van a tener que cambiar esto, por una validación con la DB.
        session['user_id'] = nombre #definición de cookie de sesión.
        return render_template('login.html', user=nombre)                
    flash('Invalid username or password')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['user_id'] = None
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
