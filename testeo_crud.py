from crud_ import *

print(" PRUEBAS CRUD")

print(" Crear")
resultado = crear("productos", {
    "nombre": "Atarashii Gakko - Vinyl",
    "genero": "J-Pop",
    "precio": 150
})
print(resultado)


print("Leer")
resultado = leer("productos")
print(resultado[:2] if isinstance(resultado, list) else resultado)

print("Actualizar")
resultado = actualizar(
    "productos",
    {"nombre": "Atarashii Gakko - Vinyl"},
    {"precio": 170}
)
print(resultado)


print("Eliminar")
resultado = eliminar(
    "productos",
    {"nombre": "Atarashii Gakko - Vinyl"}
)
print(resultado)


print("\n PRUEBAS DE MANEJO DE ERRORES ")

print(crear("", {"a": 1}))

print(crear("productos", {}))

print(leer("coleccion_falsa"))

print(actualizar("productos", {}, {"precio": 100}))

print(eliminar("productos", {"nombre": "NoExiste"}))

print("\n====== FIN DE PRUEBAS ======")

