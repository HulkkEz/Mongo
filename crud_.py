from conexion import db
from pymongo.errors import PyMongoError  

print("hola")

def crear(coleccion, datos):
    try:
        if not coleccion or not datos:
            return "Error: colección o datos vacíos"

        if coleccion not in db.list_collection_names():
            return f"Error: la colección '{coleccion}' no existe"

        result = db[coleccion].insert_one(datos)
        return f"Documento creado con ID {result.inserted_id}"

    except PyMongoError as e:
        return f"Error MongoDB: {e}"


def leer(coleccion, filtro={}):
    try:
        if not coleccion:
            return "Error: colección vacía"

        if coleccion not in db.list_collection_names():
            return f"Error: la colección '{coleccion}' no existe"

        return list(db[coleccion].find(filtro, {"_id": 0}))

    except PyMongoError as e:
        return f"Error MongoDB: {e}"


def actualizar(coleccion, filtro, datos):
    try:
        if not coleccion or not filtro or not datos:
            return "Error: parámetros incompletos"

        if coleccion not in db.list_collection_names():
            return f"Error: la colección '{coleccion}' no existe"

        result = db[coleccion].update_one(filtro, {"$set": datos})

        if result.matched_count == 0:
            return "Error: documento no encontrado"

        return "Documento actualizado correctamente"

    except PyMongoError as e:
        return f"Error MongoDB: {e}"


def eliminar(coleccion, filtro):
    try:
        if not coleccion or not filtro:
            return "Error: parámetros incompletos"

        if coleccion not in db.list_collection_names():
            return f"Error: la colección '{coleccion}' no existe"

        result = db[coleccion].delete_one(filtro)

        if result.deleted_count == 0:
            return "Error: documento no encontrado"

        return "Documento eliminado correctamente"

    except PyMongoError as e:
        return f"Error MongoDB: {e}"


