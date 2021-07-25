from sqlalchemy.orm import backref
from app import db

class User(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(60), nullable=False, unique=True)
    clave = db.Column(db.String(150), nullable=False)
    relacion = db.relationship('Repositorio', backref = 'usuario', passive_deletes = True)

    def __init__(self, nombre_usuario, clave):
        self.nombre_usuario = nombre_usuario
        self.clave = clave