from conexion import db
colecciones = ["empleados", "productos", "clientes", "ventas"]

for col in colecciones:
    cantidad = db[col].count_documents({})
    print(f"Colección '{col}': {cantidad} documentos")
