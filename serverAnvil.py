from pymongo import MongoClient
import anvil.server

URI = "mongodb+srv://..."

client = MongoClient(URI)
db = client["Tienda"]

@anvil.server.callable
def agregar_producto(nombre, precio):
  db.productos.insert_one({
    "nombre": nombre,
    "precio": precio
  })
  return "Producto agregado correctamente"

@anvil.server.callable
def listar_productos():
  return list(db.productos.find({}, {"_id": 0}))

@anvil.server.callable
def eliminar_producto(nombre):
    result = db.productos.delete_one({"nombre": nombre})
    if result.deleted_count == 0:
        return "Producto no encontrado"
    return "Producto eliminado"

@anvil.server.callable
def filtrar_productos(campo, orden, limite):
   campo = campo.lower()
   if campo not in ["precio", "nombre"]:
     return []

   orden_mongo = 1 if orden == "asc" else -1

   return list(
     db.productos
      .find({}, {"_id": 0})
      .sort(campo, orden_mongo)
      .limit(limite)
    ) 

