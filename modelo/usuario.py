from sqlalchemy import Column, Integer, String, Boolean, BLOB
from modelo  import db

class Usuarios(db.Model):

    __tablename__ = 'usuario'
    idUsuario = Column(Integer, nullable=False, primary_key=True)
    nombre = Column(String(200), nullable=False)
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

    def __str__(self):
        return f'Nombre del usuario: {self.nombre} {self.apPat} {self.apMat}\n - Id: {self.idUsuario}\n - Correo: {self.email}\n - Contraseña: {self.password}\n - Rol: {self.superUser}\n'