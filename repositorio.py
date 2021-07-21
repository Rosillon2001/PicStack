from app import db
from sqlalchemy import ForeignKey

class Repositorio(db.Model):
    __tablename__ = 'repositorio', 
    id_repo = db.Column(db.Integer, primary_key=True)
    nombre_repo = db.Column(db.String(60), nullable=False, unique=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('id_usuario'))

    def __init__(self, id_repo, nombre_repo, id_usuario):
        self.id_repo = id_repo
        self.nombre_repo = nombre_repo
        self.id_usuario = id_usuario
