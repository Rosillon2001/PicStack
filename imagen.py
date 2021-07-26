from app import db
from sqlalchemy import ForeignKey

class Imagen(db.Model):
    __tablename__ = 'imagen'
    id_imagen = db.Column(db.Integer, primary_key=True)
    ruta_imagen = db.Column(db.String(200), nullable=False)
    nombre_imagen = db.Column(db.String(60), nullable=False)
    autor = db.Column(db.String(60), nullable=False)
    tags = db.Column(db.String, nullable = False)
    id_repo = db.Column(db.Integer, db.ForeignKey('repositorio.id_repo', ondelete = 'CASCADE', onupdate = 'CASCADE'))

    def __init__(self, ruta_imagen, nombre_imagen, autor, tags, id_repo):
        self.ruta_imagen = ruta_imagen
        self.nombre_imagen = nombre_imagen
        self.autor = autor
        self.tags = tags
        self.id_repo = id_repo