import re
from flask import Blueprint, request, render_template, flash, url_for
from modelo import db
# from alchemyClasses.Usuarios import Usuarios
# from alchemyClasses.Rentar import Rentar

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/')
def ver_acciones():
    return render_template('usuario.html')

@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():

    if request.method == 'GET':
        return render_template('agrega_usuario.html')
    else:
        nombre = request.form['nombre']
        apPat = request.form['apPat']
        apMat = request.form['apMat']
        password = request.form['password']
        email = request.form['email']
        profilePicture = request.form['profilePicture']
        profilePicture = bytes(profilePicture, 'utf8')
        id = 1
        for registro in Usuarios.query.all():
            id += 1
            if email == registro.email:
                flash("ERROR: Pon otro correo!")
                return render_template('agrega_usuario.html')
        usuario = Usuarios(id, nombre, apPat, apMat, password, email, profilePicture, None)
        db.session.add(usuario)
        db.session.commit()
        return render_template('usuario_agregado.html', nombre=nombre, apPat=apPat)

@usuario_blueprint.route('/actualizar', methods=['GET', 'POST'])
def actualizar_usuario():
    if request.method == 'GET':
        return render_template('actualiza_usuario.html')
    else:
        email = request.form['email']
        password = request.form['password']
        opciones = request.form['opciones']
        opcion = request.form['opcion']
        usuario = Usuarios.query.filter(Usuarios.email == email, Usuarios.password == password).first()
        if usuario == None :
            flash("ERROR: Usuario no encontrado")
            return render_template('actualiza_usuario.html')
        db.session.delete(usuario)
        if opciones == 'opcion1':
            if len(opcion) <= 200:
                usuario.nombre = opcion
            else:
                flash("ERROR: Pon un nombre válido!")
                return render_template('actualiza_usuario.html')
        elif opciones == 'opcion2':
            if len(opcion) <= 200:
                usuario.apPat = opcion
            else:
                flash("ERROR: Pon un apellido paterno válido!")
                return render_template('actualiza_usuario.html')
        elif opciones == 'opcion3':
            usuario.apMat = opcion
        elif opciones == 'opcion4':
            if len(opcion) <= 64:
                usuario.password = opcion
            else:
                flash("ERROR: Pon un password válido!")
                return render_template('actualiza_usuario.html')
        elif opciones == 'opcion5':
            if len(opcion) <= 500 and re.match(opcion, r'^[\w\.-]+@[\w\.-]+\.\w+$)'):
                usuario.email = opcion
            else:
                flash("ERROR: Pon un correo electrónico válido!")
                return render_template('actualiza_usuario.html')
        elif opciones == 'opcion6':
            if opcion == 1 or opcion == 0:
                usuario.superUser = opcion
            else:
                flash("ERROR: Pon 0, si el usuario no es super usuario, pon 1 si quieres que sea super usuario")
                return render_template('actualiza_usuario.html')
        db.session.add(usuario)
        db.session.commit()
        return render_template('usuario_actualizado.html', nombre=usuario.nombre)

def actualizar_ids():
    id = 1
    for registro in Usuarios.query.all():
        registro.idUsuario = id
        db.session.commit()
        id += 1

@usuario_blueprint.route('/eliminar', methods=['GET', 'POST'])
def eliminar_usuario():
    if request.method == 'GET':
        return render_template('elimina_usuario.html')
    else:
        email = request.form['email']
        password = request.form['password']
        usuario = Usuarios.query.filter(Usuarios.email == email, Usuarios.password == password).first()
        if usuario == None :
            flash("ERROR: Usuario no encontrado")
            return render_template('elimina_usuario.html')
        elif usuario.idUsuario == Rentar.query.filter(Rentar.idUsuario == usuario.idUsuario).first().idUsuario:
            flash("ERROR: El usuario no puede ser eliminado, rento una película")
            return render_template('elimina_usuario.html')
        db.session.delete(usuario)
        db.session.commit()
        actualizar_ids()
        return render_template('usuario_eliminado.html', nombre=nombre)

@usuario_blueprint.route('/usuarios')
def ver_usuarios():
    usuarios = Usuarios.query.all()
    return render_template('ver_usuarios.html', usuarios=usuarios)