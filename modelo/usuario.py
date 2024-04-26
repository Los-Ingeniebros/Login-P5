from sqlalchemy import Column, Integer, String, Boolean, BLOB
from modelo  import db
from flask import Flask, redirect, render_template, url_for, request, flash, session, Blueprint

class Usuarios(db.Model):

    __tablename__ = 'usuario'
    user_id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String(200), nullable=False)
    # apPat = Column(String(200), nullable=False)
    # apMat = Column(String(200))
    password = Column(String(64), nullable=False)
    # email = Column(String(500), default=None, unique=True)
    # rol = Column(Boolean, default=None)

    def __init__(self, idUsuario, nombre, password):
        self.idUsuario = idUsuario
        self.nombre = nombre
        # self.apPat = apPat
        # self.apMat = apMat
        self.password = password
        # self.email = email
        # self.rol = rol
        
    #Sugerencia, después poner las funciones en los modelos de tal manera que en app.py no tengamos eso y solo lo mandemos a llamar
    def sesion(self, nombre, password):
        if session.get('user_id') != None:
            return render_template('login.html', user=session['user_id'])
        if request.method == 'GET':
            return render_template('index.html')
        
        name = request.form.get('username')
        passwd = request.form.get('password')
        
        for registro in Usuarios.query.all():
                id += 1
                if name == registro.nombre and passwd == registro.password:
                    flash("ERROR: Pon otro correo!")
                else:
                    session['user_id'] = name #definición de cookie de sesión.
                    return render_template('login.html', user=name)
        return redirect(url_for('login'))

    def __str__(self):
        return f'Nombre del usuario: {self.nombre} {self.apPat} {self.apMat}\n - Id: {self.idUsuario}\n - Correo: {self.email}\n - Contraseña: {self.password}\n - Rol: {self.superUser}\n'