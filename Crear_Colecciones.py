from pymongo.errors import CollectionInvalid
from conexion import db

def crear_colecciones():
    colecciones = ["empleados", "productos", "clientes", "ventas"]
    for col in colecciones:
        try:
            db.create_collection(col)
            print(f"Colección {col} creada")
        except CollectionInvalid:
            print(f"Colección {col} ya existe")

def insertar_datos():
    if db.productos.count_documents({}) == 0:
        db.productos.insert_one({
            "nombre": "Vinilo Queen",
            "precio": 120,
            "stock": 5
        })
        print("Datos insertados")

if __name__ == "__main__":
    crear_colecciones()
    insertar_datos()
