from sqlalchemy.orm import backref
from app import db
from sqlalchemy import ForeignKey

class Repositorio(db.Model):
    __tablename__ = 'repositorio' 
    id_repo = db.Column(db.Integer, primary_key=True)
    nombre_repo = db.Column(db.String(60), nullable=False, unique=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    relacion = db.relationship('Imagen', backref = 'repositorio')

    def __init__(self, nombre_repo, id_usuario):
        self.nombre_repo = nombre_repo
        self.id_usuario = id_usuario
