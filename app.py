from flask import Flask, redirect, render_template, url_for, request, flash, session, Blueprint

from controller.catalogue import catalogue
from modelo.usuario import Usuarios
from modelo import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ferfong:Develooper123!@localhost:3306/merkApp'
app.config.from_mapping(
    SECRET_KEY='dev'
)

db.init_app(app)


@app.route('/')
def inicioSesion():
    return redirect(url_for('login'))


@app.route('/tonto', methods=['GET', 'POST'])
def login():
    if session.get('user_id') != None:
        return render_template('login.html', user=session['user_id'])
    if request.method == 'GET':
        return render_template('index.html')
    
    name = request.form.get('username')
    passwd = request.form.get('password')
    
    for registro in Usuarios.query.all():
            if name == registro.username and passwd == registro.password:
                session['user_id'] = name #definición de cookie de sesión.
                return render_template('login.html', user=name)
            else:
                flash("ERROR: nombre de usuario o contraseña incorrectos")

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['user_id'] = None
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
