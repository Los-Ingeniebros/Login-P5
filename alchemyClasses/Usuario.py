from sqlalchemy import Column, Integer, String, Boolean, BLOB
from alchemyClasses import db

class Usuario(db.Model):

    __tablename__ = 'usuario'
    idUsuario = Column(Integer, nullable=False, primary_key=True)
    nombre = Column(String(200), nullable=False)
    contrasenia = Column(String(64), nullable=False)

    def __init__(self, idUsuario, nombre, contrasenia):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.contrasenia = contrasenia

    def __str__(self):
        return f'Nombre del usuario: {self.nombre}\n - Id: {self.idUsuario}\n - Contraseña: {self.contrasenia}'