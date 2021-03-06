from re import search
from app import db
from imagen import Imagen
from sqlalchemy import text


def create_image(request):
    data = []
    etiquetas = []

    ruta = request.files['rutaImagen']
    file = ruta.filename
    data.append(ruta)

    nombre = request.form['tituloImagen']
    data.append(nombre)

    autor = request.form['autorImagen']
    data.append(autor)

    tags = request.form['tagsImagen']
    etiquetas = tags.split('#')
    del etiquetas[0]
    for i in range (0, len(etiquetas)):
        cadena = etiquetas[i]
        cadenaLimpia = cadena.strip()
        etiquetas[i] = "#"+cadenaLimpia
    data.append(etiquetas)
    print(etiquetas)

    idRepo = request.form['repoImagen']
    data.append(idRepo)


    return data

def nombre_disponible(nombre):
    imgNameDB = ''
    existencia = db.session.query(Imagen).filter(Imagen.nombre_imagen == nombre)
    for row in existencia:
        imgNameDB = row.nombre_imagen
    if imgNameDB == nombre:
        return False
    else:
        return True

def imag_data(id):
    img = Imagen.query.get(id)
    return {
        "id": img.id_imagen,
        "ruta": img.ruta_imagen,
        "nombre": img.nombre_imagen,
        "autor": img.autor,
        "tags": img.tags,
        "repo": img.id_repo
    }

def repo_images(idrepo):
    images = db.session.query(Imagen).filter(Imagen.id_repo == idrepo)
    imgList = []
    for row in images:
        sin = row.tags.copy()
        for i in range (0, len(sin)):
            tags = sin[i]
            tags = tags.strip("#")
            sin[i] = tags
        img = {
            'id':row.id_imagen,
            "ruta": row.ruta_imagen,
            "nombre": row.nombre_imagen,
            "autor": row.autor,
            "tags": row.tags, 
            "nonum":sin
        }
        imgList.append(img)
    return imgList

def delete_img(id):
    data = []
    data.append(imag_data(id))
    img = Imagen.query.get(id)
    db.session.delete(img)
    db.session.commit()
    data.append({'mensaje':'Imagen eliminada'})

    return data

def allimg():
    images = Imagen.query.all()
    image_list = []
    for img in images:
        sin = img.tags.copy()
        for i in range (0, len(sin)):
            tags = sin[i]
            tags = tags.strip("#")
            sin[i] = tags
        datos = {
            'id_imagen':img.id_imagen, 
            'ruta_imagen':img.ruta_imagen,
            'nombre_imagen':img.nombre_imagen, 
            'autor':img.autor,
            'tags':img.tags, 
            'nonum':sin
        }
        image_list.append(datos)

    return image_list

def img_by_tag(tag):
    resultados = []
    sin = ''
    queryDB = db.session.query(Imagen).from_statement(text("select *from imagen where :tag = ANY(tags)")).params(tag = tag).all()
    for img in queryDB:
        
        sin = img.tags.copy()
        for i in range (0, len(sin)):
            tags = sin[i]
            tags = tags.strip("#")
            sin[i] = tags
            
        datos = {
            'id_imagen':img.id_imagen, 
            'ruta_imagen':img.ruta_imagen,
            'nombre_imagen':img.nombre_imagen, 
            'autor':img.autor,
            'tags':img.tags,
            'nonum':sin
        }

        resultados.append(datos)
    return resultados

def search_by_tag(request):
    tag = request.form['searchTag']
    resultados = img_by_tag(tag)

    return resultados

def busqueda(request):
    search = []
    tag = request.form['searchTag']
    search.append(tag)
    return search